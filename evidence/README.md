# Evidence - Network Traffic Investigation

## Pcap-källa

Pcap-filen skapades av mig i min egen WSL2 Ubuntu-miljö.

Jag skapade kontrollerad trafik med:

* ICMP med `ping`
* DNS-förfrågan med `dig`
* HTTP-trafik med `curl`
* HTTPS-trafik med `curl`

Capture gjordes med `tcpdump`:

```bash
sudo tcpdump -i eth0 -s 0 -c 5000 -w trafikmix.pcap
```

Capture-gränsen var 5000 paket. Totalt fångades **47 paket** under ungefär **24 sekunder**.

Den råa pcap-filen sparas lokalt och laddas inte upp till GitHub.

## Analysdatum

Analysen genomfördes 24 september 2026.

## Miljö

Analysen genomfördes i:

* Windows med WSL2
* Ubuntu
* Wireshark 4.6.4
* tcpdump
* Nätverksinterface: `eth0`

## Sanering

Rå pcap-data publiceras inte i GitHub.

I rapporten används endast relevant nätverksevidens, till exempel packet numbers, protokoll, portar och observerade händelser.

Känsliga uppgifter som lösenord, nycklar, tokens och cookies har inte inkluderats.
