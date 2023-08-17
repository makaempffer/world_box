import pygame as pg
from settings import *


class Tile:
    def __init__(self, screen: pg.Surface, x, y):
        self.screen = screen
        self.position = pg.Vector2(x, y)
        self.size = TILE_SIZE
        self.rect = pg.Rect(self.position.x, self.position.y, self.size, self.size)
        self.color = (255, 255, 255)

    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect)
        
