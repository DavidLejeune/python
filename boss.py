# Class to implement the boss - Donkey Kong
import pygame

class DK:
    def __init__(self, imgs, size):
        self.speed = 1
        self.canvas = size

        # Load spritesheet images into array
        self.image_array = imgs
        self.image_width = 50
        self.image_height = 40

        # Scale images to increase the size
        self.scale_factor = 2
        for i in range(len(self.image_array)):
            self.image_array[i] = pygame.transform.scale(self.image_array[i], (self.image_width*self.scale_factor, self.image_height*self.scale_factor))
        self.current_image = 0

        self.obj = self.image_array[self.current_image]

        #Positions
        self.x = size[0]/2
        self.y = 0

    def move_right(self):
        self.x += 1
    def move_left(self):
        self.x -= 1

    def cycle_image(self):
        if self.current_image+1 < len(self.image_array):
            self.current_image += 1
        else:
            self.current_image = 0
        self.obj = self.image_array[self.current_image]
