import pygame

gameTitle = 'Snake Revamp'
gameExit = False



pygame.init()
x = pygame.init()
print(x)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Snake Revamp')

pygame.display.update()
#pygame.display.flip()


while not gameExit:
    for event in pygame.event.get():
        print(event)







pygame.quit()
quit()
