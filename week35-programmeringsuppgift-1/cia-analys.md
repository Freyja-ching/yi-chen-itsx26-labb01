# Del 4: CIA-analys

I denna analys utgår jag från hotet **Nätfiske (Phishing)** från Del 3 och analyserar dess påverkan på CIA-triaden (Konfidentialitet, Integritet och Tillgänglighet).

---

## Valt hot: Nätfiske (Phishing)
Nätfiske innebär att en angripare skickar ett förfalskat e-postmeddelande för att lura anställda att uppge sina inloggningsuppgifter till Microsoft 365 och HR-systemet.

---

## Påverkan på CIA-triaden

### 1. Konfidentialitet (Confidentiality) - HÖG PÅVERKAN
- **Hur påverkas principen?** Om en anställd blir lurad och anger sina inloggningsuppgifter får angriparen obehörig åtkomst till företagets Microsoft 365 och HR-system.
- **Konsekvens:** Känsliga personuppgifter (som personnummer, löneuppgifter och anställningsavtal) läcker ut till obehöriga. Konfidentialiteten bryts fullständigt.

### 2. Integritet (Integrity) - MEDEL TILL HÖG PÅVERKAN
- **Hur påverkas principen?** Med giltiga inloggningsuppgifter kan angriparen ändra, radera eller förfalska data i systemen.
- **Konsekvens:** Angriparen kan ändra utbetalningsuppgifter i HR-systemet eller skicka ut falska e-postmeddelanden i VD:ns namn (CEO Fraud). Data går inte längre att lita på.

### 3. Tillgänglighet (Availability) - LÅG TILL MEDEL PÅVERKAN
- **Hur påverkas principen?** Nätfiske i sig stänger inte nödvändigtvis ner systemen direkt, men om angriparen använder kontot för att installera Ransomware (utpressningstrojan) kan hela systemet låsas.
- **Konsekvens:** Om angriparen ändrar lösenordet och låser ute den rättmätiga användaren förlorar den anställde tillgång till sina verktyg och data.

---

## Sammanfattning och Åtgärd
För att skydda CIA-triaden mot detta hot krävs **Multifaktorautentisering (MFA)**. MFA säkerställer konfidentialiteten även om lösenordet läcker, vilket i sin tur skyddar systemets integritet och tillgänglighet.