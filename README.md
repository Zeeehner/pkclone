# PKClone – Parallel Kingdom Clone

A minimalist multiplayer RPG inspired by Parallel Kingdom, built with OpenStreetMap and FastAPI.

## Features

- 🗺️ Live map using Leaflet and real-time object rendering
- 🧙 Player system with XP, attack, and leveling
- 🐺 Combat system for monsters
- 🌳 Resource gathering (trees, berries)
- 🔌 REST API (FastAPI backend)


## Setup

```
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
uvicorn main:app --reload
```

Then open in your browser: `http://localhost:8000`

## Disclaimer & License

This is a fan-made, non-commercial educational project.  
It is **not affiliated with or endorsed by PerBlue**.  
All game concepts, names, and trademarks mentioned belong to their respective owners.

Source code is licensed under the [MIT License](LICENSE).
