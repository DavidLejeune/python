# Classic Donkey Kong Port
# Visrut Sudhakar
# April, 2015

import pygame, sys
import platform
import spritesheet

## Colors ##
BLACK = (0, 0, 0)
RED = (255, 0, 0)
## End Colors ##

pygame.init()

size = (600, 800)

screen = pygame.display.set_mode(size)  # Main surface

background = pygame.Surface(size) # BG Surface
background = background.convert()
foreground = pygame.Surface(size)
background.fill(BLACK)

# Generate and draw platforms
levels = platform.Platforms(size, 3)
foreground = levels.render(foreground)

# Game Loop
while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        print "Exit"
        break

    # Keyboard events
    if ev.type == pygame.KEYDOWN:
        print ev.key
        if ev.key == 32:
            levels.iSmash()
            foreground.fill(BLACK)
            foreground = levels.render(foreground)

    screen.blit(background, (0, 0))
    screen.blit(foreground, (0, 0))
    pygame.display.flip()

print "Quitting game"
pygame.quit()
sys.exit()
