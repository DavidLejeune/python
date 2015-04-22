# This is the game

import pygame, sys
import spritesheet


## Colors ##
BLACK = (0, 0, 0)
RED = (255, 0, 0)
## End Colors ##

def game():
    pygame.init()

    FPS = 30
    clock = pygame.time.Clock()

    size = (600, 850)

    screen = pygame.display.set_mode(size)  # Main surface

    ss = spritesheet.spritesheet('res\sprites\misc.gif')
    scale_factor = 4
    platform_img = pygame.transform.scale(ss.image_at((222, 270, 16, 10)), (16*scale_factor, 10*scale_factor))

    platforms = []

    h = size[1] - platform_img.get_height() - 50

    for j in range(6):
        l = []
        for i in range(0, size[0], platform_img.get_width()):
            l.append((i, h))
        platforms.append(l)
        h -= platform_img.get_height() * 3

    #Segment platforms
    for i in range(len(platforms[0])/2-2, len(platforms[0])):
        curr_y = platforms[0][i][1]
        curr_y -= 6*(i - (len(platforms[0])/2-2))
        platforms[0][i] = (platforms[0][i][0], curr_y)

    for i in range(0, len(platforms[1])/2):
        curr_y = platforms[1][i][1]
        curr_y += 6*(i - (len(platforms[1])/2))
        print i
        platforms[1][i] = (platforms[1][i][0], curr_y)

    for i in range(len(platforms[2])/2-2, len(platforms[0])):
        curr_y = platforms[2][i][1]
        curr_y -= 6*(i - (len(platforms[2])/2-2))
        platforms[2][i] = (platforms[2][i][0], curr_y)

    for i in range(0, len(platforms[3])/2):
        curr_y = platforms[3][i][1]
        curr_y += 6*(i - (len(platforms[3])/2))
        print i
        platforms[3][i] = (platforms[3][i][0], curr_y)

    for i in range(len(platforms[4])/2-2, len(platforms[4])):
        curr_y = platforms[4][i][1]
        curr_y -= 6*(i - (len(platforms[4])/2-2))
        print i
        platforms[4][i] = (platforms[4][i][0], curr_y)

    barrel_sprite = ss.image_at((95, 260, 16, 10))
    barrel_sprite = pygame.transform.scale(barrel_sprite, (16*scale_factor, 10*scale_factor))

    #(94, 3), (15, 17)
    mario_sprites = []
    mario_sprites.append(pygame.transform.scale(ss.image_at((94, 3, 15, 17)), (15*scale_factor, 17*scale_factor)))


    ss = spritesheet.spritesheet('res\sprites\enemies.png')

    dk_sprites = []
    dk_sprites.append(ss.image_at((100, 0, 50, 40)))

    for i in range(5):
        dk_sprites.append(ss.image_at((50*i, 50, 50, 40)))

    for i in range(5):
        dk_sprites.append(ss.image_at((50*i, 100, 50, 40)))

    scale_factor = 2

    for i in range(len(dk_sprites)):
        dk_sprites[i] = pygame.transform.scale(dk_sprites[i], (50*scale_factor, 40*scale_factor))

    background = pygame.Surface(size) # BG Surface
    background = background.convert()

    foreground = pygame.Surface(size)

    background.fill(BLACK)

    dk_sprite_counter = 2


    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            print "Exit"
            break

        # Keyboard events
        if ev.type == pygame.KEYDOWN:
            print ev.key
            # Cycle sprites for DK
            if ev.key == 113:
                if dk_sprite_counter == 2:
                    dk_sprite_counter = 4
                else:
                    dk_sprite_counter = 2

        for places in platforms:
            for pls in places:
                background.blit(platform_img, pls)

        background.blit(dk_sprites[dk_sprite_counter], (80,88))

        sprite = mario_sprites[dk_sprite_counter]
        background.blit(sprite, (0, size[1]-sprite.get_height()-82))

        buffer_height = 5

        for i in range(4):
            background.blit(barrel_sprite, (0, buffer_height+barrel_sprite.get_height()*i))

        screen.blit(background, (0, 0))
        pygame.display.flip()

    print "Quitting game"
    pygame.quit()
    sys.exit()

game()
