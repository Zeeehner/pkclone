from sqlalchemy import (Column, Integer, Float, String, ForeignKey, DateTime, LargeBinary)
from sqlalchemy.orm import declarative_base, relationship
import uuid
import datetime
import math
import random
import time

Base = declarative_base()

# Basemodels
class BaseModel(Base):
    __abstract__ = True
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)


class ItemModel(BaseModel):
    __abstract__ = True
    tag = Column(Integer)
    quantity = Column(Integer)
    meta_data = Column(LargeBinary)


class LivingEntity(BaseModel):
    __abstract__ = True
    lat = Column(Float)
    lon = Column(Float)
    hp = Column(Integer)


# Entities
class Player(LivingEntity):
    __tablename__ = "players"

    user_id = Column(String, nullable=True)  # Replace with ForeignKey to your user table
    city_id = Column(String, ForeignKey("cities.id"), nullable=True)
    clan_id = Column(String, ForeignKey("clans.id"), nullable=True)

    avatar = Column(Integer)
    gold = Column(Integer)

    centre_lat = Column(Float)
    centre_lon = Column(Float)

    status = Column(String(64))
    bio = Column(String(256))

    city = relationship("City", back_populates="members", foreign_keys=[city_id])
    clan = relationship("Clan", back_populates="members", foreign_keys=[clan_id])
    clan = relationship("Clan", back_populates="members", foreign_keys=[clan_id])



class Mob(LivingEntity):
    __tablename__ = "mobs"
    tag = Column(Integer)


# Structures
class Structure(BaseModel):
    __tablename__ = "structures"
    tag = Column(Integer)
    hp = Column(Integer)
    meta_data = Column(LargeBinary)
    lat = Column(Float)
    lon = Column(Float)


class NatureStructure(Structure):
    __tablename__ = "nature_structures"
    id = Column(String, ForeignKey("structures.id"), primary_key=True)
    last_harvest = Column(DateTime)


class PlayerStructure(Structure):
    __tablename__ = "player_structures"
    id = Column(String, ForeignKey("structures.id"), primary_key=True)
    creator_id = Column(String, ForeignKey("players.id"))
    creator = relationship("Player")


class Flag(PlayerStructure):
    __tablename__ = "flags"
    id = Column(String, ForeignKey("player_structures.id"), primary_key=True)
    level = Column(Integer)
    availability = Column(Integer)
    fee = Column(Integer)


class City(PlayerStructure):
    __tablename__ = "cities"
    id = Column(String, ForeignKey("player_structures.id"), primary_key=True)
    major_id = Column(String, ForeignKey("players.id"))
    name = Column(String(32))

    major = relationship("Player", foreign_keys=[major_id], backref="lead_cities")
    members = relationship("Player", back_populates="city",  foreign_keys="[Player.city_id]")


class TradePost(PlayerStructure):
    __tablename__ = "tradeposts"
    id = Column(String, ForeignKey("player_structures.id"), primary_key=True)
    corresponding_city_id = Column(String, ForeignKey("cities.id"))
    corresponding_city = relationship("City", backref="city2")


class CityFlag(Structure):
    __tablename__ = "city_flags"
    id = Column(String, ForeignKey("structures.id"), primary_key=True)
    city_id = Column(String, ForeignKey("cities.id"))
    level = Column(Integer)


class Library(PlayerStructure):
    __tablename__ = "libraries"
    id = Column(String, ForeignKey("player_structures.id"), primary_key=True)
    fee = Column(Integer)
    skill = Column(Integer)
    level = Column(Integer)


# Relationen
class FlagPass(BaseModel):
    __tablename__ = "flag_passes"
    builder_id = Column(String, ForeignKey("players.id"))
    license_id = Column(String, ForeignKey("players.id"))


class Clan(BaseModel):
    __tablename__ = "clans"
    leader_id = Column(String, ForeignKey("players.id"))
    name = Column(String(32))
    members = relationship("Player", back_populates="clan", foreign_keys="[Player.clan_id]")



class Skill(BaseModel):
    __tablename__ = "skills"
    player_id = Column(String, ForeignKey("players.id"))
    tag = Column(Integer)
    transient_exp = Column(Integer)
    total_exp = Column(Integer)


class TradePostListing(ItemModel):
    __tablename__ = "tradepost_listings"
    tradepost_id = Column(String, ForeignKey("tradeposts.id"))


class PlayerItem(ItemModel):
    __tablename__ = "player_items"
    player_id = Column(String, ForeignKey("players.id"))


class GroundItem(ItemModel):
    __tablename__ = "ground_items"
    lat = Column(Float)
    lon = Column(Float)
