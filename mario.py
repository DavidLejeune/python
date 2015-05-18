# Mario character class

import pygame

class Mario:
    def __init__(self, pos, img, img_hammer):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.img_arr = img
        self.img_hammer_arr = img_hammer
        self.img_set = 0
        self.img_counter = 2
        self.speed = 0.2
        self.last_dir = 'r'
        self.platform_level = 0
        self.jumping = False
        self.jumpY = 0
        self.jump_dir = 0
        self.hammer = False
        self.cushion = 0
        self.hammer_movement = 0
        self.run_pos = 0
    def render(self, surface):
        self.pos = (self.x, self.y-self.cushion)
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
    def jump(self, platforms, h):
        if self.jump_dir == 0:
            self.y -= 0.2
            self.jumpY += 1
            if self.jumpY >= 400:
                self.jump_dir = 1
        elif self.jump_dir == 1:
            self.y += 0.2
            self.jumpY -= 1
            if self.jumpY <= 0:
                self.jump_dir = 0
                self.jumping = False

    def update(self, left, right, up, down, jump, platforms, plt_height, ladders, barrels, items):
        if right:
            if self.run_pos == 0:
                self.img_counter = 1
                self.run_pos += 1
            elif self.run_pos == 1:
                self.img_counter = 5
                self.run_pos = 0
            self.move_right()
        if left:
            if self.run_pos == 0:
                self.img_counter = 0
                self.run_pos += 1
            elif self.run_pos == 1:
                self.img_counter = 4
                self.run_pos = 0
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
        if self.platform_level > 0 and not self.jumping:
            for l in ladders[self.platform_level-1]:
                if abs(l[0]-self.x) < 5 and down:
                    self.y += 10
                    self.platform_level -= 1
        if self.hammer:
            if self.hammer_movement < 50 and self.hammer_movement >= 0:
                print "up"
                if self.last_dir == 'l':
                    self.img_counter = 7
                else:
                    self.img_counter = 10
            elif self.hammer_movement >= 50 and self.hammer_movement < 100:
                print "down"
                if self.last_dir == 'l':
                    self.img_counter = 6
                else:
                    self.img_counter = 11
            else:
                self.hammer_movement = 0
            self.hammer_movement += 0.075
            self.cushion = 10
        mario_rect = pygame.Rect(self.pos, (self.img_arr[self.img_counter].get_width(), self.img_arr[self.img_counter].get_height()))
        for i in items:
            if mario_rect.colliderect(i):
                # self.img_counter = 4
                self.hammer = True
                return 10
        for b in barrels:
            r = tuple(b.get_rect())
            print "R"
            print r
            mod_rect = pygame.Rect((r[0]+35, r[1]+5), (r[2]-5, r[3]))
            if mario_rect.colliderect(mod_rect):
                if not self.hammer:
                    print "collision"
                    return False
                else:
                    return ('barrel', barrels.index(b))
