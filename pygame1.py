import pygame

gameTitle = 'Snake Revamp'
gameExit = False


#intialise the pygame stuff
#return result of init
#pygame.init()
x = pygame.init()
print(x)

#basic frame with title
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption(gameTitle)

pygame.display.update()
#alternative : pygame.display.flip()


while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        #event debugging
        print(event)


pygame.quit()
quit()



