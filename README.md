[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wxDq4rbD)
# Zadaća 2 - REST API aplikacija

## O projektu
Turistička agencija
Aplikacija služi za digitalnu evidenciju turističkih aranžmana i upravljanje rezervacijama klijenata. Sistem omogućava potpunu CRUD funkcionalnost nad podacima o putovanjima i klijentima, pružajući agenciji centralizovan pregled ponude i prodaje.

## Tim

- **Student A**: Edin Hodžić - resurs: `/resursi_a`
- **Student B**: Elma Čandić - resurs: `/resursi_b`

## Instalacija i pokretanje

### Preduvjeti

- Python 3.10 ili noviji
- pip

### Koraci

1. Klonirajte repozitorij:
```bash
git clone <url-repozitorija>
cd <naziv-repozitorija>
```

2. Kreirajte virtuelno okruženje:
```bash
python -m venv venv
```

3. Aktivirajte virtuelno okruženje:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. Instalirajte zavisnosti:
```bash
pip install -r requirements.txt
```

5. Pokrenite aplikaciju:
```bash
uvicorn main:app --reload
```

6. Otvorite browser na adresi: `http://localhost:8000/docs`

## API Endpointi

### Resurs A: `/resursi_a`

| Metoda | Ruta | Opis |
|--------|------|------|
| GET | `/arrangement` | Dohvatanje svih aranzmana ili filtriranje po destinaciji |
| GET | `/arrangement/{id}` | Dohvatanje aranzmana po ID-u |
| POST | `/arrangement` | Kreiranje novog aranzmana |
| PUT | `/arrangement/{id}` | Azuriranje cijelog aranzmana |
| PATCH | `/arrangement/{id}` | Djelimično azuriranje aranzmana |
| DELETE | `/arrangement/{id}` | Brisanje aranzmana po ID-u |

**Primjer zahtjeva:**
```bash
# Kreiranje novog resursa
curl -X POST "http://localhost:8000/resursi_a" \
  -H "Content-Type: application/json" \
  -d '{"polje1": "vrijednost", "polje2": 123}'
```

### Resurs B: `/resursi_b`

[Analogno kao za Resurs A]
## Bookings API Endpoints

| Metoda | Ruta | Opis |
|--------|------|------|
| POST | `/bookings` | Kreiranje rezervacije |
| GET | `/bookings` | Dohvatanje svih rezervacija |
| GET | `/bookings/{id}` | Dohvatanje jedne rezervacije po ID-u |
| PUT | `/bookings/{id}` | Ažuriranje (potpuna zamjena) rezervacije |
| PATCH | `/bookings/{id}` | Djelimično ažuriranje rezervacije |
| DELETE | `/bookings/{id}` | Brisanje rezervacije |

Primjer zahtjeva:
curl -X GET "http://127.0.0.1:8000/bookings"
curl -X PATCH "http://127.0.0.1:8000/bookings/1" \
-H "Content-Type: application/json" \
-d '{
  "status": "confirmed",
  "is_paid": true
}'

## Korištenje AI alata

### Alat: [GitHub Copilot / ChatGPT / ...]
**Model:** [GPT-4, Copilot model, ...]

**Primjer 1:**
- **Prompt:** Napiši mi rutu za GET zahtjev koja omogućava filtriranje rezervacija po destinaciji
- **Kako je pomoglo:** Generisan je kod koji koristi select i .where() uslove, što je omogućilo naprednu pretragu baze umjesto samo listanja svih podataka.
- **Prilagodbe:** Prilagodila sam nazive varijabli da se tačno poklapaju sa mojim modelom i dodala Optional tipove kako filteri ne bi bili obavezni

**Primjer 2:**
- **Prompt:** Objasni mi sta sve trebam imati kada definisem strukturu podataka u models_a.py
- **Kako je pomoglo:** Dobio sam jasniju sliku kako tacno trebam napraviti srukture koje sam napravio u ovom file-u
- **Prilagodbe:** Prilagodjeni nazivi, dodane odredjene stavke (npr. duration_days), a neke izbacene 

## Napomene

Pokretanje se vrsi istim postupkom koji je naveden u prethodnim dijelovima README.md file-a. 
