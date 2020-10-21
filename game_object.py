import pygame
from constants import *
from vector import Vector
import random
from pygame.locals import(RLEACCEL)

class GameObject(pygame.sprite.Sprite):
    def __init__(self, sprite_path=""):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(sprite_path).convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.pos = Vector()
        self.pos.random(SCREEN_DIM)
        self.rot = random.random() * math.pi
        self.dir = Vector(math.cos(self.rot), math.sin(self.rot))
        self.speed = 0.0

    def rotate(self, rad=0.0, clockwise=True):
        if rad == 0.0:
            return
        if clockwise:
            self.rot += rad
            new_dir = Vector(math.cos(self.rot), math.sin(self.rot))
        else:
            self.rot -= rad
            new_dir = Vector(math.cos(self.rot), math.sin(self.rot))
        self.dir = Vector(math.cos(self.rot), math.sin(self.rot))

    def move(self, speed=0):
        new_pos = self.pos.add(self.dir.scalar_mult(speed * TIME_DELTA))
        self.pos = new_pos

    def set_dir(self, rad=0.0):
        self.rot = rad
        self.dir = Vector(math.cos(self.rot), math.sin(self.rot))