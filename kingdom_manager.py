from settings import *
from kingdom import Kingdom


class KingdomManager:
    def __init__(self, screen):
        self.screen = screen
        self.kingdoms_data = {}
        self.kingdom_list = []
        self.setup_default()

    def setup_default(self):
        self.add_kingdom(Kingdom(self.screen, 100, 100))

    def add_kingdom(self, kingdom: Kingdom):
        self.kingdoms_data[kingdom] = [kingdom.get_entities()]
        self.kingdom_list.append(kingdom)

    def update(self):
        for kingdom in self.kingdoms_data:
            kingdom.update()

    def draw(self):
        for kingdom in self.kingdoms_data:
            kingdom.draw()
    
    def get_kingdom(self, index: int) -> Kingdom:
        return self.kingdom_list[index]

