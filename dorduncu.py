# FUNCTIONS ...

# f(x) = 2*x + 5
# x = 3

# f(x) = 7

# def fx() :
#     print( 2  + 5)

# fx()
# fx()
# fx()
# fx()

# DONT REPEAT YOURSELF DRY

# def f( x ):
#     print( 2 * x + 5 )

# f( 5 )
# f(25)
# f(50)


def diskriminant ( a , b, c ) :
    print( b*b - 4*a*c )

# 2x^2 + 10x -9 = 0
#diskriminant(2,10,-9)

def iki_kati(x):
    return  2 * x
    # return None

# print( iki_kati ( iki_kati( 23 )  )   )


import math

def final_hesapla(vize) :
    if vize < 50:
        final_icin_gerekli_not = ( 50 - 0.4 * vize ) / 0.6
        print("Final için almanız greken not: " , math.ceil(final_icin_gerekli_not))
    else:
        print("Final için almanız gereken not: 50")

# final_hesapla(35)


def iki_kati():
    # global x
    x = 2
    x =   2 * x
    return x

x = 5
# print( iki_kati() )
# x = iki_kati(x)
# print(x)


# varsayılan değerli arguman
# def ussunu_al(sayi=2,us): Hata , çünkü varsayılan değer atanırsa sonrakilerde de varsayılan değer olmalı.

# üssünü eğer yazmazsanız 2 verir...
def ussunu_al(sayi=2,us=2):
    """Fonksiyonla alakalı bilgiler...
    Fonksiyonla alakalı bilgiler...
    Fonksiyonla alakalı bilgiler..."""
    return sayi**us

# print ( ussunu_al(5,3) )
# print ( ussunu_al(5) )
# print ( ussunu_al() )
# print ( ussunu_al(us=5) )


# print()
# print(1 , 5 , 7 )
# print("4545",  333 , "fdsa")


# abc = iki_kati

# print( abc() )


# yazdir = print

# yazdir("Merhaba Dünya")


print("deneme")
ussunu_al(5,7)