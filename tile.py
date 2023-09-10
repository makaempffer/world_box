import pygame as pg
from random import randint
from settings import *
from resource_data import ResourceData


class Tile(pg.sprite.Sprite):
    def __init__(self, screen: pg.Surface, x, y):
        super().__init__()
        self.screen = screen
        self.position = pg.Vector2(x, y)
        self.size = TILE_SIZE
        self.rect = pg.Rect(self.position.x, self.position.y, self.size, self.size)
        self.image = pg.image.load("./assets/grass.png")
        self.color = (0, 150, 0)
        self.border_color = (200, 200, 200)
        self.resource_data = None
        self.is_conquered = False
        self.conqueror = None
        self.setup()

    def set_conquered(self, kingdom):
        if self.is_conquered == False and self.conqueror == None:
            self.is_conquered = True
            self.conqueror = kingdom
            self.color = kingdom.color

    def setup(self):
        if randint(0, 1000) > 990:
            self.resource_data = ResourceData()
            self.resource_data.get_supply("wood", 1000)

    def update(self):
        self.get_tile_type()

    def get_tile_type(self):
        if self.is_conquered:
            self.image = pg.image.load("./assets/brick_floor.png")
            return
        if self.resource_data:
            if self.resource_data.data.get("wood"):
                self.image = pg.image.load("./assets/wood.png")
            else:
                self.image = pg.image.load("./assets/grass.png")

    def has_resource(self):
        return self.resource_data

