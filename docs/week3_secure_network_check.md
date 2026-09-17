
# Secure Network Check

## Syfte och säkerhetsgräns

Syftet med skriptet är att kontrollera grundläggande nätverksfunktioner och lokala tjänster i Linux-miljön.

Kontrollerna är begränsade till den egna Linux-miljön och localhost. Skriptet gör ingen nätverksskanning och ändrar inte brandväggsregler.

## Miljö

Arbetet genomfördes i WSL2 med Ubuntu på Windows.

Användare: `yiching`
Hostname: `Ching-Chen`
Python-version: 3.14.4

Tester med lokal HTTP-tjänst genomfördes på `127.0.0.1:8080`.

## Kontroller

Följande kontroller genomfördes i WSL-miljön:

- `ip address` - visar nätverksinterface och IP-adresser.
- `ip route` - visar routing och default route.
- `getent hosts google.com` - kontrollerar DNS-upplösning.
- `ss -tuln` - visar lokalt lyssnande portar.
- `curl -I http://127.0.0.1:8080` - kontrollerar den lokala HTTP-tjänsten.
- `ps` - visar körande processer.

Kontrollerna visar vad som är observerbart i WSL-miljön. De bevisar inte att nätverket fungerar på samma sätt som i en OCI-miljö, eftersom WSL har en annan nätverksmiljö.

## Testresultat

### Test 1 - DNS fungerar

DNS-uppslagningen lyckades med `getent hosts google.com`.

**Observation:** `google.com` kunde översättas till en IP-adress.

**Slutsats:** DNS fungerar i WSL-miljön.

### Test 2 - Lokal tjänst fungerar

Den lokala HTTP-tjänsten startades på `127.0.0.1:8080`. `curl` fick HTTP 200 som svar.

**Observation:** En lokal HTTP-tjänst lyssnade på port 8080 och svarade på localhost.

**Slutsats:** Den lokala tjänsten var tillgänglig från WSL-miljön.

### Test 3 - Tomt DNS-värde

När `DNS_HOST` sattes till ett tomt värde gav skriptet status `WARN` och fortsatte utan att krascha.

**Observation:** Skriptet upptäckte det tomma värdet innan DNS-uppslagningen kördes.

**Slutsats:** Skriptet hanterar ett tomt DNS-värde på ett kontrollerat sätt.

### Test 4 - Ingen lokal tjänst

När den lokala HTTP-tjänsten var stoppad misslyckades anslutningen till `127.0.0.1:8080`.

**Observation:** Ingen lokal tjänst lyssnade på port 8080.

**Slutsats:** Skriptet upptäckte att tjänsten inte var tillgänglig och avslutades med exit code `1`.

Mer detaljerade testdokumentation finns i `evidence/README.md`.

## CIA-triaden

### Confidentiality

Skriptet begränsar kontrollerna till den egna Linux-miljön och localhost. Känslig information som lösenord, nycklar och tokens ska inte inkluderas i loggar eller evidens.

### Integrity

Skriptet använder statusar och tidsstämplar i loggen för att göra resultaten tydligare och spårbara. Git används för versionshantering av skript och dokumentation.

### Availability

Kontroller av DNS, routing, lokala tjänster och lyssnande portar kan visa om viktiga nätverksfunktioner är tillgängliga.

### Säkerhet kontra tillgänglighet

En säkerhetsåtgärd kan påverka tillgängligheten om den konfigureras för strikt. Därför behöver ändringar testas så att legitima tjänster och anslutningar fortfarande fungerar.

## Koppling till tidigare säkerhetsarbete

### Hardening

Efter hardening kan `ss -tuln` användas för att kontrollera vilka portar och tjänster som fortfarande lyssnar.

Det gör det möjligt att jämföra det observerade läget med vilka tjänster som förväntas vara aktiva.

### Recovery

Efter en återställning skulle jag först kontrollera routing med `ip route` och DNS med `getent hosts google.com`.

Routingkontrollen visar om nätverksvägen finns. DNS-kontrollen visar om namn kan översättas till IP-adresser.

Dessa kontroller kan göras innan man går vidare till kontroller av högre nivå, till exempel lokala tjänster.

## Reflektion

### Mest värdefulla kontrollen

Den lokala servicekontrollen var en viktig kontroll eftersom den visar om en tjänst faktiskt svarar på localhost. Den kopplar ihop port, tjänst och anslutning på ett konkret sätt.

### Skillnad i miljö

Arbetet genomfördes i WSL2 och inte på en OCI-VM. WSL har en annan nätverksmiljö, vilket påverkar bland annat IP-adresser och routing. Därför kan resultaten inte förväntas vara exakt samma som i OCI.

### Svåraste felet att tolka

Ett fel som behövde tolkas var när `curl` inte kunde ansluta till port 8080. Felet berodde på att den lokala testtjänsten inte körde. Genom att kontrollera porten och starta tjänsten igen kunde felet förstås.

### Förbättringar i en framtida version

En framtida version skulle kunna ge tydligare information om varje kontroll och göra sammanfattningen ännu lättare att läsa.

### Säker användning

Skriptet ska användas i den egna miljön eller mot system där man har tillstånd att testa. Det ska inte användas för nätverksskanning eller mot externa system utan godkännande.

## Cleanup

Den lokala HTTP-testtjänsten stoppades efter testerna med `Ctrl+C`.

Skriptet skapade inga tillfälliga systemförändringar eller brandväggsregler. Loggfilen ska kontrolleras och inte publiceras om den innehåller känslig information.

## AI-deklaration

AI-deklaration

Jag använde ChatGPT som stöd för att förklara Bash-syntax, diskutera skriptets struktur och kontrollera dokumentationens tydlighet.

Jag använde förslag om variabler, funktioner, villkor, loop, loggning och testfall när de passade uppgiftens krav. Jag valde bort förslag som gjorde skriptet mer avancerat än nödvändigt eller som inte behövdes för uppgiften.

Jag verifierade kommandon och skript genom egna tester i WSL Ubuntu, bland annat DNS-kontroll, lokal HTTP-tjänst, tomt DNS-värde och test mot en port där ingen tjänst lyssnade. Jag kontrollerade även skriptets syntax med bash -n.

Jag använde kursens uppgiftsinstruktioner som grund för kraven och ansvarar själv för den slutliga koden, testerna, resultaten och dokumentationen. Jag har själv utformat och anpassat skriptets kontroller och testning till min WSL-miljö.
