# input output i/o

# dosya = open( "cuzdan.oto", "w" )

# liste = ""
# for i in range(100) :
#     if(i==99) :
#         liste += str(i+1) 
#         continue
#     liste += str(i+1) + ", "

# dosya.write(liste)
#print( dosya.read() )
# for satir in dosya.readlines() :
#     print(satir)

# dosya.close()

# try: 
#     dosya = open( "cuzdan.oto", "w" )
# except FileNotFoundError :
#     print("Dosya bulunamadı.")
# finally:
#     if dosya:
#         dosya.close()


# with open("cuzdan.oto") as dosya:
#     print(dosya.read())


# import datetime

# print( datetime.datetime.now() )

from datetime import datetime

# print(datetime.now())
""" şimdi adlı bir fonksiyon tanımladım. .. """
şimdi = datetime.now

ne_zaman = datetime(2020,5,12)

print(şimdi() , ne_zaman)

# zaman = input("Şimdi gün/ay/yıl şeklinde tarihi giriniz.:")
zaman = "  15 / 12  / 2020"
zaman = "15/12/2020"
zaman = "    15/12/2020 "

# def trim(metin) :
#     sonuc = ""
#     for i in metin:
#         if(i == " " ):
#             continue
#         sonuc += i
#     return sonuc


zaman = "    15/4/aa2020 "

# zaman = zaman.strip(" a")

# print(zaman[0:2] , zaman[3:5], zaman[6:] )

import re 


zaman = "    15/4/aa2020 "
def tarih_kontrol(zaman):
    sonuclar = re.findall("(\d+)", zaman)
    if sonuclar :
        if ( len(sonuclar) < 3) : 
            return None
        if str(sonuclar[0]).isnumeric() and str(sonuclar[1]).isnumeric() and str(sonuclar[2]).isnumeric() :
            print("Doğru" , sonuclar)
            return int(sonuclar[0]) ,int(sonuclar[1]),int(sonuclar[2])
    return None


while True:
    zaman = input("Şimdi gün/ay/yıl şeklinde tarihi giriniz.:")

    x =  tarih_kontrol(zaman) 
    if x :
        print(x)
        break
    else:
        print("Yeniden yazınız.")
