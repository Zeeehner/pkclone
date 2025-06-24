from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Player, Mob, Flag, City, Structure, GroundItem
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

# Beispiel-Schema
class PlayerCreate(BaseModel):
    name: str
    avatar: int = 0
    gold: int = 100
    lat: float
    lon: float
    hp: int = 100

@router.post("/players", response_model=dict)
def create_player(player: PlayerCreate, db: Session = Depends(get_db)):
    db_player = Player(
        avatar=player.avatar,
        gold=player.gold,
        lat=player.lat,
        lon=player.lon,
        centre_lat=player.lat,
        centre_lon=player.lon,
        hp=player.hp,
        bio="",
        status=""
    )
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return {"id": db_player.id}

@router.get("/players", response_model=List[dict])
def list_players(db: Session = Depends(get_db)):
    return db.query(Player).all()

@router.get("/players/{player_id}")
def get_player(player_id: str, db: Session = Depends(get_db)):
    player = db.query(Player).get(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

# Gleiches Muster für weitere Modelle...

@router.get("/mobs", response_model=List[dict])
def list_mobs(db: Session = Depends(get_db)):
    return db.query(Mob).all()

@router.get("/flags", response_model=List[dict])
def list_flags(db: Session = Depends(get_db)):
    return db.query(Flag).all()

@router.get("/cities", response_model=List[dict])
def list_cities(db: Session = Depends(get_db)):
    return db.query(City).all()

@router.get("/structures", response_model=List[dict])
def list_structures(db: Session = Depends(get_db)):
    return db.query(Structure).all()

@router.get("/items", response_model=List[dict])
def list_items(db: Session = Depends(get_db)):
    return db.query(GroundItem).all()
