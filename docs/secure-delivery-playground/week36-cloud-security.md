# Week 36 Cloud Security Lab

## 1. Min VM
- Projekt: ITSX26 Cloud Security Lab
- VM-namn: instance-20260907-1850
- Zon: eu-stockholm-1 (AD-1)
- Operativsystem: Ubuntu 24.04 LTS
- Inloggningsmetod: SSH Key via PowerShell

## 2. Linux-kommandon
| Kommando | Vad visar det? | CIA-koppling |
|---|---|---|
| whoami | Visar att jag är inloggad som användaren ubuntu | Confidentiality / Integrity |
| hostname | Visar serverns namn instance-20260907-1850 | Integrity |
| pwd | Visar att jag står i mappen /home/ubuntu | Confidentiality |
| uname -a | Visar systeminformation och Linux kernel version | Integrity / Availability |
| uptime | Visar hur länge servern har varit igång sedan start | Availability |

## 3. Hardening-checklista
| Kontroll | Åtgärd | Verifiering | CIA-koppling |
|---|---|---|---|
| Identitet | Körde whoami, id och groups för att kolla min användare | Såg att jag var ubuntu och hade sudo rättigheter | Confidentiality / Integrity |
| Filrättigheter | Skapade filen test.txt och körde chmod 600 test.txt | Körde ls -l test.txt och såg att rättigheten ändrades till -rw------- | Confidentiality |
| Systemuppdatering | Körde sudo apt update och apt list --upgradable | Fick fram en lista på alla tillgängliga uppdateringar | Integrity / Availability |
| Processer | Körde ps aux \| head för att se igångvarande processer | Verifierade att vanliga systemprocesser rullade på servern | Availability / Integrity |

## 4. Recovery-plan
- Vad kan gå fel? SSH slutar fungera, man blir utelåst på grund av brandväggsregler eller felaktiga filrättigheter.
- Hur upptäcker jag felet? Anslutningen i PowerShell tajmar ut eller säger Connection refused.
- Vilket Google Cloud/OCI-verktyg använder jag? OCI Console, Ingress Rules och Boot Volume Snapshots.
- Hur återställer jag? Starta om VM:en via Console för att låsa upp sshd, eller återställa från en Snapshot.

## 5. Backup-strategi
- Snapshot/backup: Ta en Boot Volume Snapshot i Console innan man ändrar viktiga inställningar.
- GitHub-evidens: Alla labbrapporter i docs och skript sparas och pushas till GitHub.
- Vad kan återskapas: Alla skript, rapporter och konfigurationer kan laddas ner igen från GitHub.
- Vad kan inte återskapas: Tillfälliga filer eller loggar som låg på VM:en och inte skickats till GitHub.

## 6. Resource cleanup
- VM: Stoppad och raderad (Terminate) i Console.
- Diskar: Boot Volume raderas tillsammans med VM:en.
- Snapshots: Gamla temporära snapshots och nycklar rensas.
- IP-adresser: Den publika IP-adressen frigörs.
- Firewall-regler: Inga öppna portar lämnas kvar.

## 7. Reflektion
- Konfidentialitet: Vi använde SSH-nycklar och ändrade rättigheter med chmod 600 så att obehöriga inte kan läsa filer.
- Integritet: Vi kontrollerade att rätt användare har sudo och kollade efter systemuppdateringar.
- Tillgänglighet: Vi kollade att systemet mår bra med uptime och ps aux, samt har en plan för vad vi gör om SSH kraschar.

## 8. Egen reflektion
- Vad fungerade bra: Det gick bra att ansluta via PowerShell med mitt SSH-key när jag väl fick det att fungera.
- Vad var svårt: Jag hade stora problem med att ansluta via VS Code och trodde först att det berodde på att jag hade för många resurser igång. Därför skapade jag om VM:en tre gånger.
- Vad lärde jag mig: 
  1. Jag lärde mig hur chmod 600 ändrar filrättigheter och skyddar känslig data.
  2. Jag lärde mig hur cloud cleanup fungerar i praktiken: Jag insåg att man inte kan radera ett subnet direkt, utan måste radera VM:en och dess nätverkskort först. Det gav mig en bra förståelse för hur resurser i molnet hänger ihop.