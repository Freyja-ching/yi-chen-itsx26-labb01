# Security Automation Report

## Syfte

Syftet med projektet är att använda Python för att läsa och analysera syntetiska loggfiler.

Programmet räknar säkerhetsrelevanta händelser, sammanställer source IP-adresser och jämför IP-adresser med en indikatorlista.

Programmet skapar sedan en säkerhetsrapport i `output/security_report.txt`.

Originalfilerna i `data/` ändras inte.

## Dataset

Programmet använder data från följande filer:

* `auth.log` – innehåller login-händelser.
* `access.log` – innehåller HTTP-förfrågningar och statuskoder.
* `firewall.log` – innehåller firewall-händelser.
* `suspicious_ips.txt` – innehåller IP-adresser som används som indikatorer.

Data är syntetiska och används för kursuppgiften.

## Python-version

Programmet använder Python 3.

Jag använde:

`Python 3.14.4`

## Hur programmet körs

Programmet ska köras från projektets mapp.

Kommando:

```bash
python3 src/security_report.py
```

Programmet läser data från `data/` och skriver resultatet till:

`output/security_report.txt`

## Filer och mappar

Projektet innehåller:

* `README.md` – information om projektet och hur programmet körs.
* `data/` – loggfiler och indikatorlistan.
* `src/` – Python-programmet `security_report.py`.
* `output/` – den skapade säkerhetsrapporten.
* `docs/` – analysen av resultatet.

## Resultat

Programmet räknar bland annat:

* antal misslyckade inloggningar
* antal förekomster per source IP i `auth.log`
* antal `401`-svar i `access.log`
* matchningar med indikatorlistan
* antal rader som saknar source IP

Med samma data ska programmet ge samma resultat när det körs igen.

## Felhantering

Programmet kontrollerar om en loggrad innehåller `src=`.

Om en rad saknar source IP hoppas raden över. Programmet fortsätter sedan att läsa nästa rad.

Programmet rapporterar också hur många rader som hoppades över.

I testdatan finns en rad:

`Malformed line without source`

Den saknar `src=` och räknas därför som en överhoppad rad.

## Begränsningar

Programmet analyserar endast de loggfiler som finns i projektets `data/`-mapp.

Data är syntetiska och visar bara en begränsad mängd händelser.

En IP-adress som finns i indikatorlistan är inte automatiskt bevis på ett angrepp. Resultatet används som underlag för vidare analys.

Programmet använder inga externa API:er eller externa threat feeds.

Programmet blockerar inte IP-adresser och ändrar inte firewall- eller systeminställningar.

## Testing

### Test 1: Känt positivt test

Jag kontrollerade `auth.log` manuellt och räknade 4 rader med `Failed login`.

Förväntat resultat:

`Misslyckade inloggningar: 4`

Programmets resultat:

`Misslyckade inloggningar: 4`

Resultat: PASS

Det manuella resultatet stämmer med programmets resultat.

### Test 2: Inga träffar

Jag skapade ett separat testfall där indikatorlistan endast innehöll `10.10.10.10`.

Ingen av de observerade IP-adresserna i `auth.log` matchade denna adress.

Förväntat resultat:

Ingen matchning med indikatorlistan.

Manuell kontroll:

0 matchningar.

Detta användes som ett separat kontrollfall för zero-match. Testet kördes inte med programmets ordinarie `data/suspicious_ips.txt`.

### Test 3: Felaktig rad

`auth.log` innehåller en rad utan `src=`:

`Malformed line without source`

Förväntat resultat:

Raden ska hoppas över och programmet ska fortsätta köra.

Programmets resultat:

`Överhoppad rad: saknar source IP`

Rapporten visar också:

`Överhoppade rader: 1`

Resultat: PASS

Testet visar att programmet kan hantera en rad som saknar source IP utan att stoppa körningen.

## AI-stöd

Jag använde AI som stöd under arbetet med uppgiften. Jag använde AI främst för att förstå Python-kod, hitta fel i koden och få hjälp att formulera dokumentationen.

Jag testade själv programmet med kursens data och jämförde resultatet med manuella kontroller. På så sätt kontrollerade jag att resultatet stämde.

Jag har gått igenom hur programmet läser loggarna, räknar händelser, jämför IP-adresser och skriver resultatet till rapporten. Jag kan därför förklara programmets dataflöde och analyslogik.
