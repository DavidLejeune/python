# This is the game

import pygame, sys
import spritesheet
from mario import Mario
from rollingbarrel import RollingBarrel
import random

## Colors ##
BLACK = (0, 0, 0)
RED = (255, 0, 0)
## End Colors ##

lives = 3

def game():
    pygame.init()

    FPS = 10
    clock = pygame.time.Clock()

    size = (600, 850)

    screen = pygame.display.set_mode(size)  # Main surface

    ss = spritesheet.spritesheet('res\sprites\hammer.png')
    scale_factor = 4
    hammer_img = pygame.transform.scale(ss.image_at((0, 0, 10, 15)), (10*scale_factor, 15*scale_factor))

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

    platforms.append([(300, 50), (300+platform_img.get_width(), 50)])

    #(106, 125)

    #Segment platforms
    for i in range(len(platforms[0])/2-2, len(platforms[0])):
        curr_y = platforms[0][i][1]
        curr_y -= 6*(i - (len(platforms[0])/2-2))
        platforms[0][i] = (platforms[0][i][0], curr_y)

    for i in range(0, len(platforms[1])/2):
        curr_y = platforms[1][i][1]
        curr_y += 6*(i - (len(platforms[1])/2))
        ##print i
        platforms[1][i] = (platforms[1][i][0], curr_y)

    for i in range(len(platforms[2])/2-2, len(platforms[0])):
        curr_y = platforms[2][i][1]
        curr_y -= 6*(i - (len(platforms[2])/2-2))
        platforms[2][i] = (platforms[2][i][0], curr_y)

    for i in range(0, len(platforms[3])/2):
        curr_y = platforms[3][i][1]
        curr_y += 6*(i - (len(platforms[3])/2))
        ##print i
        platforms[3][i] = (platforms[3][i][0], curr_y)

    for i in range(len(platforms[4])/2-2, len(platforms[4])):
        curr_y = platforms[4][i][1]
        curr_y -= 6*(i - (len(platforms[4])/2-2))
        ##print i
        platforms[4][i] = (platforms[4][i][0], curr_y)

    barrel_sprite = ss.image_at((95, 260, 16, 10))
    barrel_sprite   = pygame.transform.scale(barrel_sprite, (16*scale_factor, 10*scale_factor))

    rolling_barrel_sprite_arr = [ss.image_at((65, 257, 15, 12)).convert_alpha(), ss.image_at((80, 257, 15, 12)).convert_alpha(), ss.image_at((65, 270, 15, 10)).convert_alpha(), ss.image_at((80, 270, 15, 10)).convert_alpha()]

    for b in range(len(rolling_barrel_sprite_arr)):
        rolling_barrel_sprite_arr[b] = pygame.transform.scale(rolling_barrel_sprite_arr[b], (10*scale_factor, 10*scale_factor))

##    rolling_barrel = RollingBarrel((300,15*scale_factor*2+5), rolling_barrel_sprite_arr, (170, size[0]))

    rolling_barrels = []

    scale_factor  = 3
    mario_sprites = []
    mario_sprites.append(pygame.Surface.convert_alpha(pygame.transform.scale(ss.image_at((94, 3, 15, 17)), (15*scale_factor, 17*scale_factor))))
    mario_sprites.append(pygame.Surface.convert_alpha(pygame.transform.scale(ss.image_at((175, 3, 15, 17)), (15*scale_factor, 17*scale_factor))))
    mario_sprites.append(pygame.Surface.convert_alpha(pygame.transform.scale(ss.image_at((160, 3, 15, 17)), (15*scale_factor, 17*scale_factor))))
    mario_sprites.append(pygame.Surface.convert_alpha(pygame.transform.scale(ss.image_at((135, 3, 15, 17)), (15*scale_factor, 17*scale_factor))))
    mario_sprites.append(pygame.Surface.convert_alpha(pygame.transform.scale(ss.image_at((114, 4, 15, 17)), (15*scale_factor, 17*scale_factor))))
    mario_sprites.append(pygame.Surface.convert_alpha(pygame.transform.scale(ss.image_at((196, 3, 15, 17)), (15*scale_factor, 17*scale_factor))))

    mario_hammer_sprites = []
    mario_hammer_sprites.append(pygame.Surface.convert_alpha(pygame.transform.scale(ss.image_at((69, 55, 26, 20)), (15*scale_factor, 17*scale_factor))))

    mario_sprites.append(pygame.Surface.convert(pygame.transform.scale(ss.image_at((69, 55, 28, 18)), (20*scale_factor, 22*scale_factor))))
    mario_sprites.append(pygame.Surface.convert(pygame.transform.scale(ss.image_at((102, 43, 19, 30)), (22*scale_factor, 26*scale_factor))))
    mario_sprites.append(pygame.Surface.convert(pygame.transform.scale(ss.image_at((69, 55, 28, 18)), (20*scale_factor, 22*scale_factor))))
    mario_sprites.append(pygame.Surface.convert(pygame.transform.scale(ss.image_at((69, 55, 28, 18)), (20*scale_factor, 22*scale_factor))))
    mario_sprites.append(pygame.Surface.convert(pygame.transform.scale(ss.image_at((157, 54, 28, 18)), (20*scale_factor, 22*scale_factor))))
    mario_sprites.append(pygame.Surface.convert(pygame.transform.scale(ss.image_at((189, 43, 19, 30  )), (22*scale_factor, 26*scale_factor))))
    #(69,55)

    mario_character = Mario((0, size[1]-mario_sprites[0].get_height()-62), mario_sprites, mario_hammer_sprites)

    daisy_sprite = pygame.Surface.convert_alpha(pygame.transform.scale(ss.image_at((106, 125, 15, 17)), (15*scale_factor, 17*scale_factor)))

    ss = spritesheet.spritesheet('res\sprites\enemies.png')

    dk_sprites = []
    dk_sprites.append(ss.image_at((100, 0, 50, 40)))

    for i in range(5):
        dk_sprites.append(ss.image_at((50*i, 50, 50, 40)))

    for i in range(5):
        dk_sprites.append(ss.image_at((50*i, 100, 50, 40)))

    scale_factor = 2

    ##print "# of sprites", len(dk_sprites)

    for i in range(len(dk_sprites)):
        dk_sprites[i] = pygame.transform.scale(dk_sprites[i], (50*scale_factor, 40*scale_factor))

    ss = spritesheet.spritesheet('res\sprites\ladder.png')

    scale_factor = 2
    ladder_sprite = pygame.transform.scale(ss.image_at((0, 0, 20, 50)), (int(20*scale_factor), int(40*scale_factor)))

    ladders = [[(500, 660)],[(50, 540)],[(500, 420)],[(70, 300)],[(480, 190)],[(310, 90)],[]]

    background = pygame.Surface(size) # BG Surface
    background = background.convert()
    blank = pygame.Surface(size)
    blank.fill(BLACK)

    foreground = pygame.Surface(size)

    background.fill(BLACK)

    dk_sprite_counter = 1

    left, right, up, down, jump = False, False, False, False, False

    dk_launch_stage = 0
    dk_launch = False

    game_state = True

    items = [(400,300)]

    launch_buffer = 0

    daisy_call = 0

    while game_state:
        if launch_buffer % 500 == 0:
            # l_int = random.randint(1,100)
            # if l_int >= 97 and l_int <= 100:
            #     dk_launch = True
            dk_launch = True
        launch_buffer += 1

        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            ##print "Exit"
            quit_game()

        if dk_launch:
            #print dk_launch_stage
            if dk_launch_stage == 0:
                dk_sprite_counter = 0
            elif dk_launch_stage == 4:
                dk_sprite_counter = 5
            elif dk_launch_stage == 8:
                dk_sprite_counter = 1
                dk_launch_stage = 0
                dk_launch = False
                fall = random.randint(0, 1)
                if fall == 1:
                    rolling_barrels.append(RollingBarrel((170,15*scale_factor*2+50), rolling_barrel_sprite_arr, (170, size[0]), True))
                else:
                    rolling_barrels.append(RollingBarrel((170,15*scale_factor*2+50), rolling_barrel_sprite_arr, (170, size[0])))
            if dk_launch:
                dk_launch_stage += 1
        # Keyboard events
        if ev.type == pygame.KEYDOWN:
            #print ev.key
            # Cycle sprites for DK
            if ev.key == 113:
                if dk_sprite_counter == 1:
                    dk_sprite_counter = 0
                elif dk_sprite_counter == 0:
                    dk_sprite_counter = 5
                elif dk_sprite_counter == 5:
                    dk_sprite_counter = 1
            if ev.key == 275:
                right = True
            if ev.key == 276:
                left = True
            if ev.key == 273:
                up = True
            if ev.key == 274:
                down = True
            if ev.key == 116:
                dk_launch = True
            if ev.key == 32:
                jump = True
        if ev.type == pygame.KEYUP:
            if ev.key == 275:
                right = False
            if ev.key == 276:
                left = False
            if ev.key == 273:
                up = False
            if ev.key == 274:
                down = False
            if ev.key == 32:
                jump = False

        background.blit(blank, (0,0))

        for places in platforms:
            for pls in places:
                background.blit(platform_img, pls)

        for levels in ladders:
            for points in levels:
                background.blit(ladder_sprite, points)

        background.blit(dk_sprites[dk_sprite_counter], (80,88))


        mario_character.render(background)

##        rolling_barrel.update(platforms, platform_img.get_height(), ladders)
##        rolling_barrel.render(background)

        for rb in rolling_barrels:
            rb.update(platforms, platform_img.get_height(), ladders)
            rb.render(background)

        buffer_height = 5

        for i in range(4):
            background.blit(barrel_sprite, (0, buffer_height+barrel_sprite.get_height()*i))

        background.blit(daisy_sprite, (310, 10))

        m_items = []
        for i in items:
            m_items.append(pygame.Rect(i[0], i[1], hammer_img.get_width(), hammer_img.get_height()))
            background.blit(hammer_img, i)

        mario_status = mario_character.update(left, right, up, down, jump, platforms, platform_img.get_height(), ladders, rolling_barrels, m_items)

        font = pygame.font.Font(None, 20)
        text = font.render("Lives: " + str(lives), 1, (250, 250, 250))
        background.blit(text, (int(size[0]-70), int(10)))

        if daisy_call > 0 and daisy_call < 150:
            font = pygame.font.Font(None, 25)
            text = font.render("HELP!", 1, (250, 250, 250))
            background.blit(text, (360, 10))
        daisy_call += 1
        if daisy_call >= 300:
            daisy_call = 0

        if mario_status == False:
            font = pygame.font.Font(None, 40)
            text = font.render("FAILED", 1, (250, 0, 0))
            background.blit(text, (int(size[0]/2), int(size[1]/2)))
            game_state = False
            global lives
            lives -= 1
        elif mario_status == 10:
            items = []
        elif type(mario_status) == tuple:
            rolling_barrels.pop(mario_status[1])

        screen.blit(background, (0, 0))
        pygame.display.flip()

def quit_game():
    #print "Quitting game"
    pygame.quit()
    sys.exit()

for i in range(3):
    game()
    pygame.time.wait(3000)

quit_game()
