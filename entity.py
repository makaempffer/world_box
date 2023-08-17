from settings import *
import pygame as pg
from random import randint

class Entity:
    def __init__(self, screen):
        self.screen = screen
        self.color = (200, 0, 0)
        self.position = pg.Vector2(randint(0, WIDTH), randint(0, HEIGHT))
        self.size = ENTITY_SIZE
        self.rect = pg.Rect(self.position.x, self.position.y, self.size, self.size)

    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect)


