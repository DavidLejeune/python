# Mario character class

import pygame

class Mario:
    def __init__(self, pos, img):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.img_arr = img
        self.img_counter = 0
    def render(self, surface):
        self.pos = (self.x, self.y)
        surface.blit(self.img_arr[self.img_counter], self.pos)
        print "RENDER"
        return surface
    def increment(self):
        if self.img_counter + 1 < len(self.img_arr):
            self.img_counter += 1
        else:
            self.img_counter = 0
    def move_left(self):
        self.x -= 10
    def move_right(self):
        self.x += 10
    def update(self, left, right, up, down, platforms, plt_height):
        if right:
            self.move_right()
        if left:
            self.move_left()
        for p in platforms:
            print str(self.y) + "::" + str(p[1]-plt_height)
            if abs(p[0]-self.x) < 10:
                self.y = p[1]-plt_height-20
