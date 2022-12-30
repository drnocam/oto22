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
            karolar.append([ mouse_index, 1])
        if event.type == pg.QUIT :
            sys.exit();
    ekran.fill(gri)

    for ind in range(len(karolar)):
        
        sol = sag = alt = 0
        for ind2 in range(len(karolar)):
            if ind == ind2 :
                # mevcut karo ise bakma.
                continue
            if karolar[ind2][0] == karolar[ind][0] +  en // karo_en :
                #altı dolu
                alt = 1
            elif karolar[ind2][0] == karolar[ind][0] +  en // karo_en -1 :
                #sol aşağı dolu
                sol = 1
            elif karolar[ind2][0] == karolar[ind][0] +  en // karo_en + 1 :
                #sağ aşağı dolu..
                sag = 1

        if karolar[ind][0] <  (en // karo_en) * (boy // karo_boy -1)  :
            if(alt==0) :
                karolar[ind][0] +=  en // karo_en 
            elif sol==0 :
                karolar[ind][0] =  karolar[ind][0] +  en // karo_en -1
            elif sag == 0:
                karolar[ind][0] +=  en // karo_en + 1 
        x , y = kordinat_hesapla( karolar[ind][0] )
        pg.draw.rect(ekran,sari,(x , y,karo_en,karo_boy) )

    pg.display.flip()
    clock.tick(10)
