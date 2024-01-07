---
created: 2024-01-07T15:07:38+01:00
modified: 2024-01-07T15:35:24+01:00
---

# hoofdstuk 1 conway

Hoofdstuk 1, conway's law. 
>> org charts geven de werkelijke organiisatie structuur niet goed weer
Idee: je zou de werkelijke org struct kunnen reproduceren door de meta data van communicatie tools te analyseren (slack, teams, email)

-> heeft nog niemand dat gedaan??


monolieth/wehkamp
Bij wehkamp riepen sommige mensen dat de grote monolitische applicatie opgebroken moest worden in microservices. 
Maar waarom?
De applicatie werd onderhouden door 1 team. Is dat niet de belangrijkste aanwijzing?
Misschien moet ik erbij vermelden dat de cognitive load hoog was. Sommige delen van de complexe code werden maar door 1 persoon begrepen. Aan de andere kant was het wel 'duurzaam' waarmee ik bedoel dat het werk niet teveel was voor het team.
En stel dat je de applicatie openbreekt en zeg in 2 delen splitst. (in casu klant en order). Wat schiet je daarmee op als je niet bijbehorende teams creeert? Maar het geheel werd onderhouden door een man (soms ook vrouw) of 5. Een samenstelling met teams van 2/3 maakt je niet erg flexibel. Waar je uiteindelijk belandt is in een situatie dat je nominaal misschien 2 teams hebt, die in de praktijk maar 1 team zijn, omdat er zoveel interteam communicatie is.


>>'if you have four groups working on a compiler, you'll get a 4-pass compiler' (Eric Raymond)
Hoewel dit niet een helemaal serieus argument is, vraag ik me hierbij toch af hoe tautologisch Conway's law is. Iemand moet toch hebben bedacht dat het zinvol is om 4 teams samen te stellen. En heeft die dan niet gelijk al een intuitie dat een 4-pass compiler een goede implementatie is? Beter gezegd een compiler met 4 kern-functionaliteiten?
Is er dan  niet ook ergens in een vroege fase van het project een plaatje gemaakt met dit design?
Hoogstens zou je kunnen zeggen dat een 4-pass compiler extra lastig wordt met 5 teams. En dat er dus alignment nodig is tussen team indeling en architectuur. 
Die 'vier teams' is niet zomaar uit de lucht komen vallen, omdat we zeg 20 man beschikbaar hadden, die we op wilden delen. 

De 'reverse Conway move' kan ik begrijpen. Dit is het aanpassen van de team samenstelling aan de doelarchitectuur. Want waarom zou je een suboptimale architectuur in het leven roepen, alleen omdat je teams hebt die op een bepaalde manier zijn georganiseerd?
Ì
