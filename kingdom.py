import pygame as pg
from settings import *

class Kingdom:
    def __init__(self, screen, x, y) -> None:
        self.screen = screen
        self.position = pg.Vector2(x, y)
        self.entities = []
        self.size = 100
        self.rect = pg.Rect(self.position.x, self.position.y, self.size, self.size)
        self.color = (0, 0, 100)

    def set_entities(self, array_entities):
        self.entities += array_entities

    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        pass
