import math
import time
import random
import datetime


class Chunk:
    GRANULARITY = 100
    PERIOD = 15  # seconds

    def __init__(self, parts):
        self.y, self.x = parts
        self.s = self.y / Chunk.GRANULARITY
        self.w = self.x / Chunk.GRANULARITY
        self.n = (self.y + 1) / Chunk.GRANULARITY
        self.e = (self.x + 1) / Chunk.GRANULARITY
        self.key = f"chunk.{self.y}_{self.x}"

    def generate(self, existing_structures, create_structure):
        num = random.randint(4, 16)
        if len(existing_structures) >= num:
            return []

        new_structures = []
        for _ in range(num - len(existing_structures)):
            lat = (random.random() + self.y) / Chunk.GRANULARITY
            lon = (random.random() + self.x) / Chunk.GRANULARITY
            if any(Chunk.distance(lat, lon, s.lat, s.lon) < 200 for s in existing_structures):
                continue
            s = create_structure(lat, lon)
            new_structures.append(s)
        return new_structures

    @staticmethod
    def lower_left_corner(lat, lon):
        lat = max(min(lat, 85), -85)
        lon = (lon + 180) % 360 - 180
        return (math.floor(lat * Chunk.GRANULARITY), math.floor(lon * Chunk.GRANULARITY))

    @staticmethod
    def get(lat, lon):
        return Chunk(Chunk.lower_left_corner(lat, lon))

    @staticmethod
    def distance(lat1, lon1, lat2, lon2):
        R = 6.371e6
        dLat = math.radians(lat2 - lat1)
        dLon = math.radians(lon2 - lon1)
        a = math.sin(dLat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dLon / 2) ** 2
        return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


class EntityMotion:
    def __init__(self, entity_id, lat, lon, lat2, lon2, t1, t2):
        self.entity_id = entity_id
        self.lat, self.lon = lat, lon
        self.lat2, self.lon2 = lat2, lon2
        self.t1, self.t2 = t1, t2

    def recenter(self):
        now = time.time()
        if now < self.t2:
            f = (now - self.t1) / (self.t2 - self.t1)
            self.lat += (self.lat2 - self.lat) * f
            self.lon += (self.lon2 - self.lon) * f
            self.t1 = now
        else:
            self.lat = self.lat2
            self.lon = self.lon2

    def move(self, lat2, lon2):
        self.recenter()
        d = Chunk.distance(self.lat, self.lon, lat2, lon2)
        t = d / (1600.0 / 5)  # speed factor
        self.t1 = time.time()
        self.t2 = self.t1 + t
        self.lat2 = lat2
        self.lon2 = lon2

    def serialize(self):
        return (self.lat, self.lon, self.lat2, self.lon2, self.t1, self.t2)

    @staticmethod
    def deserialize(entity_id, data):
        return EntityMotion(entity_id, *data)

    @staticmethod
    def create(entity_id, lat, lon):
        return EntityMotion(entity_id, 0, 0, lat, lon, 0, 0)
