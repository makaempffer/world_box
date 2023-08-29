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
        self.next_level = 10 


    def get_tile_by_index(self):
        tile_x , tile_y = (self.position.x) // TILE_SIZE, self.position.y // TILE_SIZE
        tile_x_index = str(int(tile_x)) 
        tile_y_index = str(int(tile_y))
        if int(tile_y_index) < 10:
            tile_y_index = "0" + tile_y_index

        index = (tile_x_index) + (tile_y_index)
        
        return index

    def get_random_neighbor(self, position):
        neighbor_left = str(int((position.x - TILE_SIZE) // TILE_SIZE)) + str(int(position.y // TILE_SIZE))
        neighbor_right = str(int((position.x + TILE_SIZE) // TILE_SIZE)) + str(int(position.y // TILE_SIZE))
        neighbor_top = str(int(position.x // TILE_SIZE)) + str(int((position.y - TILE_SIZE) // TILE_SIZE))
        neighbor_bottom = str(int(position.x // TILE_SIZE)) + str(int((position.y + TILE_SIZE) // TILE_SIZE))
        choices = [neighbor_left, neighbor_right, neighbor_top, neighbor_bottom]
        choice = rand.choice(choices)
        return choice


    def check_conquered(self, tile):
        if tile.is_conquered:
            return True
        else:
            return False

    def conquer(self):
        if not self.tile_manager:
            return
        if len(self.conquered_tiles) < 4:
            conquered_tile = self.get_random_neighbor(self.position)
        else:
            conquered_tile = None
            for _i in range(4):
                choice = rand.choice(self.conquered_tiles)
                conquered_tile = self.get_random_neighbor(choice.position)
                print(f"[DEBUG] -> tile -> {conquered_tile}")
                tile_object = self.tile_manager.get_tile(conquered_tile)
                if not self.check_conquered(tile=tile_object):
                    break

        print(f"[KGD] -> Tile conquered -> {conquered_tile}")
        tile_object = self.tile_manager.get_tile(conquered_tile)
        tile_object.set_conquered(self)
        self.conquered_tiles.append(tile_object)
    
    def calculate_level(self):
        total_experience = 0
        for item in self.resource_data.data:
            item_exp = self.resource_data.get_quantity(item)
            if item == "wood":
                item_exp *= 1
            elif item == "stone":
                item_exp *= 1.2
            total_experience += item_exp

        self.experience = total_experience
            


    def level_logic(self):
        self.calculate_level()
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
    

    
