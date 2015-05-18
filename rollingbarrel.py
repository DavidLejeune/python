# Rolling barrel class

import pygame

class RollingBarrel:
    def __init__(self, pos, img_arr, size, falling=False):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.img_arr = img_arr
        self.img_counter = 3
        self.speed = 1
        self.platform_level = 4
        self.last_dir = 'r'
        self.max_x = size[1]
        self.min_x = size[0]
        self.falling = falling
    def render(self, surface):
        self.pos = (self.x, self.y)
        surface.blit(self.img_arr[self.img_counter], self.pos)
        return surface
    def get_rect(self):
        return pygame.Rect(self.pos, (self.img_arr[self.img_counter].get_width(), self.img_arr[self.img_counter].get_height()))
    def update(self, platforms, plt_height, ladders):
        if self.falling:
            self.y += self.speed
        else:
            if self.last_dir == 'r':
                if self.x + self.speed < self.max_x:
                    self.x += self.speed
                else:
                    self.last_dir = 'l'
                if self.img_counter + 1 < len(self.img_arr):
                    self.img_counter += 1
                else:
                    self.img_counter = 0
            elif self.last_dir == 'l':
                if self.x - self.speed >= self.min_x:
                    self.x -= self.speed
                else:
                    self.last_dir = 'r'
                if self.img_counter - 1 >= 0:
                    self.img_counter -= 1
                else:
                    self.img_counter = len(self.img_arr)-1
            for p in platforms[self.platform_level+1]:
                if abs(p[0]-self.x) < 10:
                    self.y = p[1]-plt_height+7
            for l in ladders[self.platform_level]:
                if abs(l[0]-self.x) < 15:
                    self.y += 10
                    self.min_x = 0
                    self.platform_level -= 1
                    if self.last_dir == 'r':
                        self.last_dir = 'l'
                    elif self.last_dir == 'l':
                        self.last_dir = 'r'
