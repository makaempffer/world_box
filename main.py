import pygame as pg
import sys
from settings import *

from tile_manager import TileManager

class Game:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.is_running = True
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.setup()

    def setup(self):
        self.tile_manager = TileManager(self.screen)

    def update(self):
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(str(self.clock.get_fps()))
        pg.display.flip()      

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.tile_manager.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()



    def run(self):
        while self.is_running:
            self.check_events()
            self.update()
            self.draw()



game = Game()
game.run()

