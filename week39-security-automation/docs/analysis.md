# Analys

## Metod

Programmet läser data från `auth.log`, `access.log` och `suspicious_ips.txt`.

Från `auth.log` räknar programmet antal misslyckade inloggningar och sammanställer source IP-adresser. Programmet jämför sedan de observerade IP-adresserna med IP-adresserna i `suspicious_ips.txt`.

Från `access.log` räknar programmet antal `401`-svar och sammanställer source IP-adresser.

Programmet ändrar inte originalfilerna. Resultatet skrivs till `output/security_report.txt`.

## Observation

* I `auth.log` finns totalt 4 misslyckade inloggningar.

* IP-adressen `203.0.113.15` förekommer 3 gånger och `198.51.100.44` förekommer 1 gång bland de misslyckade inloggningarna.

* Båda IP-adresserna finns också i `suspicious_ips.txt`.

* I `access.log` finns 2 svar med status `401`. IP-adressen `203.0.113.15` förekommer också i `access.log`.

## Slutsats

Resultatet visar flera observationer som kan vara relevanta för en säkerhetsanalys. Framför allt förekommer `203.0.113.15` i flera datakällor och finns i indikatorlistan.

Detta kan vara en signal som behöver undersökas vidare, men resultatet bevisar inte att IP-adressen är en angripare.

## Osäkerhet

* Loggarna är syntetiska och visar bara en begränsad
tidsperiod. Programmet analyserar endast de data som finns i de använda loggfilerna.

* En IP-adress som finns i indikatorlistan är inte automatiskt bevis på ett angrepp. Det kan finnas andra förklaringar till observationerna.

* En rad i `auth.log` saknar source IP och kan därför inte användas i IP-sammanställningen. Programmet hoppar över raden och rapporterar detta som en överhoppad rad.

## Säkerhetsbetydelse

Flera misslyckade inloggningar från samma IP-adress kan vara relevant att undersöka, särskilt när samma IP-adress också förekommer i andra loggar och i indikatorlistan.

Resultatet kan därför användas som ett underlag för vidare analys. Det ska inte användas som ett automatiskt beslut om att blockera en IP-adress.

## Alternativ förklaring

En annan möjlig förklaring är att aktiviteten kan bero på felaktiga inloggningar, testaktivitet eller annan legitim aktivitet. Därför behövs mer information innan man kan dra en säker slutsats om vad som har hänt.