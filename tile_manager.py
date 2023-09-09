from tile import *
import pygame as pg
from settings import *

class TileManager:
    def __init__(self, screen):
        self.screen = screen
        self.tiles = []
        self.group = pg.sprite.Group()
        self.setup()

    def create_default_map(self): 
        for x in range(WIDTH//TILE_SIZE):
            for y in range(HEIGHT//TILE_SIZE):
                tile = Tile(self.screen, x*TILE_SIZE, y*TILE_SIZE)
                self.tiles.append(tile)
                self.group.add(tile)

    def draw(self):
        self.group.draw(self.screen)

    def update(self):
        self.group.update()

    def get_tile(self, idx) -> Tile:
        index = int(idx)
        if int(index) <= len(self.tiles):
            return self.tiles[index]
        else:
            return self.tiles[0]


    def setup(self):
        self.create_default_map()
