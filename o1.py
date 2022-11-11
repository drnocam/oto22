import pygame as pg
import sys
pg.init()

en , boy = 800 , 600
siyah =  0 , 0 , 0 # RGB 0- 255
beyaz = 255 ,255, 255

ekran = pg.display.set_mode( (en,boy)  )

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT :
            sys.exit();
    ekran.fill(siyah)
    pg.draw.circle(ekran,beyaz,( en//2 , boy //2  ),20)
    pg.display.flip()
