import pygame as pg
import sys
from settings import *

from tile_manager import TileManager
from entity_manager import EntityManager
from kingdom_manager import KingdomManager
from entity_kingdom_linker import EntityKingdomLinker


class Game:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.is_running = True
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.LAZY_UPDATE_MAX = 100
        self.lazy_update_counter = 0
        self.setup()

    def on_lazy_update(self):
        "Function that get's called every X time."
        print("[MAIN] -> Lazy update.")
        self.tile_manager.update()

    def lazy_counter_logic(self):
        self.lazy_update_counter += 1
        if self.lazy_update_counter >= self.LAZY_UPDATE_MAX:
            self.on_lazy_update()
            self.lazy_update_counter = 0

    def setup(self):
        self.tile_manager = TileManager(self.screen)
        self.entity_manager = EntityManager(self.screen, self.tile_manager)
        self.kingdom_manager = KingdomManager(self.screen, self.tile_manager)
        self.entity_linker = EntityKingdomLinker()
        self.entity_linker.link_all_entities(
            self.entity_manager.get_entities(), self.kingdom_manager.get_kingdoms())

    def update(self):
        self.delta_time = self.clock.tick(FPS)
        self.lazy_counter_logic()
        # COMPONENT UPDATES.
        self.entity_manager.update()
        self.kingdom_manager.update()
        # DRAW UPDATES.
        pg.display.set_caption(str(self.clock.get_fps()))
        pg.display.flip()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.tile_manager.draw()
        self.kingdom_manager.draw()
        self.entity_manager.draw()

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
