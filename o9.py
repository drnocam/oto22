import pygame as pg
import sys
pg.init()
clock = pg.time.Clock()

def kordinat_hesapla(index) :
    global karo_boy , karo_en , en
    return index * karo_en % en, (index * karo_en // en)*karo_boy


en , boy = 800 , 600
gri = 125,125,12
beyaz = 255 ,255, 255
sari = 255 ,255, 0
kzm = 255,0,0

ekran = pg.display.set_mode( (en,boy)  )

karolar = []
karo_en = 40
karo_boy = 40

# ilk sıradaki index ikincisi kum, su veya taş
karolar.append([ 50, 1])


kutu_yer = 0
mouse_index = 0
while True:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN :
            mx, my = pg.mouse.get_pos()
            mouse_index =  mx //40 + (my // 40 )*20
        if event.type == pg.QUIT :
            sys.exit();
    ekran.fill(gri)

    for cord in karolar:
        x , y = kordinat_hesapla( cord[0] )
        pg.draw.rect(ekran,sari,(x , y,karo_en,karo_boy) )


    pg.display.flip()
    clock.tick(10)
