import pygame as pg
import random as rand
from settings import *
from entity import Entity
from resource_data import ResourceData

class Kingdom:
    def __init__(self, screen, x, y, tile_manager = None) -> None:
        self.screen = screen
        self.tile_manager = tile_manager
        self.position = pg.Vector2(x, y)
        self.entities = []
        self.size = 10
        self.rect = pg.Rect(self.position.x, self.position.y, self.size, self.size)
        self.color = (0, 0, 100)
        self.resource_data = ResourceData()
        self.conquered_tiles = []
        self.level = 0
        self.experience = 0
        self.next_level = 100


    def get_tile_by_index(self):
        tile_x , tile_y = (self.position.x) // TILE_SIZE, self.position.y // TILE_SIZE
        tile_x_index = str(int(tile_x)) 
        tile_y_index = str(int(tile_y))
        if int(tile_y_index) < 10:
            tile_y_index = "0" + tile_y_index

        index = (tile_x_index) + (tile_y_index)
        
        return index

    def get_random_neighbor(self, x, y):
        neighbor_left = str(int((x - TILE_SIZE) // TILE_SIZE)) + str(int(y // TILE_SIZE))
        neighbor_right = str(int((x + TILE_SIZE) // TILE_SIZE)) + str(int(y // TILE_SIZE))
        neighbor_top = str(int(x // TILE_SIZE)) + str(int((y - TILE_SIZE) // TILE_SIZE))
        neighbor_bottom = str(int(x // TILE_SIZE)) + str(int((y + TILE_SIZE) // TILE_SIZE))
        choices = [neighbor_left, neighbor_right, neighbor_top, neighbor_bottom]
        choice = rand.choice(choices)
        return choice


    def conquer(self):
        if not self.tile_manager:
            return
        if len(self.conquered_tiles) < 4:
            conquered_tile = self.get_random_neighbor(self.position.x, self.position.y)
        else:
            conquered_tile = rand.choice(self.conquered_tiles)
            conquered_tile = self.get_random_neighbor(conquered_tile.position.x, conquered_tile.position.y)

        print(f"[KGD] -> Tile conquered -> {conquered_tile}")
        tile_object = self.tile_manager.get_tile(conquered_tile)
        tile_object.set_conquered(self)
        self.conquered_tiles.append(tile_object)

        print(self.conquered_tiles)
        

    def level_logic(self):
        if self.experience >= self.next_level:
            self.conquer()
            self.level += 1
            self.experience = 0
            self.next_level *= 1.2
        

    def set_entities(self, array_entities):
        self.entities += array_entities

    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        self.level_logic()

    def get_entities(self) -> list[Entity]:
        return self.entities
    

    
