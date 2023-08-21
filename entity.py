from settings import *
import pygame as pg
from random import randint
from resource_data import ResourceData
# TODO Add searching/discovering/remembering of the resources that has stepped over. 
# TODO Add rutine priorities.
# TODO Add interaction. Entity -> Tile -> GetResources() -> HarvestResources().
# TODO Think if give all the entities access/store all tiles or just get one by functions...
class Entity:
    def __init__(self, screen, tile_manager):
        self.screen = screen
        self.tile_manager = tile_manager
        self.color = (200, 0, 0)
        self.position = pg.Vector2(randint(0, WIDTH), randint(0, HEIGHT))
        self.size = ENTITY_SIZE
        self.rect = pg.Rect(self.position.x, self.position.y, self.size, self.size)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.cooldown_counter = 0
        self.MAX_COOLDOWN = 100 # Miliseconds
        self.can_move = True 
        self.move_target = None
        self.kingdom = None
        self.activity_fullfilled = False
        self.rutines = ["wonder"]
        self.rutine_performed = None
        self.reached = False
        self.idle = True
        self.resource_data = ResourceData()
        self.resource_data.get_supply('wood', 100)

    def get_tile_data(self):
        tile_x , tile_y = self.position.x // TILE_SIZE, self.position.y // TILE_SIZE
        tile_x_index = str(int(tile_x)) 
        tile_y_index = str(int(tile_y))
        if int(tile_y_index) < 10:
            tile_y_index = "0" + tile_y_index

        # index = str(int(tile_y_index)) + str(int(tile_x_index))
        index = (tile_x_index) + (tile_y_index)
        
        tile = self.tile_manager.get_tile(index)
        tile.color = (150, 150, 0)
        # pg.draw.circle(self.screen, (0, 0, 255), (tile.position.x, tile.position.y), 5)
        print(f'[ENT] -> Tile index -> {index} -> tile {self.tile_manager.get_tile(index)}, raw -> {tile_x_index} {tile_y_index}')


    
    def behavior(self):
        if self.kingdom and self.position.distance_to(self.kingdom.position) < 20:
            self.resource_data.dump_inventory_to_target(self.kingdom)
            # self.resource_data.supply(self.kingdom, "wood", 1)
        current_rutine = self.rutines[0]
        self.rutine_performed = current_rutine

        if self.rutine_performed == "wonder" and self.idle == True and not self.move_target:
            self.move_target = pg.Vector2(randint(0, WIDTH), randint(0, HEIGHT)) 
            self.idle = False

        elif self.rutine_performed == "go_home" and self.idle == True and not self.move_target and self.kingdom:
            self.return_home()
            self.idle = False

    def set_kingdom(self, kingdom):
        self.kingdom = kingdom

    def draw(self):
    # pg.draw.rect(self.screen, self.color, self.rect)
        pg.draw.circle(self.screen, self.color, self.position, self.size)

    def update(self):
        self.timer_logic()
        self.behavior()
        self.move()
        self.get_tile_data()

    def timer_logic(self):
        self.delta_time = self.clock.tick(FPS)
        self.cooldown_counter += 1
        if self.cooldown_counter >= self.MAX_COOLDOWN:
            self.on_cooldown()
            print("[ENT.CLOCK] -> Cooldown reached.")
            self.cooldown_counter = 0

    def on_cooldown(self):
        self.can_move = True
        # Actions to do when the cooldown is over.

    def on_target_reached(self):
        if self.position == self.move_target:
            # Changing fullfiled routine to the back of the stack.
            self.rutines.append(self.rutines.pop(0))
            print(f'[ENT] -> Routine: {self.rutines}')
            print("[ENT] -> Target reached.")
            self.idle = True
            self.reached = True
            self.move_target = None

    def return_home(self):
        if self.kingdom:
            self.move_target = self.kingdom.position


    def move(self):
        self.on_target_reached()
        if self.move_target:
            dist_x = self.position.x - self.move_target.x
            dist_y = self.position.y - self.move_target.y
            if dist_x < 0:
                self.position.x += 1
            elif dist_x > 0:
                self.position.x -= 1 
            if dist_y < 0:
                self.position.y += 1  
            elif dist_y > 0:
                self.position.y -= 1
            self.rect.x = int(self.position.x)
            self.rect.y = int(self.position.y)
            return
            
