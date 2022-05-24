import numpy as np

#zadanie 1

x = np.arange(4, 84, 4)
print(x)

#zadanie 2

x = [5.0, 6.6, 7.5, 9.25]
y = [np.int32(a) for a in x]
print(y)

#zadanie 3


def fun(n):
    x = np.array([2**i for i in range(1, n*n+1)])
    return x.reshape(n, n)


print(fun(4))

#zadanie 4


def fun(x, y):
    return np.logspace(1, y, num=y, base=x)


print(fun(2, 4))

#zadanie 5

import random

def fun(n):
    y = []
    for x in range(n):
        y.append(random.randint(0, 100))
    y.reverse()
    x = np.diag(y, 2)
    return x


print(fun(3))

#zadanie 6

zad6
malina = np.array(list('malina'))
mrowka = np.array(list('mrówka'))
armata = np.array(list('armata'))
armata = np.flip(armata)

wykreslanka = np.zeros((6,6), dtype='str')

print(wykreslanka)

wykreslanka = np.diag(mrowka)
wykreslanka[:, 0] = malina
#wykreslanka[5,::-1] = armata
wykreslanka[5,:] = armata
print(wykreslanka)
print("")
wykreslanka[:, 0] = mrowka
wykreslanka[5,::-1] = armata
for a in range(5):
    wykreslanka[a,a] = malina[a]
print(wykreslanka)

#zadanie 7


def fun(n):
    a = np.diag([2 for x in range(1, n + 1)])
    p = 4
    for i in range(1, n):
        y = np. diag([p for x in range(1, n+1-i)], i)
        z = np.diag([p for x in range(1, n + 1 - i)], -i)
        a += z + y
        p += 2
    print(a)


fun(3)

#zadanie 8


def podziel(tab, kierunek='poziomo'):
    print(tab)
    if kierunek == 'poziomo':
        # nieparzysta liczba wierszy
        if tab.shape[0] % 2 != 0:
            print("Tablica posiada nieprzystą liczbę wierszy")
            return
        p1 = tab[0:int(tab.shape[0]/2), :]
        p2 = tab[int(tab.shape[0]/2):, :]
        print("***** część 1 *****")
        print(p1)
        print("***** część 2 *****")
        print(p2)
    elif kierunek == "pionowo":
        if tab.shape[1] % 2 != 0:
            print("Tablica posiada nieprzystą liczbę kolumn")
            return
        p1 = tab[:, 0:int(tab.shape[1]/2)]
        p2 = tab[:, int(tab.shape[1] / 2):]
        print("***** część 1 *****")
        print(p1)
        print("***** część 2 *****")
        print(p2)


podziel(np.arange(36).reshape((6,6)), kierunek='poziomo')

#zadanie 9

def n_ty_wyraz(a1, n, r):
    return a1 + (n-1)*r


macierz = np.ones(25, dtype='int32')
print(macierz)
for a in range(0, 25, 1):
    element = n_ty_wyraz(4, a+1, 4)
    macierz[a] = element

macierz = macierz.reshape((5, 5))
print(macierz)
