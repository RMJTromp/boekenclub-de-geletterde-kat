# boekenclub-de-geletterde-kat
Eindopdracht Boekenclub Keuzevak Django – Hogeschool Rotterdam

# Intro
Deze opdracht dient in een tweetal gemaakt te worden. De beoordeling zal plaatsvinden zoals omschreven in de cursushandleiding. De verwachte duur dat je er per persoon mee bezig bent staat hier ook vermeld. Je hoeft geen logboek bij te houden.<br/>
Vermeld de namen van jullie tweetal op de inlogpagina. 

Maak een Github project voor je opdracht en voeg ook de docent toe hieraan, github naam: Krul-HR. Via de GitHub commits zullen we zien of er door iedereen in het team gelijkwaardig werk is geleverd.

# Opdracht
### Boekenclub De Geletterde Kat
Deze regionale boekenclub wil een eigen website waarop leden kunnen aangeven welke boeken ze hebben gelezen en welke score ze daar aan geven.

- [ ] Een gebruiker kan zich registreren en inloggen. Op zijn profiel wordt zijn woonplaats, geboortedatum en biotekst bijgehouden. De gebruiker kan deze dingen updaten via de website.
- [ ] Een gebruiker kan een nieuwe ‘leesactie’ (welke boek, wanneer en welke score) toevoegen.
- [ ] Een gebruiker kan een nieuwe boek toevoegen. Een boek moet na het toevoegen eerst worden goedgekeurd door een admin voordat het boek op de website te gebruiken is.
- [ ] Een gebruiker kan een ‘newsfeed’ pagina openen, hierop zijn alle leesacties van alle gebruikers zichtbaar, op chronologische volgorde.
- [ ] Een gebruiker kan op een pagina al zijn eigen leesacties inzien, aanpassen en verwijderen.
- [ ] De admin kan ingediende boeken goedkeuren.
- [ ] De admin kan zelf nieuwe boeken toevoegen, die worden dan automatish goedgekeurd.
- [ ] De admin kan bestaande boeken aanpassen en verwijderen.
- [ ] De admin kan leesacties van alle gebruikers verwijderen (niet aanpassen).

### Bijkomende functionaliteiten
- [ ] Een gebruiker kan zijn wachtwoord updaten.
- [ ] Gebruikers hebben een profielpagina, waarop je van de betreffende gebruiker al zijn gelezen boeken kan zien. (Denk aan je profiel op Instagram waar al je berichten op staan). Hier kan je op komen door bijvoorbeeld in de newsfeed op de gebruikersnaam te klikken.
- [ ] Een gebruiker mag niet op één dag meerdere keren hetzelfde boek lezen.
- [ ] Er is een boekenpagina, waarop de details van één boek te vinden zijn. Met ook informatie over hoe vaak het gelezen is en wat de gemiddelde score is. Hier kan je op komen door bijvoorbeeld in de newsfeed op de boekentitel te klikken.
- [ ] Vanaf de boekenpagina kan een gebruiker een nieuwe leesactie aanmaken, dan komt hij op die pagina terecht en is het gekozen boek direct geselecteerd.


# Models
| *Book* |
| ------ |
| Title |
| Author |
| Genre |
| NumberOfPages |
| Approved |
| ApprovedBy (FK) |

| *Read* |
| ------ |
| Book (FK) |
| User (FK) |
| Date |
| Score |

| *Profile* |
| --------- |
| BioText |
| City | 
| DateOfBirth |
