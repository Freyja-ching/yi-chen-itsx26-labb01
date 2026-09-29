# AI Security Case Investigation - Case A

## 1. Executive Summary

Flera medarbetare i en kommunal förvaltning har fått mejl som ser ut att komma från intern IT-support. I mejlen uppmanas mottagarna att använda en länk för att behålla åtkomsten till ett internt system. En medarbetare har klickat på länken. Det är ännu inte bekräftat om medarbetaren skrev in några uppgifter eller inloggningsuppgifter. Det är inte heller känt om andra medarbetare har klickat på länken utan att rapportera det.

Det behöver därför kontrolleras om länken kommer från en legitim källa och om mejlen är en del av ett phishingförsök. Det finns i nuläget ingen bekräftad incident eller bekräftad obehörig åtkomst. Om inloggningsuppgifter har lämnats ut kan ett användarkonto däremot utsättas för obehörig åtkomst. Det kan påverka information och interna system beroende på användarens behörigheter.

Den första åtgärden bör därför vara att kontrollera mejlet, avsändaren och länken. Därefter bör relevanta loggar kontrolleras för att se om det finns tecken på misstänkt aktivitet. Organisationen bör också ha kontroll över användarnas behörigheter för att begränsa möjliga konsekvenser om ett konto skulle vara komprometterat.

## 2. Fakta, antaganden och scope

### Fakta

Flera medarbetare har fått mejl som ser ut att komma från intern IT-support. Avsändarnamnet liknar intern IT-support och en medarbetare har klickat på länken. Det finns ingen bekräftad information om att någon har lämnat ut inloggningsuppgifter. Det finns inte heller någon bekräftad incident. Det är inte fastställt om mejlen har skapats med AI.

### Antaganden

Länken kan vara en del av ett phishingförsök. Om en medarbetare har lämnat ut inloggningsuppgifter kan användarkontot utsättas för obehörig åtkomst. Konsekvenserna beror bland annat på vilka behörigheter användarkontot har.

### Information som behöver verifieras

Organisationen behöver kontrollera om länken kommer från en legitim källa. Det behöver också kontrolleras om medarbetaren skrev in några uppgifter och om andra medarbetare har klickat på länken. Relevanta loggar bör kontrolleras för att se om det finns tecken på misstänkt aktivitet. Det behöver även kontrolleras vilka behörigheter det berörda användarkontot har.

### Scope

Analysen avgränsas till det misstänkta mejlet, länken, användarkonton, åtkomst till interna system och möjlig påverkan på information. Det finns inte tillräckligt med information för att fastställa att ett intrång har skett.

## 3. Tillgångar och händelsekedja

### Tillgångar

Följande tillgångar är relevanta för caset:

1. **Medarbetarnas användarkonton** – konton som används för åtkomst till interna system.
2. **Det interna systemet** – systemet som medarbetarna uppmanas att logga in till.
3. **Information i det interna systemet** – information som kan nås genom användarkonton.
4. **Organisationens e-postmiljö** – används för att skicka och ta emot mejlen.

### Händelsekedja

1. Flera medarbetare får mejl som ser ut att komma från intern IT-support.
2. En medarbetare öppnar länken i mejlet.
3. Länken kan leda till en falsk inloggningssida som försöker få användaren att lämna ut information.
4. Om användaren lämnar ut inloggningsuppgifter kan användarkontot utsättas för obehörig åtkomst.
5. Ett komprometterat konto kan ge åtkomst till interna system och information beroende på användarens behörigheter.

Steg 3–5 är möjliga scenarier och är inte bekräftade fakta i caset.

## 4. CIA och enkel riskbedömning

### Confidentiality

Confidentiality kan påverkas om en medarbetare har lämnat ut inloggningsuppgifter och någon obehörig får tillgång till användarkontot. Då kan information i interna system bli åtkomlig för obehöriga. Det är inte bekräftat att detta har hänt.

### Integrity

Integrity kan påverkas om ett användarkonto komprometteras och kontot har behörighet att ändra information eller system. En obehörig person kan då i vissa fall ändra information. Det är inte bekräftat att någon information har ändrats i detta case.

### Availability

Availability kan påverkas om ett komprometterat konto används för att störa eller påverka ett internt system. Det kan till exempel göra att information eller system inte fungerar som förväntat. Det finns dock ingen bekräftad störning i nuläget.

### Enkel riskbedömning

**Sannolikhet: Medel / osäker.** Flera medarbetare har fått mejlen och en medarbetare har klickat på länken. Samtidigt är det inte bekräftat att någon har lämnat ut inloggningsuppgifter eller att ett konto har komprometterats.

**Konsekvens: Hög.** Om ett användarkonto komprometteras kan konsekvenserna bli betydande beroende på användarens behörigheter och vilken information kontot kan nå.

Den samlade risken bedöms därför som **medel med osäkerhet**. Riskbedömningen kan ändras om organisationen får ny information om länken, inloggningsuppgifter, användarnas aktiviteter eller loggar.

### CIS 6: Access Control Management

CIS 6 handlar om att kontrollera och begränsa användares behörigheter. I detta case är det relevant eftersom ett användarkonto kan påverkas om en medarbetare har lämnat ut sina inloggningsuppgifter.

Organisationen bör kontrollera vilka behörigheter det berörda användarkontot har och begränsa onödiga behörigheter. På så sätt kan konsekvenserna bli mindre om ett konto skulle komprometteras.

Åtgärden kan verifieras genom att kontrollera användarkontots behörigheter och se vilka system och vilken information kontot kan komma åt.

### CIS 8: Audit Log Management

CIS 8 handlar om att använda och hantera loggar för att upptäcka och undersöka misstänkt aktivitet. I detta case är det relevant eftersom organisationen behöver kontrollera om det har skett misstänkta inloggningar efter att en medarbetare klickade på länken.

Organisationen bör kontrollera relevanta authentication logs och andra säkerhetsloggar för att se om det finns misstänkt aktivitet.

Åtgärden kan verifieras genom att kontrollera loggarna och se om det finns information om till exempel tidpunkt, användare och inloggning. Loggar kan också analyseras med Python för att hitta relevanta händelser.

### CIS 14: Security Awareness and Skills Training

CIS 14 är relevant eftersom caset handlar om ett möjligt phishingförsök. Organisationen bör utbilda medarbetare i att känna igen phishing och andra social engineering-attacker.

Medarbetarna bör få tydliga rutiner för hur de ska kontrollera misstänkta mejl och länkar och hur de ska rapportera dem. Detta kan minska risken att en medarbetare lämnar ut information eller inloggningsuppgifter.

Åtgärden kan verifieras genom att kontrollera att utbildning och rapporteringsrutiner finns och är tillgängliga för medarbetarna.

## 6. Prioriterade åtgärder

### 1. Kontrollera mejlet och länken

Organisationen bör kontrollera avsändaren, mejlets innehåll och länken för att se om länken kommer från en legitim källa. Det bör också kontrolleras om andra medarbetare har klickat på länken.

**Verifiering:** Kontrollera mejlets information, länkens domän och vart länken leder.

### 2. Kontrollera relevanta loggar

Organisationen bör kontrollera relevanta authentication logs och säkerhetsloggar för att se om det finns tecken på misstänkta inloggningar eller annan aktivitet efter att länken klickades.

**Verifiering:** Kontrollera tidpunkt, användare och inloggningar i relevanta loggar.

### 3. Kontrollera och begränsa behörigheter

Organisationen bör kontrollera vilka behörigheter det berörda användarkontot har och ta bort onödiga behörigheter.

**Verifiering:** Kontrollera vilka system och vilken information användarkontot kan komma åt.

## 7. Teknisk koppling

I detta case kan organisationen använda loggning för att undersöka om det har skett misstänkt aktivitet efter att en medarbetare klickade på länken.

Relevanta **authentication logs** kan kontrolleras för att se om det finns misstänkta inloggningar. Till exempel kan organisationen kontrollera tidpunkt, användare och inloggningar.

Detta kopplar till tidigare arbete med **Python och logganalys**. Python kan användas för att läsa och analysera loggar och hitta relevanta händelser.

Loggar kan ge information om misstänkt aktivitet, men de visar inte alltid exakt vad användaren gjorde på phishing-sidan.

## 9. AI- och källredovisning

### AI-användning och egen kontroll

Jag har använt AI som stöd i min analys, men jag har inte bett AI att göra analysen åt mig. Jag bad istället AI att ställa frågor från lärarens perspektiv, så att jag själv kunde svara och förklara mina bedömningar.

AI frågade till exempel vilken risknivå jag tyckte att olika situationer hade. Vid en fråga bedömde jag först risken som hög. Genom följdfrågor fick jag tänka mer på vilka fakta som faktiskt var bekräftade och vilken information som saknades. Jag ändrade därför min bedömning.

Det hjälpte mig att förstå att en möjlig säkerhetshändelse inte automatiskt betyder att risken är hög. Riskbedömningen behöver baseras på fakta, sannolikhet, konsekvens och osäkerheter.

Jag har själv kontrollerat och ändrat AI:s förslag när de inte passade med fakta i caset. Information om CIS Controls har också kontrollerats mot CIS:s officiella information.

Jag har också använt AI för att kontrollera och korrigera min svenska, men jag har själv kontrollerat att innehållet och bedömningarna stämmer med casets fakta.

### Källor

CIS Controls v8.1 används som källa för namn och beskrivning av CIS 6, CIS 8 och CIS 14. Andra bedömningar i rapporten bygger på fakta som anges i caset och på tidigare kursmoment.

## 10. Slutsats

Det finns tecken på ett möjligt phishingförsök, men det är inte bekräftat att någon har lämnat ut sina inloggningsuppgifter eller att ett konto har blivit komprometterat.

Organisationen bör därför först kontrollera mejlet och länken och sedan kontrollera relevanta loggar för att upptäcka eventuell misstänkt aktivitet. Organisationen bör också kontrollera användarnas behörigheter för att begränsa möjliga konsekvenser om ett konto skulle bli komprometterat.

Analysen visar också att CIS 14, CIS 6 och CIS 8 kan kopplas till caset genom utbildning, behörighetskontroll och loggning.
