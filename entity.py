from settings import *
import pygame as pg
from random import randint

class Entity:
    def __init__(self, screen):
        self.screen = screen
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

    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        self.timer_logic()
        self.move_random()

    def timer_logic(self):
        self.delta_time = self.clock.tick(FPS)
        self.cooldown_counter += 1
        if self.cooldown_counter >= self.MAX_COOLDOWN:
            self.on_cooldown()
            print("TIME EXCEDED")
            self.cooldown_counter = 0

    def on_cooldown(self):
        self.can_move = True
        # Actions to do when the cooldown is over.

    def on_target_reached(self):
        if self.position == self.move_target:
            print("Destination Reached.")
            self.move_target = None

    def move_random(self):
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
        if self.can_move:
            x, y = randint(0, WIDTH), randint(0, HEIGHT)
            self.move_target = pg.Vector2(x, y)
