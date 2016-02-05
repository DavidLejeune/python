#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import environ
environ['SDL_VIDEO_CENTERED'] = '1'
import os.path
thisrep = os.path.dirname(__file__)
imagesrep = os.path.join(thisrep,'images')

from pygame import *
font.init()
font = font.Font(os.path.join(thisrep,'MonospaceTypewriter.ttf'),16)

from textwrap import wrap
from subprocess import Popen,PIPE
from sys import stdout

class Button(Rect):
    def __init__(self,image0,image1):
        self.scr = display.get_surface()
        self.images = [image0,image1]
        Rect.__init__(self,image0.get_rect())
        self.status = False
        self.over = False
        
    def update(self,ev):
        if ev.type == MOUSEMOTION:
            if self.collidepoint(ev.pos) and not self.over:
                self.over = True
                return True
            elif not self.collidepoint(ev.pos) and self.over:
                self.over = False
                return True
        elif ev.type == MOUSEBUTTONUP and ev.button == 1 and self.collidepoint(ev.pos):
            self.status = True
            return True
        elif ev.type == ACTIVEEVENT:
            self.over = False
            return True
        
    def screen(self):
        return self.scr.blit(self.images[self.over],self)
        


def get(label='...',title='Message'):
    args = ["python", __file__,label,title]
    return eval(Popen(args,stdout=PIPE).communicate()[0].strip())

if __name__ == '__main__':
    import sys
    try: label = sys.argv[1].replace('\\n','\n')
    except: label = '...'
    try: title = sys.argv[2]
    except: title = 'Message'
    
    width = 300
    
    w,h = font.size(' ')
    y = 10

    wrap = sum([wrap(line,(width-20) // w,drop_whitespace=False) for line in label.expandtabs(4).split('\n')],[])

    height = h*len(wrap)+92
    scr = display.set_mode((width,height))
    display.set_caption(title)
    scr.fill(0x202020)
    
    
    for line in wrap:
        x = 10
        for char in line:
            scr.blit(font.render(char,1,(0,0,0)),(x+2,y+2))
            scr.blit(font.render(char,1,(255,255,255)),(x,y))
            x += w
        y += h
    
    NO = Button(image.load(os.path.join(imagesrep,"NO.png")),image.load(os.path.join(imagesrep,"NO1.png")))
    NO.bottomleft = 10,height-10
    YES = Button(image.load(os.path.join(imagesrep,"YES.png")),image.load(os.path.join(imagesrep,"YES1.png")))
    YES.bottomright = width-10,height-10
    back = Button(image.load(os.path.join(imagesrep,"back.png")),image.load(os.path.join(imagesrep,"back1.png")))
    back.midbottom = width//2,height-10
    
    NO.screen()
    YES.screen()
    back.screen()

    display.flip()

    while 1:
        ev = event.wait()
        if NO.update(ev):
            scr.fill(0x202020,NO)
            display.update(NO.screen())
            if NO.status:
                stdout.write('False')
                break
        if YES.update(ev):
            scr.fill(0x202020,YES)
            display.update(YES.screen())
            if YES.status:
                stdout.write('True')
                break
        if back.update(ev):
            scr.fill(0x202020,back)
            display.update(back.screen())
            if back.status:
                stdout.write('None')
                break
    
