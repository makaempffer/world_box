from settings import *
from random import randint
from kingdom import Kingdom
from entity_kingdom_linker import EntityKingdomLinker


class KingdomManager:
    def __init__(self, screen, tile_manager):
        self.screen = screen
        self.tile_manager = tile_manager
        self.kingdoms_data = {}
        self.kingdom_list = []
        self.linker = EntityKingdomLinker()
        self.create_kingdoms(2)

    def create_kingdoms(self, amount: int):
        for i in range(amount):
            random_x, random_y = randint(0, WIDTH), randint(0, HEIGHT)
            self.add_kingdom(Kingdom(self.screen, x=random_x,
                             y=random_y, tile_manager=self.tile_manager))

    def setup_test_kingdom(self):
        self.add_kingdom(Kingdom(self.screen, 500, 500, self.tile_manager))

    def add_kingdom(self, kingdom: Kingdom):
        self.kingdoms_data[kingdom] = [kingdom.get_entities()]
        self.kingdom_list.append(kingdom)

    def update(self):
        for kingdom in self.kingdoms_data:
            kingdom.update()

    def draw(self):
        for kingdom in self.kingdoms_data:
            kingdom.draw()

    def get_kingdom(self, index: int):
        if len(self.kingdom_list) > 0:
            return self.kingdom_list[index]

    def get_kingdoms(self):
        return self.kingdom_list
