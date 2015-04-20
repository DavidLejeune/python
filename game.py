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

    size = (600, 800)

    screen = pygame.display.set_mode(size)  # Main surface

    ss = spritesheet.spritesheet('res\sprites\misc.gif')
    scale_factor = 4
    platform_img = pygame.transform.scale(ss.image_at((222, 270, 16, 10)), (16*scale_factor, 10*scale_factor))

    platforms = []

    h = size[1] - platform_img.get_height()

    for j in range(6):
        l = []
        for i in range(0, size[0], platform_img.get_width()):
            l.append((i, h))
        platforms.append(l)
        h -= platform_img.get_height() * 4

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

    dk_sprite_counter = 3

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
                dk_sprite_counter += 1

        for places in platforms:
            for pls in places:
                background.blit(platform_img, pls)

        background.blit(dk_sprites[dk_sprite_counter], (80,48))

        screen.blit(background, (0, 0))
        pygame.display.flip()

    print "Quitting game"
    pygame.quit()
    sys.exit()

game()
