import pygame as pg
import sys
pg.init()

en , boy = 800 , 600
siyah =  0 , 0 , 0 # RGB 0- 255
beyaz = 255 ,255, 255
kirmizi = 255,0,0
gri = 100,100,100

ekran = pg.display.set_mode( (en,boy)  )
x , y = en//2,boy//2
x_speed = y_speed = 1
y_cap = 50
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT :
            sys.exit();
    ekran.fill(gri)
    pg.draw.circle(ekran,kirmizi,( x , y  ),y_cap)
    
    x += x_speed
    y += y_speed

    if x >= en - y_cap :
        x_speed *= -1
    if x <= 0 + y_cap :
        x_speed *= -1

    if y >= boy - y_cap:
        y_speed *= -1
    if y <=0 + y_cap :
        y_speed *= -1

    pg.display.flip()
