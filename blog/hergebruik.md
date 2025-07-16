Een aspect waar ik  nooit iemand over hoor als het gaat over code dupliceren, versus hergebruiken (abstraheren etc) is dit: je hebt code en je hebt ... tja, code. 

Je hebt technische code, die een file leest, of queries uitvoert, of een moeilijk algoritme uitvoert zoals een _dual pivot quicksort_.

En je hebt code die een lijstje gegevens uit de database haalt en kijkt of daar een bepaalde waarde in voorkomt. Of zoiets. De 'domme' code die bovenop de lowlevel technische lagen komt. Kan ook heel complex zijn door de combinaties van regels. Het is ook het deel van de applicatie dat min of meer rechtreeks voortkomt uit de wensen van die ene gebruiker drie jaar geleden. En omdat een andere gebruiker dit jaar een net andere wens heeft voor dat lijstje, kopieren de de oude code, passen iets aan en voila, het werkt.

Een sorteer algoritme is bijna wiskunde. Quicksort is quicksort, onafhankelijk van de wetten van het universum, of van gebruikerswensen. De komende honderd jaar komen er misschien sorteer algoritmes bij, maar dat maakt de oude niet minder goed.

Gebruikers daarentegen zijn grillige wezens. Misschien willen ze wel elke maand iets anders, als je ze de kans geeft. Dit deel van de code is veranderlijk, komt heel vaak in verschillende variaties voor. Omdat het moeilijk is om het gemeenschappelijke erin zo te maken dat het maar één keer in de code hoeft te staan.

**Moet je überhaupt hergebruiken?**
Neem dat ene geval waarbij je data wil tonen in een tabel op het scherm. De query om de data op te halen wordt nog een paar keer aangeroepen om dropdowns voor filters te kunnen vullen. De rijen op het scherm zijn gesorteerd. Ja het hoeft niet voor de dropdown, maar het werkt toch prima? Totdat het onmogelijk lang duurt. 

Of je stopt het in een aparte library zodat je buurteam het ook kan gebruiken. Iedere nieuwe developer neemt aan dat het de ultieme waarheid is, tot iemand ze vertelt dat zelf aan kunnen passen. Ja je moet wel een aparte pipeline draaien en dan de dependency versie updaten. Je bent zo een paar uur verder, met je toevoeging aan een _Enum_. En maar hopen dat het geen code breekt van andere teams.

Zodra je de ultieme waarheid hebt ontdekt is het overigens prima om dat in code uit te hakken. Quicksort bijvoorbeeld. Dat wiel vind je liever niet opnieuw uit.

**Leftpad**
We zijn doorgeschoten in het importeren van standaard functies, die we ook zelf hadden kunnen schrijven. Leftpad in de javascript wereld. Maar voor java: guava, commons-text, commons-io. Ik noem maar een paar. Mijn favoriete hobby is het vervangen van guava *List* factories door standaard java functies. Ja het werkt. Totdat er een *vulnerability* in zit. Of de developer zijn toetsenbord aan de wilgen hangt. String.isEmpty? Heb je dat echt nodig?

**Logging**
Mijn grootste

**hoe vaak verandert het?** 
en hoe groot is de moeite om de abstractie te ontleden om dat ene afwijkende geval in te bouwen