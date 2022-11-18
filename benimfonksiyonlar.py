import math

def final_hesapla(vize) :
    if vize < 50:
        final_icin_gerekli_not = ( 50 - 0.4 * vize ) / 0.6
        print("Final için almanız greken not: " , math.ceil(final_icin_gerekli_not))
    else:
        print("Final için almanız gereken not: 50")

def selam_soyle() :
    print("Merhaba")