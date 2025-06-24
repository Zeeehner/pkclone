from pydantic import BaseModel
from typing import Optional
from app.models import Player  # Assuming Player is defined in app.models

class PlayerOut(BaseModel):
    id: str
    user_id: str 
    avatar: int
    gold: int
    lat: float
    lon: float
    centre_lat: float
    centre_lon: float
    hp: int
    status: Optional[str]
    bio: Optional[str]

    class Config:
        orm_mode = True


class PlayerCreate(BaseModel):
    name: str
    avatar: int = 0
    gold: int = 100
    lat: float
    lon: float
    hp: int = 100
