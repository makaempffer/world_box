from settings import *
from entity import Entity


class EntityManager:
    def __init__(self, screen, tile_manager):
        self.entities = []
        self.screen = screen
        self.tile_manager = tile_manager
        self.setup_default_entities(1)
    
    def get_entities(self) -> list:
        return self.entities


    def setup_default_entities(self, amount: int):
        for _i in range(amount):
            self.entities.append(Entity(screen = self.screen, tile_manager=self.tile_manager))

    def draw(self):
        for entity in self.entities:
            entity.draw()

    def update(self):
        for entity in self.entities:
            entity.update()
