import pgzrun
import random
from pgzhelper import *

class Dino:
    def __init__(self):
        self.x = 100
        self.y = 470
        self.velocity_y = 0
        self.gravity = 1
        self.images = ['run1', 'run2', 'run3', 'run4', 'run5', 'run6', 'run7', 'run8']
        self.image_index = 0
        self.actor = Actor(self.images[self.image_index], (self.x, self.y))
        self.on_ground = True

    def update(self):
        # Yerçekimi uygula
        self.velocity_y += self.gravity
        self.y += self.velocity_y

        # Zıplama
        if keyboard.up and self.on_ground:
            self.velocity_y = -18
            self.on_ground = False

        # Yere düşmeyi kontrol et
        if self.y > 470:
            self.y = 470
            self.velocity_y = 0
            self.on_ground = True

        # Animasyonu güncelle
        self.image_index = (self.image_index + 1) % len(self.images)
        self.actor.image = self.images[self.image_index]
        self.actor.pos = (self.x, self.y)

    def draw(self):
        self.actor.draw()
