import pygame as pg
from random import randint
from settings import *
from resource_data import ResourceData


class Tile:
    def __init__(self, screen: pg.Surface, x, y):
        self.screen = screen
        self.position = pg.Vector2(x, y)
        self.size = TILE_SIZE
        self.rect = pg.Rect(self.position.x, self.position.y, self.size, self.size)
        self.color = (0, 150, 0)
        self.border_color = (200, 200, 200)
        self.resource_data = None
        self.setup()

    def setup(self):
        if randint(0, 100) > 99:
            self.resource_data = ResourceData()
            self.resource_data.get_supply("wood", 1000)

    def update(self):
        self.get_color()

    def has_resource(self):
        return self.resource_data

    def get_color(self):
        if self.resource_data:
            for item in self.resource_data.data:
                if item == "wood" and self.resource_data.get_quantity(item) >= 1:
                    self.color = (111, 78, 55)
                else:
                    self.color = (0, 150, 0)


    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect)

    def draw_border(self):
        #LEFT
        pg.draw.line(self.screen, self.border_color, self.position, (self.position.x, self.position.y + TILE_SIZE))
        #TOP
        pg.draw.line(self.screen, self.border_color, self.position, (self.position.x + TILE_SIZE, self.position.y))
