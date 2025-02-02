import pgzrun
import random
from pgzhelper import *

default_enemy_y_range = (100, 300)


class Enemy:
    def __init__(self, image, speed,name):
        self.actor = Actor(
            image, (random.randint(900, 900), random.randint(*default_enemy_y_range))
        )
        self.speed = speed
        self.name= name

    def update(self):
        self.actor.x -= self.speed
        if self.actor.x < -50:
            self.actor.x = random.randint(900, 900)
            self.actor.y = random.randint(*default_enemy_y_range)

    def draw(self):
        self.actor.draw()
