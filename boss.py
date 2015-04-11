# Class to implement the boss - Donkey Kong
import pygame

class DK:
    def __init__(self):
        self.obj = pygame.Rect((0, 0), (50, 70))
        self.speed = 1
    def move_right(self):
        self.obj = self.obj.move((self.speed, 0))
    def move_left(self):
        self.obj = self.obj.move((-self.speed, 0))
