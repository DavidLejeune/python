# Mario character class

import pygame

class Mario:
    def __init__(self, pos, img):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.img_arr = img
        self.img_counter = 2
        self.speed = 4
        self.last_dir = 'r'
        self.platform_level = 0
        self.jumping = False
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
##    def jump(self, platforms, h):
##        h -= 5
##        if self.platform_level+1 < len(platforms):
##            print str(platforms[self.platform_level+1][1][1]), "::", str(self.y)
##            if self.y >= platforms[self.platform_level+1][1][1]+h:
##                self.y -= 3
##            else:
##                self.jumping = False
##        else:
##            print "Last platform"
##            if self.y > 0+h:
##                self.y -= 3
##            else:
##                self.jumping = False
##            print "Done"
    def jump(self, platforms, h):
        self.y -= 3
        
    def update(self, left, right, up, down, jump, platforms, plt_height, ladders, barrels):
        if right:
            self.img_counter = 1
            self.move_right()
        if left:
            self.img_counter = 0
            self.move_left()
        if jump and not self.jumping:
            self.jumping = True
            print "Set to true"
        if self.jumping:
            self.jump(platforms, plt_height)
        if not right and not left:
            if self.last_dir == 'r':
                self.img_counter = 2
            elif self.last_dir == 'l':
                self.img_counter = 3
        if not self.jumping:
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
        mario_rect = pygame.Rect(self.pos, (self.img_arr[self.img_counter].get_width(), self.img_arr[self.img_counter].get_height()))
        for b in barrels:
            if mario_rect.colliderect(b.get_rect()):
                print "collision"
                return False
