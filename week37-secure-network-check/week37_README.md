# Evidence - Secure Network Check

Testerna genomfördes i WSL Ubuntu.

Ingen känslig information som lösenord, nycklar eller tokens har inkluderats.

## Test 1 - DNS fungerar

**Kommando:**
`getent hosts google.com`

**Resultat:**
DNS-uppslagningen lyckades.

**Observation:**
`google.com` kunde översättas till en IP-adress.

**Slutsats:**
DNS fungerar i WSL-miljön.

## Test 2 - Lokal tjänst fungerar

**Kommando:**
`curl -I http://127.0.0.1:8080`

**Resultat:**
HTTP-förfrågan lyckades och tjänsten svarade med HTTP 200.

**Observation:**
En lokal HTTP-tjänst lyssnade på port 8080 och svarade på localhost.

**Slutsats:**
Den lokala tjänsten var tillgänglig från WSL-miljön.

## Test 3 - Tomt DNS-värde

**Test:**
`DNS_HOST=""`

**Resultat:**
Skriptet gav status `WARN` och fortsatte utan att krascha.

**Observation:**
Skriptet upptäckte att DNS-värdet var tomt innan DNS-uppslagningen kördes.

**Slutsats:**
Skriptet hanterar ett tomt DNS-värde på ett kontrollerat sätt.

## Test 4 - Ingen lokal tjänst på porten

**Kommando:**
`bash scripts/secure_network_check.sh`

**Resultat:**
Anslutningen till `127.0.0.1:8080` misslyckades. Skriptet gav `FAIL: 1` och exit code `1`.

**Observation:**
Ingen lokal tjänst lyssnade på port 8080 när testet kördes.

**Slutsats:**
Skriptet upptäckte att den lokala tjänsten inte var tillgänglig och avslutades med en felkod.
