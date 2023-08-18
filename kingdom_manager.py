from settings import *
from kingdom import Kingdom


class KingdomManager:
    def __init__(self, screen):
        self.screen = screen
        self.kingdoms = []
        self.setup_default()

    def setup_default(self):
        self.add_kingdom(Kingdom(self.screen, 100, 100))

    def add_kingdom(self, kingdom):
        self.kingdoms.append(kingdom)

    def update(self):
        for kingdom in self.kingdoms:
            kingdom.update()

    def draw(self):
        for kingdom in self.kingdoms:
            kingdom.draw()
