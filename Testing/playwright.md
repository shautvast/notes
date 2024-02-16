## Playwright 

Kan ik gewoon zeggen dat ik ontzettend blij ben met playwright?

Ik heb nog nooit zo lekker frontend tests ontwikkeld. Nu ben ik meer een developer dan een tester, en ik heb ze lang niet allemaal uitgebrobeerd. 
De meeste ervaring die ik heb is met robotframework. Dat is in de basis het zelfde, een tool met een prettige taal (python) bovenop selenium. 
Hét grote verschil is niet de taal zelf maar de tooling en de documentatie eromheen. Playwright kun je namelijk (1) headless draaien, handig voor 
in je pipelines, maar (2) ook headed, dan zie je (zoals altijd met dit soort tooling) de browserschermen automatische voorbijschieten, én (3) een _UI_ 
modus. Dit opent een window waarin je individuele tests af kunt trappen, en je ziet als in een video editing tool de individuele frames naast elkaar staan, 
wat je de mogelijkheid geeft heen en weer in de tijd te gaan. En dan krijg je meer dan alleen een screenshot, je krijgt de pagina zelf (!) en daarbinnen
de mogelijkheid _locators_ uit te proberen. 
De workflow is daarmee zó veel lekkerder dan met andere tools. Daar ben je steeds aan het wijzigen, en dan moet je maar hopen dat de volgende testrun slaagt.
Ik voeg in intellij een nieuwe test toe (typescript). Die verschijnt automatisch in de nog draaiende UI en ik trap hem af.
