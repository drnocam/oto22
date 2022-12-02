def test():
    t = 1
    for i in range(1,10) :
        t = t * i * 2
    return t

print(test())

def x_degistir(x):
    x[0] = x[0]+1

x = [5]
x_degistir(x)
print(x)