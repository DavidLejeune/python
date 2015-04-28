# Mario character class

import pygame

class Mario:
    def __init__(self, pos, img):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.img_arr = img
        self.img_counter = 2
        self.speed = 5
        self.last_dir = 'r'
        self.platform_level = 0
    def render(self, surface):
        self.pos = (self.x, self.y)
        surface.blit(self.img_arr[self.img_counter], self.pos)
        return surface
    def increment(self):
        if self.img_counter + 1 < len(self.img_arr):
            self.img_counter += 1
        else:
            self.img_counter = 0
    def move_left(self):
        self.x -= self.speed
        self.last_dir = 'l'
    def move_right(self):
        self.x += self.speed
        self.last_dir = 'r'
    def update(self, left, right, up, down, platforms, plt_height, ladders):
        if right:
            self.img_counter = 1
            self.move_right()
        if left:
            self.img_counter = 0
            self.move_left()
        if not right and not left:
            if self.last_dir == 'r':
                self.img_counter = 2
            elif self.last_dir == 'l':
                self.img_counter = 3
        for p in platforms[self.platform_level]:
            if abs(p[0]-self.x) < 10:
                self.y = p[1]-plt_height-5
        for l in ladders[self.platform_level]:
            if abs(l[0]-self.x) < 5:
                if up:
                    self.y -= 10
                    self.platform_level += 1
                print self.platform_level
                print "^^"
        if self.platform_level > 0:
            for l in ladders[self.platform_level-1]:
                if abs(l[0]-self.x) < 5 and down:
                    self.y += 10
                    self.platform_level -= 1
