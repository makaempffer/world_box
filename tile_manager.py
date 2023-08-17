from tile import *
from settings import *

class TileManager:
    def __init__(self, screen):
        self.screen = screen
        self.tiles = []
        self.setup()

    def create_default_map(self): 
        for x in range(WIDTH//TILE_SIZE):
            for y in range(HEIGHT//TILE_SIZE):
                self.tiles.append(Tile(self.screen, x*TILE_SIZE, y*TILE_SIZE))

    def draw(self):
        for tile in self.tiles:
            tile.draw()
            tile.draw_border()


    def setup(self):
        self.create_default_map()
