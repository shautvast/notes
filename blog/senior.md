---

layout: post

title: "Wat is het verschil tussen een junior en een senior developer?"

author: sander.hautvast

categories: [java, jdk-22]

image: assets/images/classfile/writer.jpg

beforetoc: "seeds"

featured: true

hidden: false

lang: nl

---

Performance probleem in een middelgrote (java) applicatie: in de frontend kun je voor het overzichtscherm filteren op diverse kolommen in de database. Die waardes worden dynamisch bepaald (zonder caching) en komen dan in drop-downs terecht.

  

Na een paar jaar in productie performt dit niet meer zo goed. Er komt een story voor op de backlog en de junior in het team pakt het op. Ik was even met hem gaan zitten om de aanpak door te spreken. Die leek me prima: log statements inbouwen en op de testomgeving kijken waar de meeste tijd in gaat zitten. _Keep it simple_

  

Elke dag in de standup geeft hij een update en er lijkt genoeg voortgang in te zitten. Toch duurt het nu al zeker een sprint. Niet zo'n probleem, want dat heb ik zelf ook vaak bij deze opdrachtgever....

  

Het feit dat hij in de standup meldt dat de sortering (in java) de meeste tijd kost en dat hij die naar de database wil verplaatsen met een _order-by_ doet geen alarmbellen afgaan. Integendeel: de database kan dat vaak sneller. Bovendien is iedereen druk met andere zaken. Op het moment dat we met een mede-senior toch eens dieper op de story ingaan, zien we dat hij erg veel code heeft gewijzigd in zijn branch. Allebei kennen we dit deel van de applicatie niet zo goed. De _refactoring_ lijkt daarom best riskant.

  

Maar eh, waarom sorteren we eigenlijk? We willen een lijstje unieke waardes. Moeten we daar x-duizend records voor sorteren??

Ah, _hergebruik_... De code die de filterwaardes bepaalt (dynamisch opgebouwde query) doet ook de uiteindelijke selectie voor de records op het overzichtsscherm. Voor dat laatste is sortering zinvol. Maar voor de filterwaardes hoeft dat helemaal niet!

  

Kortom: als we de bewuste methode dupliceren en bij één ervan de sortering weglaten, zijn we er ook.

  

En ja, ik heb liever leesbare code, die er twee keer staat, dan iets abstracts, waar je eerst een half uur moet studeren voor het begint in te dalen wat er precies gebeurt.

  

En dan: waarom voeren we de query vijf keer uit? O, omdat er vijf kolommen zijn op te filteren. Kan dat niet in één keer? O, en wat is dat, Spring BeanUtils? Het R-woord: _Reflectie_ De oorspronkelijke developer, nu niet meer in het team, heeft zich uitgeleefd om alles lekker abstract en dynamisch te maken, zonder zich zorgen te maken over toekomstige ontwikkelingen, zoals junior developers of meer data in de database.

  

Dus drie mogelijke performance verbeteringen en de nodige kansen om de code simpeler te maken. Klinkt als een plan. En niet alles in één keer uitvoeren. Eerst maar eens kijken of een enkele optimalisatie genoeg is. (Is er ook een test die dit afdekt?)

  

Kortom, twee weken weggegooid werk? Ja, een senior had dit waarschijnlijk beter gedaan. Maar hoe word je senior, behalve door stug door te gaan met ouder worden? We zelf toch ook vaak genoeg op de bek gegaan. En hoe leer je code kennen? Door eens wat te refactoren. Misschien niet committen.

