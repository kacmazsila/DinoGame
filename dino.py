import pgzrun
import random
from pgzhelper import *

default_dino_y = 470
dino_images = ['run1', 'run2', 'run3', 'run4', 'run5']

default_gravity = 1

class Dino:
    def __init__(self):
        self.actor = Actor('idle1', (100, default_dino_y))
        self.actor.images = dino_images
        self.actor.fps = 5
        self.velocity = 0
        self.gravity = default_gravity

    def update(self,keyboard):

        if keyboard.up and self.actor.y == default_dino_y:
           self.velocity = -18
        self.actor.y += self.velocity
        self.velocity += self.gravity
        if self.actor.y > default_dino_y:
            self.actor.y = default_dino_y
            self.velocity = 0
        self.actor.next_image()

    def draw(self):
        self.actor.draw()

    def collides_with(self, obj):
        return self.actor.colliderect(obj)

    def collides_list_with(self, obj):
        return self.actor.collidelist(obj)
