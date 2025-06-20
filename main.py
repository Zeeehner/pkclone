from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from game_objects import Player, Monster, Tree
from math import sqrt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

player = Player("p1", "Held", "Mutiger Krieger", 52.52, 13.405)

objects = [
    Monster("m1", "Wolf", "Boeser Wolf", 52.521, 13.404, 80, 10),
    Tree("t1", "Baum", "Ein Baum mit Beeren", 52.519, 13.406, has_berries=True)
]

@app.get("/")
def root():
    return FileResponse("static/game.html")

@app.get("/player")
def get_player():
    return player.__dict__

@app.get("/objects")
def get_objects():
    return [obj.__dict__ for obj in objects]

@app.post("/attack")
def attack_monster(monster_id: str):
    for obj in objects:
        if isinstance(obj, Monster) and obj.id == monster_id:
            if player.attack(obj):
                objects.remove(obj)
                player.add_exp(50)
                return {"message": f"{obj.name} besiegt!", "exp": player.exp, "level": player.level}
            else:
                return {"message": f"{obj.name} verletzt!", "monster_health": obj.health}
    return {"error": "Monster nicht gefunden"}

@app.post("/gather")
def gather_from_tree(tree_id: str):
    for obj in objects:
        if isinstance(obj, Tree) and obj.id == tree_id:
            if obj.has_berries:
                obj.has_berries = False
                player.inventory.append("berries")
                return {"message": "Beeren gesammelt!", "inventory": player.inventory}
            else:
                return {"message": "Keine Beeren vorhanden."}
    return {"error": "Baum nicht gefunden"}
