**Gedetailleerde Todo Lijst**

**Fase 0: Setup & Basis (Samen of één persoon start, ander reviewt)**

- [x] **GitHub Repository:** Maak een GitHub project aan, voeg teamlid en docent (Krul-HR) toe.
- [x] **Django Project Setup:** Initialiseer een nieuw Django project en een app (bijv. `boekenclub`).
- [x] **Basis Configuratie:** Configureer `settings.py` (database, static files, etc.).
- [x] **Modellen Definiëren:** Definieer samen de basisstructuur van de modellen (`Book`, `Read`, `Profile`) in `models.py`.
    - `Book`: `title`, `author`, `genre`, `numberOfPages`, `approved` (Boolean), `approvedBy` (FK naar User, nullable/blankable).
    - `Read`: `book` (FK naar Book), `user` (FK naar User), `date` (DateField), `score` (IntegerField, bijv. met choices 1-5).
    - `Profile`: `user` (OneToOneField naar User), `bioText`, `city`, `dateOfBirth`.
- [x] **Database Migraties:** Maak en voer de initiële database migraties uit (`makemigrations`, `migrate`).
- [x] **Superuser:** Maak een superuser aan (`createsuperuser`) voor toegang tot de admin interface.
- [x] **Basis Templates:** Zet een basis template structuur op (`base.html`) met navigatie.
- [x] **Namen op Loginpagina:** Voeg de namen van het tweetal toe aan de (nog te maken) loginpagina.

**Fase 1: Gebruikers & Profielen (Persoon A)**

- [x] **Gebruikersregistratie:**
    - [x] Maak een registratieformulier (`UserCreationForm` of custom).
    - [x] Maak een view voor de registratiepagina.
    - [x] Maak een URL-patroon voor de registratiepagina.
    - [x] Zorg dat bij registratie ook automatisch een `Profile` object wordt aangemaakt.
- [x] **Login / Logout:**
    - [x] Gebruik Django's ingebouwde `LoginView` en `LogoutView`.
    - [x] Maak templates voor de loginpagina (vergeet de namen niet!) en eventueel een 'logged out' pagina.
    - [x] Maak URL-patronen voor login/logout.
- [x] **Wachtwoord Wijzigen:**
    - [x] Gebruik Django's ingebouwde `PasswordChangeView`.
    - [x] Maak templates voor het wijzigen en de bevestiging.
    - [x] Maak URL-patronen.
- [x] **Profiel Beheer:**
    - [x] Maak een formulier om `Profile` gegevens te bewerken.
    - [x] Maak een view om het profiel te bekijken en bij te werken (vereist login).
    - [x] Maak een URL-patroon voor de profielpagina.
- [x] **Eigen Profielpagina (Publiek):**
    - [x] Maak een view die het profiel van een specifieke gebruiker toont.
    - [x] Toon profielgegevens en lijst van leesacties van deze gebruiker.
    - [x] Maak een URL-patroon (bijv. `/profiel/<username>/`).

**Fase 2: Boeken & Community/Admin (Persoon B)**

- [ ] **Boek Toevoegen (Gebruiker):**
    - [ ] Maak een formulier voor het toevoegen van een `Book`.
    - [ ] Maak een view die het formulier verwerkt (`approved=False`). (Vereist login).
    - [ ] Maak een URL-patroon.
- [ ] **Admin - Boek Goedkeuren:**
    - [ ] Maak een view/admin interface voor niet-goedgekeurde boeken.
    - [ ] Implementeer logica om boek goed te keuren (`approved=True`, `approvedBy=admin`).
    - [ ] Maak URL-patronen (indien nodig).
- [ ] **Admin - Boek Management:**
    - [ ] Maak views/admin interface voor admins om:
        - [ ] Nieuwe boeken direct toe te voegen (`approved=True`).
        - [ ] Bestaande boeken aan te passen.
        - [ ] Bestaande boeken te verwijderen.
    - [ ] Maak URL-patronen (indien nodig).
- [ ] **Newsfeed:**
    - [ ] Maak een view die alle `Read` objecten ophaalt (gesorteerd op datum).
    - [ ] Maak een template die de leesacties toont.
    - [ ] Maak gebruikersnaam klikbaar naar profielpagina.
    - [ ] Maak boektitel klikbaar naar boek detailpagina.
    - [ ] Maak een URL-patroon.
- [ ] **Boek Detailpagina:**
    - [ ] Maak een view die details van één boek toont.
    - [ ] Toon boekdetails.
    - [ ] Bereken en toon aantal keer gelezen.
    - [ ] Bereken en toon gemiddelde score.
    - [ ] Voeg knop/link "Leesactie toevoegen" toe.
    - [ ] Maak een URL-patroon (bijv. `/boek/<int:pk>/`).
- [ ] **Admin - Leesacties Verwijderen:**
    - [ ] Maak een view/admin interface waar admin leesacties kan verwijderen.
    - [ ] Implementeer de logica voor het verwijderen.
    - [ ] Maak URL-patronen (indien nodig).

**Fase 3: Leesacties & Afronding (Persoon A & B - Afstemming nodig)**

- [ ] **Leesactie Toevoegen (Persoon A):**
    - [ ] Maak een formulier voor `Read` actie (alleen goedgekeurde boeken).
    - [ ] Maak een view die het formulier verwerkt (`user` = ingelogde gebruiker).
    - [ ] Implementeer check: niet zelfde boek op zelfde dag.
    - [ ] Maak een URL-patroon.
    - [ ] **Afstemming (Persoon B):** Zorg dat link vanaf Boek Detailpagina werkt en boek vooraf invult.
- [ ] **Eigen Leesacties Beheren (Persoon A):**
    - [ ] Maak een view die lijst van eigen `Read` objecten toont.
    - [ ] Voeg functionaliteit toe om eigen leesactie aan te passen.
    - [ ] Voeg functionaliteit toe om eigen leesactie te verwijderen.
    - [ ] Maak URL-patronen.
- [ ] **Integratie & Testen (Samen):**
    - [ ] Loop alle requirements na.
    - [ ] Test links tussen pagina's.
    - [ ] Test admin-goedkeuring.
    - [ ] Test filtering goedgekeurde boeken.
    - [ ] Test "niet zelfde boek op zelfde dag" check.
    - [ ] Test alle admin-functionaliteiten.
- [ ] **Styling & Afronding (Samen):**
    - [ ] Zorg voor consistente basis-uitstraling.
    - [ ] Code opschonen, comments toevoegen.
    - [ ] Laatste check op requirements.