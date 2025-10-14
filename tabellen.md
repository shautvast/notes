Ik ben niet de eerste die dit zegt, maar het is nog geen gemeengoed.
Als je een tabel definieert, neem dan altijd de volgende kolommen op (in volgorde van urgentie):
1. created_at timestamp
2. created_by varchar
3. deleted_at timestamp null
4. deleted_by varchar null
5. updated_at timestamp null
6. updated_by varchar null

#3 en #4  zijn niet alleen _nullable_, maar ook _optional_. Dat wil zeggen, je kunt het record ook fysiek verwijderen. Maar mijn advies zou zijn: 
1. maak een functionele delete logisch (deleted_at/by vullen als een gebruiker iets verwijdert (een functioneel event))
2. maak een fysieke delete na bijvoorbeeld 2 jaar. Om aan juridische eisen te voldoen, of om verloren diskspace terug te krijgen. Of om zeker te weten dat de data niet gestolen kan worden. Of om tegen wie dan ook (toezichthouders, de politie) vol te kunnen houden dat je de data niet hebt.

Geloof me, op een dag zul je er voordeel van hebben.

PS.
#5 zou je zelfs nog kunnen gebruiken als _optimistic locking number_ hoewel een incrementele _integer_ waarde minstens net zo goed is. De overeenkomst is dat beide altijd oplopen. Bij een tijdgebaseerde waarde komen er allerlei vragen bij, zoals wat de precisie is, hoeveel nodes je hebt en of alle klokken gesynchroniseerd zijn.

PS2. Bij de (gerenommeerde) bank waar ik ooit werkte was het 'toezichthouder'-argument één van de redenen voor een fysieke delete.