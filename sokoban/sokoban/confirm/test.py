from pygame import *
font.init()
import Confirm

scr = display.set_mode((500,300))
scr.blit(font.Font(None,25).render('I do nothing ... click on the red X to close',1,(200,200,200)),(50,50))
display.flip()
while 1:
    ev = event.wait()
    if ev.type == QUIT:
        if Confirm.get('Do you really want to leave this program?') == True: break
scr.blit(font.Font(None,25).render('Bye ...',1,(200,200,200)),(50,75))
display.flip()
time.wait(1000)
