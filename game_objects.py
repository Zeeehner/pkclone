class Entity:
    def __init__(self, id, name, description, lat, lon):
        self.id = id
        self.name = name
        self.description = description
        self.lat = lat
        self.lon = lon

class Player(Entity):
    def __init__(self, id, name, description, lat, lon):
        super().__init__(id, name, description, lat, lon)
        self.health = 100
        self.attack_dmg = 10
        self.exp = 0
        self.gold = 0
        self.level = 1
        self.inventory = []

    def attack(self, target):
        target.health -= self.attack_dmg
        return target.health <= 0

    def add_exp(self, amount):
        self.exp += amount
        if self.exp >= 100:
            self.level += 1
            self.exp = 0

class Monster(Entity):
    def __init__(self, id, name, description, lat, lon, health, attack_dmg):
        super().__init__(id, name, description, lat, lon)
        self.health = health
        self.attack_dmg = attack_dmg

class Tree(Entity):
    def __init__(self, id, name, description, lat, lon, has_berries=False):
        super().__init__(id, name, description, lat, lon)
        self.has_berries = has_berries
