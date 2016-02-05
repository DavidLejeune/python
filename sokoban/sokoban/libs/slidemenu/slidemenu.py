#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
font.init()
from math import cos,radians
from . import GetEvent
try:
    from . import GetEvent
except ValueError:
    import GetEvent

def menu(
         menu,                          # iterable of str as ("item",) or ("item::tooltip",)
         font1      = None,             # font object|None(pygame default font): unhighlighted item font
         font2      = None,             # font object|None(font1): highlighted item font
         color1     = (128,128,128),    # (int,int,int)|color object: unhighlighted item color
         color2     = None,             # (int,int,int)|color object|None(calculated from the light arg): highlighted/neon item color
         interline  = 5,                # int: items spacing
         justify    = True,             # boolean
         light      = 5,                # int in range [-10,10]: use if color2 is None
         speed      = 300,              # int (0 = no sliding): anim speed
         lag        = 30,               # int in range [0,90]
         neon       = True,             # boolean: set neon effect
         commfont   = None,             # font object|None(pygame default font)
         commtime   = 2000,             # int
         x          = None,
         y          = None,
         topleft    = None,
         midtop     = None,
         topright   = None,
         midleft    = None,
         center     = None,
         midright   = None,
         bottomleft = None,
         midbottom  = None,
         bottomright= None,
         centerx    = None,
         centery    = None
        ):
    """
    menu(
         menu,                          # iterable of str as ("item",) or ("item::tooltip",)
         font1      = None,             # font object|None(pygame default font): unhighlighted item font
         font2      = None,             # font object|None(font1): highlighted item font
         color1     = (128,128,128),    # (int,int,int)|color object: unhighlighted item color
         color2     = None,             # (int,int,int)|color object|None(calculated from the light arg): highlighted/neon item color
         interline  = 5,                # int: items spacing
         justify    = True,             # boolean
         light      = 5,                # int in range [-10,10]: use if color2 is None
         speed      = 300,              # int (0 = no sliding): anim speed
         lag        = 30,               # int in range [0,90]
         neon       = True,             # boolean: set neon effect
         commfont   = None,             # font object|None(pygame default font)
         commtime   = 2000              # int
         x          = None,
         y          = None,
         topleft    = None,
         midtop     = None,
         topright   = None,
         midleft    = None,
         center     = None,
         midright   = None,
         bottomleft = None,
         midbottom  = None,
         bottomright= None,
         centerx    = None,
         centery    = None

    return: (None,None) if hit escape else (item,index)

    """
    shad = 100 # test

    class Item(Rect,object):
        def __init__(self,rect,label,comm):
            Rect.__init__(self,rect)
            self.label = label
            render1 = font1.render(label,1,color1)
            if justify: self.centerx = r1.centerx
            self.render1 = Surface(render1.get_rect().inflate(3,3).size,SRCALPHA)
            self.render1.blit(render1,(3,3))
            self.render1.fill((0,0,0,shad),special_flags=BLEND_RGBA_MIN)
            #sub1 = scr.subsurface(self.move(3,3)).copy().convert_alpha()       # test uncomment
            #surfarray.pixels_alpha(sub1)[:] = surfarray.array_alpha(render1)   # test uncomment
            sub1 = render1                                                      # test comment
            self.render1.blit(sub1,(0,0))
            self.render2 = font2.render(label,1,color2)
            self.white = self.render2.copy()
            self.white.fill((255,255,255,0),special_flags=BLEND_RGBA_MAX)
            if neon:
                render2 = font2.render(label,1,color1)
                renderneon = self.render2.copy()
                self.render2 = Surface(render2.get_rect().inflate(2,2).size,SRCALPHA)
                for pos in ((0,0),(0,1),(0,2),(1,0),(2,0),(0,2),(1,2),(2,2)):
                    self.render2.blit(renderneon,pos)
                self.render2.blit(render2,(1,1))
            if comm:
                comm = commfont.render(comm,1,(200,200,200))
                r = comm.get_rect().inflate(11,7)
                self.comm = Surface(r.size,SRCALPHA)
                r = self.comm.fill((0,0,0,shad),(3,3,r.w-3,r.h-3))
                r = self.comm.fill((200,200,200,30),r.move(-3,-3))
                self.comm.fill((0,0,0,200),r.inflate(-2,-2))
                self.comm.blit(comm,(4,2))
            else:
                self.comm = None

    def show():
        i = Rect((0,0),menu[idx].render2.get_size())
        if justify: i.center = menu[idx].center
        else: i.midleft = menu[idx].midleft
        scr.blit(bg,r2,r2)
        [scr.blit(item.render1,item) for item in menu if item!=menu[idx]]
        scr.blit(menu[idx].white,i)
        display.update(r2)
        time.wait(50)
        r = scr.blit(menu[idx].render2,i)
        display.update(r.inflate(2,2))
        return r

    def anim():
        clk = time.Clock()
        a = [menu[0]] if lag else menu[:]
        c = 0
        while a:
            for i in a:
                g = i.__copy__()
                i.x = i.animx.pop(0)
                r = scr.blit(i.render1,i).inflate(6,6)
                display.update((g,r))
                scr.blit(bg,r,r)
            c +=1
            if not a[0].animx:
                a.pop(0)
                if not lag: break
            if lag:
                foo,bar = divmod(c,lag)
                if not bar and foo < len(menu):
                    a.append(menu[foo])
            clk.tick(speed)

    mouse_bottonright = mouse.get_cursor()[0]
    events = event.get()
    scr = display.get_surface()
    scrrect = scr.get_rect()
    bg = scr.copy()
    if not font1: font1 = font.Font(None,scrrect.h//len(menu)//3)
    if not font2: font2 = font1
    if not color1: color1 = (128,128,128)
    if not color2: color2 = list(map(lambda x:x+int(((255-x)if light>0 else x)*(light/10.)),color1))
    if not commfont: commfont = font.Font(None,int(font1.size('')[1]//1.5))
    menu,comm = zip(*[i.partition('::')[0::2]for i in menu])
    m = max(menu,key=font1.size)
    r1 = Rect((0,0),font1.size(m))
    ih = r1.size[1]
    r2 = Rect((0,0),font2.size(m))
    r2.union_ip(r1)
    w,h = r2.w-r1.w,r2.h-r1.h
    r1.h = (r1.h+interline)*len(menu)-interline
    r2 = r1.inflate(w,h).inflate(6,6)

    pos = {"x":x,
           "y":y,
           "topleft":topleft,
           "midtop":midtop,
           "topright":topright,
           "midleft":midleft,
           "center":center,
           "midright":midright,
           "bottomleft":bottomleft,
           "midbottom":midbottom,
           "bottomright":bottomright,
           "centerx":centerx,
           "centery":centery}

    for k,v in pos.items():
        if v != None:
           setattr(r2,k,v)
           break
    else: r2.center = scrrect.center

    if justify: r1.center = r2.center
    else : r1.midleft = r2.midleft

    menu = [Item(((r1.x,r1.y+e*(ih+interline)),font1.size(i)),i,comm[e]) for e,i in enumerate(menu)if i]

    if speed:
        for i in menu:
            z = r1.w-i.x+r1.x
            i.animx = [cos(radians(x))*(i.x+z)-z for x in list(range(90,-1,-1))]
            i.x = i.animx.pop(0)
        anim()
        for i in menu:
            z = scrrect.w+i.x-r1.x
            i.animx = [cos(radians(x))*(-z+i.x)+z for x in list(range(0,-91,-1))]
            i.x = i.animx.pop(0)


    mpos = Rect(mouse.get_pos(),(0,0))
    event.post(event.Event(MOUSEMOTION,{'pos': mpos.topleft if mpos.collidelistall(menu) else menu[0].center}))
    idx = -1
    comm_seen = 0
    while True:
        ev = GetEvent.poll()
        if ev.type == NOEVENT and ev.inactiv >= commtime:
            if not comm_seen and menu[idx].comm and r.collidepoint(mouse.get_pos()):
                rcom = menu[idx].comm.get_rect(topleft=mouse.get_pos()).inflate(4,4).move(mouse_bottonright).clamp(scrrect)
                combg = scr.subsurface(rcom).copy()
                scr.blit(menu[idx].comm,rcom)
                display.update(rcom)
                comm_seen = 1
        if ev.type == MOUSEMOTION:
            idx_ = Rect(ev.pos,(0,0)).collidelist(menu)
            if idx_ != idx:
                if comm_seen and (not r.collidepoint(mouse.get_pos()) or idx_ > -1):
                    display.update(scr.blit(combg,rcom))
                    comm_seen = 0
                if idx_ > -1:
                    idx = idx_
                    r = show()
        elif ev.type == MOUSEBUTTONUP and ev.button == 1 and r.collidepoint(ev.pos):
            ret = menu[idx].label,idx
            break
        elif ev.type == KEYDOWN:
            try:
                idx = (idx + {K_UP:-1,K_DOWN:1}[ev.key])%len(menu)
                if comm_seen:
                    display.update(scr.blit(combg,rcom))
                    comm_seen = 0
                r = show()
            except:
                if ev.key in (K_RETURN,K_KP_ENTER):
                    ret = menu[idx].label,idx
                    break
                elif ev.key == K_ESCAPE:
                    ret = None,None
                    break

    if comm_seen:
        display.update(scr.blit(combg,rcom))
    scr.blit(bg,r2,r2)

    if speed:
        [scr.blit(i.render1,i) for i in menu]
        display.update(r2)
        anim()
    else: display.update(r2)

    for ev in events: event.post(ev)
    return ret

if __name__ == '__main__':
    from os.path import dirname,join
    here = dirname(__file__)
    scr = display.set_mode((0,0),FULLSCREEN)
    bg = image.load(join(here,'bg.png'))
    scr.blit(bg,bg.get_rect(center=scr.get_rect().center))
    display.flip();print(menu.__doc__)

    while True:
        resp = menu(['one player',
                     'two players',
                     'level editor::not yet implemented',
                     '',
                     'options',
                     're-show::click here to show again',
                     'quit::good bye'],
                     font1      = font.Font(join(here,'321impact.ttf'),25),
                     font2      = font.Font(join(here,'321impact.ttf'),30),
                     commfont   = font.Font(join(here,"Roboto-MediumItalic.ttf"),12),
                     color1     = (255,80,40),
                     light      = 9,
                     commtime   = 50)

        if resp[0] != "re-show": break
    print(resp)
    quit()