import pygame as pg
from settings import *
from entity import Entity


class EntityManager:
    def __init__(self, screen):
        self.entities = []
        self.screen = screen
        self.setup_default_entities(10)


    def setup_default_entities(self, amount: int):
        for _i in range(amount):
            self.entities.append(Entity(screen = self.screen))

    def draw(self):
        for entity in self.entities:
            entity.draw()
