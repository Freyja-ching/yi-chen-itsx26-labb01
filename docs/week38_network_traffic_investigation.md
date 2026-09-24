# Network Traffic Investigation

## A. Miljö och capture

### Miljö

Undersökningen genomfördes i min egen WSL2 Ubuntu-miljö på Windows.

Jag använde:

* WSL2 Ubuntu
* `tcpdump`
* Wireshark 4.6.4
* nätverksinterface `eth0`

Jag kontrollerade nätverksmiljön med:

```text
ip -br a
ip route
```

Min lokala nätverksadress och gateway är anonymiserade i denna rapport.

Capture gjordes med:

```bash
sudo tcpdump -i eth0 -s 0 -c 5000 -w trafikmix.pcap
```

Capture var begränsad till maximalt 5000 paket. Totalt fångades **47 paket under cirka 24 sekunder**. Inga paket rapporterades som tappade under capture.

Jag skapade kontrollerad trafik med:

* ICMP med `ping`
* DNS-förfrågan med `dig`
* HTTP med `curl`
* HTTPS med `curl`

Den råa pcap-filen sparas lokalt och laddas inte upp till GitHub.

### Sanitization

Av säkerhetsskäl är IP-adresser och hostnames anonymiserade i denna rapport.

Jag använder därför följande namn:

* `CLIENT_IP` = min lokala klientadress
* `SERVER_IP` = extern serveradress
* `ICMP_TARGET` = ICMP-testadress
* `GATEWAY` = lokal default gateway
* `DNS_SERVER` = DNS-server
* `example.test` = anonymiserat hostname

Packet numbers, portar och protokoll är däremot baserade på min riktiga capture.

### Skillnad mot OCI-demo

Principerna är samma som i OCI, till exempel interface, IP-adress, route, TCP, portar och protokoll.

Skillnaden är att jag använde WSL2 i stället för en OCI-VM. WSL2 har en virtuell nätverksmiljö och därför kan IP-adresser och routing se annorlunda ut än i OCI.

---

# B. Från applikation till destination

Jag analyserade HTTPS-flödet som ett exempel på hur trafik går från applikationen till destinationen.

Flödet kan beskrivas så här:

```text
Application
    ↓
CLIENT_IP
    ↓
Default route / GATEWAY
    ↓
NAT/PAT i nätverksmiljön
    ↓
SERVER_IP
    ↓
TCP port 443
    ↓
TLS / HTTPS
```

Först skapar klienten en nätverksanslutning. Den lokala datorn använder sitt nätverksinterface och sin routingtabell för att bestämma vart trafiken ska skickas.

Jag kontrollerade default route med:

```bash
ip route
```

Där finns en default route via en gateway.

### DNS

Jag använde `dig` för att testa DNS:

```bash
dig example.test
```

DNS-förfrågan fungerade och gav en IP-adress. DNS-trafik observerades däremot inte i den sparade pcap-filen.

Det betyder att DNS fungerade under testet, men capture visar inte själva DNS-paketen.

### NAT/PAT

Eftersom jag arbetade i WSL2 finns en virtuell nätverksmiljö mellan min Linux-miljö och det externa nätverket.

NAT kan översätta en privat intern adress till en annan adress när trafiken lämnar den lokala miljön. PAT kan även använda portar för att skilja olika anslutningar åt.

Detta är en nätverksteknisk förklaring och är inte något som jag kan bevisa direkt från varje paket i min capture.

### Firewall

En firewall kan vara en möjlig kontrollpunkt mellan klienten och destinationen.

För HTTPS skulle en utgående regel som tillåter TCP till port 443 kunna påverka anslutningen.

Capture visar att anslutningen lyckades, men den visar inte hela firewall-konfigurationen.

### Observerat eller förklarat?

Följande kunde observeras direkt i pcap:

* IP-adresser
* portar
* TCP
* TCP handshake
* TLS-meddelanden
* HTTP
* packet sequence

Följande är nätverkstekniska förklaringar:

* exakt NAT/PAT-funktion utanför Linux-miljön
* hela firewall-konfigurationen
* vad som händer i nätverk som inte finns med i capture

---

# C. Protokoll och paket

## Protocol inventory

| Protokoll | Observerat? | Evidens                                                |
| --------- | ----------- | ------------------------------------------------------ |
| DNS       | Nej         | DNS-testet fungerade, men DNS-paket syntes inte i pcap |
| ICMP      | Ja          | Packet 1–6                                             |
| TCP       | Ja          | HTTP- och HTTPS-flöden                                 |
| HTTP      | Ja          | Packet 16 och 18                                       |
| TLS       | Ja          | Packet 26, 29 och senare Application Data              |
| HTTPS     | Ja          | TCP port 443 + TLS                                     |

### DNS

Jag testade DNS med `dig`.

DNS-förfrågan fungerade, men när jag filtrerade efter DNS i Wireshark hittade jag ingen DNS-trafik i den sparade capture-filen.

Det kan bero på att DNS-trafiken inte gick genom det interface som fångades eller att DNS-informationen redan fanns tillgänglig på annat sätt när capture startade.

Därför skriver jag inte att DNS "inte hände". Jag kan bara säga att **DNS-trafik inte observerades i denna capture**.

---

## ICMP

Packet 1–6 visar ICMP Echo Request och Echo Reply.

Sekvensen var:

```text
1  Echo Request
2  Echo Reply
3  Echo Request
4  Echo Reply
5  Echo Request
6  Echo Reply
```

Det visar att ICMP-kommunikationen fungerade under testet.

Det visar däremot inte att nätverket alltid kommer att vara tillgängligt.

---

## TCP handshake för HTTP

HTTP-flödet började med en vanlig TCP three-way handshake:

```text
Packet 13  SYN
Packet 14  SYN, ACK
Packet 15  ACK
```

Detta visar att TCP-anslutningen etablerades.

---

## HTTP request och response

Efter TCP-handshaken observerades:

```text
Packet 16  HTTP HEAD request
Packet 18  HTTP 200 OK
```

Requesten innehöll:

```text
HEAD / HTTP/1.1
```

Response innehöll:

```text
HTTP/1.1 200 OK
```

Det visar att HTTP-kommunikationen fungerade och att servern svarade med statuskod 200.

Därefter stängdes TCP-anslutningen
