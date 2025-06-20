# PKClone – Parallel Kingdom Klon

Ein minimalistisches Multiplayer-RPG basierend auf OpenStreetMap und FastAPI.

## Features

- 🗺️ Karte mit Leaflet und Echtzeit-Objekten
- 🧙 Spieler mit EXP, Angriff & Levelsystem
- 🐺 Monster bekämpfen
- 🌳 Bäume mit Beeren sammeln
- 🔌 REST-API (FastAPI)

## Projektstruktur

```
.
├── main.py              # FastAPI Backend
├── game_objects.py      # Entity-, Player-, Monster-, Tree-Klassen
├── static/
│   └── game.html        # Leaflet-Karte mit JS-Interaktion
```

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
uvicorn main:app --reload
```

Öffne dann im Browser: `http://localhost:8000`

## Lizenz

MIT License – feel free to build your own Kingdom.
