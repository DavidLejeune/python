# Classic Donkey Kong Port
# Visrut Sudhakar
# April, 2015

import pygame, sys
import platform
import spritesheet
import boss

## Colors ##
BLACK = (0, 0, 0)
RED = (255, 0, 0)
## End Colors ##

pygame.init()

FPS = 30
clock = pygame.time.Clock()

size = (600, 800)

screen = pygame.display.set_mode(size)  # Main surface

background = pygame.Surface(size) # BG Surface
background = background.convert()

foreground = pygame.Surface(size)

background.fill(BLACK)

# Generate and draw platforms
levels = platform.Platforms(size, 3)
foreground = levels.render(foreground)

# Create and add characters
dk = boss.DK()

# Move controllers
dk_right = False
dk_left = False

# Game Loop
while True:
    pygame.draw.rect(foreground, (255, 0, 0), dk.obj)

    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        print "Exit"
        break

    # Keyboard events
    if ev.type == pygame.KEYDOWN:
        print ev.key
        if ev.key == 32:
            levels.iSmash()
            foreground.fill((0,0,0,0))
            foreground = levels.render(foreground)
        if ev.key == 275:
            dk_right = True
        if ev.key == 276:
            dk_left = True
    if ev.type == pygame.KEYUP:
        print ev.key
        if ev.key == 275:
            dk_right = False
        if ev.key == 276:
            dk_left = False

    if dk_right:
        print 'bananas'
        foreground.fill((0,0,0,0))
        foreground = levels.render(foreground)
        dk.move_right()
    if dk_left:
        foreground.fill((0,0,0,0))
        foreground = levels.render(foreground)
        dk.move_left()

    screen.blit(background, (0, 0))
    screen.blit(foreground, (0, 0))
    pygame.display.flip()

print "Quitting game"
pygame.quit()
sys.exit()
