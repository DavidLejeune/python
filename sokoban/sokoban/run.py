from pygame import *
font.init()
FONT35 = font.Font(font.get_default_font(),35)
FONT25 = font.Font(font.get_default_font(),25)

from libs.slidemenu import slidemenu
from os import listdir

import confirm.Confirm as Confirm

import os.path
imgrep = os.path.join(os.path.dirname(__file__),'images')
categrep = os.path.join(os.path.dirname(__file__),'categs')

SCREEN = display.set_mode((800,800))
FADE = Surface((800,800))


wall = image.load(os.path.join(imgrep,'parpaing.png'))
woodbox = image.load(os.path.join(imgrep,'woodbox2.png'))
zone = image.load(os.path.join(imgrep,'zone.png'))
perso = image.load(os.path.join(imgrep,'perso.png'))
intro = image.load(os.path.join(imgrep,'intro.png'))

CATEG = 0
NAME_CATEG = 0
LEVEL = 0
NUM_LEVEL = 1
POS = 0
BG = SCREEN.copy()
NB_ZONE = 0

def load_categs():
    global CATEG,NUM_LEVEL,NAME_CATEG
    categs = listdir(categrep)
    categs.sort()
    menu = categs[:]
    with open(os.path.join(os.path.dirname(__file__),'save.txt'),'r') as s:
        a,b = zip(*[i.strip().split(':') for i in s.readlines()])
        for e,i in enumerate(menu):
            try:
                index = a.index(i)
                menu[e] += '   '+b[index]
            except: continue
    NAME_CATEG = slidemenu.menu(menu,color1=(150,150,250),interline=10,font1=FONT35,light=8,justify=False,speed=450,neon=False)[0]
    if NAME_CATEG == None: return
    index = menu.index(NAME_CATEG)
    NAME_CATEG = categs[index]
    with open(os.path.join(categrep,NAME_CATEG),'r') as CATEG:
        CATEG = CATEG.read().replace('\r','').split(';')
        for index,level in enumerate(CATEG):
            level = level.split('\n')
            CATEG[index] = level[level.index('')+1:-2]
    try: NUM_LEVEL = int(b[a.index(NAME_CATEG)].split('/')[0])+1
    except: NUM_LEVEL = 1

def resize():
    global SIZE,IMAGES
    SIZE = 800//max(len(max(LEVEL,key=len)),len(LEVEL))
    if SIZE > 80: SIZE = 80
    IMAGES = {'#':wall,'$':woodbox,'.':zone,'@':perso}
    for i in IMAGES:
        IMAGES[i] = transform.scale(IMAGES[i],(SIZE,SIZE))

def draw_level():
    global POS,NB_ZONE
    NB_ZONE = 0
    FADE.fill(0x100005)
    BG.fill(0x100005)
    for y,lin in enumerate(LEVEL):
        for x,item in enumerate(lin):
            pos = x*SIZE,y*SIZE
            try:
                FADE.blit(IMAGES[item],pos)
                if item == '@':
                    POS = x,y
                    LEVEL[y][x] = ' '
                elif item != '$':
                    BG.blit(IMAGES[item],pos)
                    if item == '.':
                        NB_ZONE += 1
            except:
                if item != ' ':
                    FADE.blit(IMAGES['.'],pos)
                    BG.blit(IMAGES['.'],pos)
                    if item == '*':
                        FADE.blit(IMAGES['$'],pos)
                    else:
                        FADE.blit(IMAGES['@'],pos)
                        POS = x,y
                        LEVEL[y][x] = '.'
                        NB_ZONE += 1
    cp = SCREEN.copy()
    for i in range(1,256,2):
        FADE.set_alpha(i)
        SCREEN.blit(cp,(0,0))
        SCREEN.blit(FADE,(0,0))
        display.flip()

def draw_undo():
    SCREEN.blit(BG,(0,0))
    for y,lin in enumerate(LEVEL):
        for x,item in enumerate(lin):
            if item in ('$','*'): SCREEN.blit(IMAGES['$'],(x*SIZE,y*SIZE))
    SCREEN.blit(IMAGES['@'],(POS[0]*SIZE,POS[1]*SIZE))
    display.flip()

def play_level():
    key.set_repeat(20,20)
    global POS,NB_ZONE,LEVEL,Play
    Undo = []
    while NB_ZONE:
        ev = event.wait()
        if ev.type == KEYDOWN:
            try:
                dir = {K_LEFT:(-1,0),K_UP:(0,-1),K_RIGHT:(1,0),K_DOWN:(0,1)}[ev.key]
                if LEVEL[POS[1]+dir[1]][POS[0]+dir[0]] in (' ','.'):
                    Undo.append(([i[:] for i in LEVEL[:]],POS,NB_ZONE))
                    for x in range(SIZE+1):
                        X,Y = POS[0]*SIZE+x*dir[0],POS[1]*SIZE+x*dir[1]
                        SCREEN.blit(BG,(X,Y),(X,Y,SIZE,SIZE))
                        SCREEN.blit(IMAGES['@'],(POS[0]*SIZE+x*dir[0],POS[1]*SIZE+x*dir[1]))
                        display.update((X,Y,SIZE,SIZE))
                        time.wait(3)
                    POS = POS[0]+dir[0],POS[1]+dir[1]

                elif LEVEL[POS[1]+dir[1]][POS[0]+dir[0]] in ('$','*') and LEVEL[POS[1]+dir[1]*2][POS[0]+dir[0]*2] in (' ','.'):
                    Undo.append(([i[:] for i in LEVEL[:]],POS,NB_ZONE))
                    for x in range(SIZE+1):
                        X,Y = POS[0]*SIZE+x*dir[0],POS[1]*SIZE+x*dir[1]
                        XX,YY = (POS[0]+dir[0])*SIZE+x*dir[0],(POS[1]+dir[1])*SIZE+x*dir[1]
                        SCREEN.blit(BG,(X,Y),(X,Y,SIZE,SIZE))
                        SCREEN.blit(BG,(XX,YY),(XX,YY,SIZE,SIZE))
                        SCREEN.blit(IMAGES['@'],(X,Y))
                        SCREEN.blit(IMAGES['$'],(XX,YY))
                        display.update([(X,Y,SIZE,SIZE),(XX,YY,SIZE,SIZE)])
                        time.wait(3)
                    POS = POS[0]+dir[0],POS[1]+dir[1]
                    if LEVEL[POS[1]][POS[0]] == '$': LEVEL[POS[1]][POS[0]] = ' '
                    else:
                        LEVEL[POS[1]][POS[0]] = '.'
                        NB_ZONE += 1
                    if LEVEL[POS[1]+dir[1]][POS[0]+dir[0]] == ' ': LEVEL[POS[1]+dir[1]][POS[0]+dir[0]] = '$'
                    else:
                        LEVEL[POS[1]+dir[1]][POS[0]+dir[0]] = '*'
                        NB_ZONE -= 1
            except:
                if Undo:
                    if ev.key == K_r:
                        LEVEL,POS,NB_ZONE = Undo[0]
                        Undo =[]
                        draw_undo()
                    elif ev.key == K_u:
                        LEVEL,POS,NB_ZONE = Undo.pop()
                        draw_undo()
                        while event.wait().type != KEYUP: pass
                if ev.key == K_ESCAPE:
                    Play = False
                    break
                if ev.key == K_h:
                    bg = SCREEN.copy()
                    BG.set_alpha(50)
                    SCREEN.blit(BG,(0,0))
                    display.flip()
                    BG.set_alpha(None)
                    while event.wait().type != KEYUP: pass
                    SCREEN.blit(bg,(0,0))
                    display.flip()
    key.set_repeat()

def save_progression():
    with open(os.path.join(os.path.dirname(__file__),'save.txt'),'r') as save:
        a,b = zip(*[i.strip().split(':') for i in save.readlines()])
        a,b = list(a),list(b)
        try:
            b[a.index(NAME_CATEG)] = str(NUM_LEVEL)+'/'+str(len(CATEG))
        except:
            a.append(NAME_CATEG)
            b.append(str(NUM_LEVEL)+'/'+str(len(CATEG)))
        out = []
        for i in zip(a,b):
            out.append(':'.join(i))
    with open(os.path.join(os.path.dirname(__file__),'save.txt'),'w') as save:
        save.write('\n'.join(out))

def reset():
    SCREEN.fill(0x100005)
    for i,j in (('select the category you want to reset the save',20),('hit ESC to quit',55)):
        SCREEN.blit(FONT25.render(i,1,(250,200,150)),(20,j))
    display.flip()
    menu = []
    with open(os.path.join(os.path.dirname(__file__),'save.txt'),'r') as s:
        out = s.readlines()
        menu = [i.replace(':','    ').strip() for i in out[1:]]
    if not menu: return
    while menu:
        #SCREEN.fill(0x100005)
        #display.flip()
        choix = slidemenu.menu(menu+['','All'],color1=(150,150,250),interline=10,font1=FONT35,light=5,justify=False,neon=False)[0]
        if choix == None: return
        elif choix == 'All':
            out = out[:1]
            break
        index = menu.index(choix)
        del(menu[index])
        del(out[index+1])
    if choix and Confirm.get('Do you really want to delete your progress ?'):
        with open(os.path.join(os.path.dirname(__file__),'save.txt'),'w') as s: s.write(''.join(out))


while True:
    SCREEN.fill(0x100005)
    SCREEN.blit(intro,(0,0))
    display.flip()
    choix = slidemenu.menu(['START','RESET','QUIT GAME'],interline=10,color1=(150,150,250),font1=FONT35,topleft=(300,500),justify=False,speed=0,neon=False)[0]
    if choix == 'START':
        while True:
            SCREEN.fill(0x100005)
            select = FONT35.render('SELECT A CATEGEGORY',1,(200,200,255))
            R_select = select.get_rect()
            R_select.topleft = 20,20
            SCREEN.blit(select,R_select)
            display.flip()
            load_categs()
            if NAME_CATEG == None: break
            Play = True
            while NUM_LEVEL < len(CATEG):
                LEVEL = [list(s)for s in CATEG[NUM_LEVEL]]
                resize()
                draw_level()
                display.set_caption(NAME_CATEG+'    '+str(NUM_LEVEL)+'/'+str(len(CATEG)))
                play_level()
                if Play == False: break
                save_progression()
                NUM_LEVEL += 1
    elif choix == 'RESET':
        reset()
    elif choix in ('QUIT GAME',None): break
