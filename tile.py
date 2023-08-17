import pygame as pg
from settings import *


class Tile:
    def __init__(self, screen: pg.Surface, x, y):
        self.screen = screen
        self.position = pg.Vector2(x, y)
        self.size = TILE_SIZE
        self.rect = pg.Rect(self.position.x, self.position.y, self.size, self.size)
        self.color = (0, 150, 0)
        self.border_color = (200, 200, 200)

    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect)

    def draw_border(self):
        #LEFT
        pg.draw.line(self.screen, self.border_color, self.position, (self.position.x, self.position.y + TILE_SIZE))
        #TOP
        pg.draw.line(self.screen, self.border_color, self.position, (self.position.x + TILE_SIZE, self.position.y))
