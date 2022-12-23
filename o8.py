import pygame as pg
import sys
pg.init()
clock = pg.time.Clock()
font = pg.font.SysFont('timesnewroman', 18)

def yazi_yaz(ekran,metin,tx,ty,renk=(255,255,255)):
    """ 
    tx text left cord.
    ty text top cord.
     """
    global font
    text = font.render(metin, True, renk)
    textRect = text.get_rect()
    textRect.centerx = tx
    textRect.centery = ty
    ekran.blit(text, textRect)

en , boy = 800 , 600
gri = 125,125,12
beyaz = 255 ,255, 255
kzm = 255,0,0

ekran = pg.display.set_mode( (en,boy)  )

karolar = []
karo_en = 40
karo_boy = 40

for i in range(en//karo_en * boy//karo_boy) :
    karolar.append((i * karo_en % en, (i * karo_en // en)*karo_boy ))


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT :
            sys.exit();
    ekran.fill(gri)
    i = 1
    for cord in karolar:
        pg.draw.rect(ekran,beyaz,(cord[0],cord[1],karo_en,karo_boy), 3 )
        yazi_yaz(ekran,str(i),cord[0]+20,cord[1]+20)
        i += 1
    pg.draw.rect(ekran,kzm,( karolar[30][0],karolar[30][1] ,karo_en,karo_boy), 3 )
    pg.display.flip()
    clock.tick(30)
