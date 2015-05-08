# Class to generate platform objects

import pygame

class Platforms:
    def __init__(self, canvas_size, num_platforms, sprite_obj, start_dir='r'):
        self.platforms = []
        self.smashed = num_platforms-1
        self.alternate_dir = start_dir
        self.obj = sprite_obj
        self.obj = pygame.transform.scale(self.obj, (canvas_size[0]/num_platforms, 30))
        for i in range(num_platforms):
            self.platforms.append(Platform(canvas_size, i+1))
    def smash(self):
        alternate_dir = 'r'
        for p in range(len(self.platforms)):
            self.platforms[p].smash(direction=alternate_dir)
            if alternate_dir == 'r':
                alternate_dir = 'l'
            else:
                alternate_dir = 'r'
    def iSmash(self):
        if self.smashed >= 0:
            self.platforms[self.smashed].smash(direction=self.alternate_dir)
            if self.alternate_dir == 'r':
                self.alternate_dir = 'l'
            else:
                self.alternate_dir = 'r'
            self.smashed -= 1

    def render(self, surf):
        PLATFORM_COLOR = (255, 0, 0)
        for p in self.platforms:
            for r in p.rects:
                ##pygame.draw.rect(surf, PLATFORM_COLOR, r)
                surf.blit(self.obj, (r[0], r[1]))
        return surf


class Platform:
    def __init__(self, canvas_size, level, prev=0):
        width = canvas_size[0]
        spacing = canvas_size[1] / 10
        height = canvas_size[1] / 20
        segments = 12
        self.rects = []
        for i in range(segments):
            # rect = pygame.Rect((width*i/segments, canvas_size[1]-spacing*(level+1)-spacing*(level-1), width/segments, height))
##            rect = pygame.Rect((width*i/segments, canvas_size[1]-spacing*(level)-spacing*(level-1), width/segments, height))
            rect = pygame.Rect((width*i/segments, canvas_size[1]-spacing*level, width/segments, height))
            self.rects.append(rect)
        self.height = height
        self.width = width
        self.segments = segments
    def smash(self, direction='r'):
        if direction == 'r':
            for r in range(self.segments):
                self.rects[r] = self.rects[r].move(0, self.height*r/6)
        else:
            for r in range(self.segments):
                self.rects[r] = self.rects[r].move(0, self.height*(self.segments-r)/6)
