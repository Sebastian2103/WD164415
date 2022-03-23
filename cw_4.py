
import random


#Zadanie1
liczby = [random.randint(0,30) for x in range(10)]
mnozenie = [x * 2 for x in liczby]

plik = open('liczby.txt', 'w+')
plik.writelines((str(mnozenie)))
plik.close()

#Zadanie2
plik = open("liczby.txt","r")
dane = plik.readlines()
plik.close()
print(dane)

#Zadanie3
tekst = ["""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam vitae nibh eros.
 Nullam sed mauris sed ex finibus blandit. Nulla sed augue non risus consequat malesuada."""]

with open("eg.txt", "w+") as plik:
    plik.writelines(tekst)

with open("eg.txt", "r+") as plik:
    for x in plik:
        print(x, end="")

#Zadanie4
class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    def wyswietl_produkt(self):
        print("Nazwa: "+ self.nazwa_produktu)
        print("Ilość: " + str(self.ilosc) + " " + self.jednostka_miary)
        print("Cena za 1 " + self.jednostka_miary + ": " + str(self.cena_jed) + " zł")

    def ile_produktu(self):
        print(str(self.ilosc) +" "+ self.jednostka_miary)

    def ile_kosztuje(self, ile):
        return self.cena_jed*ile


Mleko = NaZakupy("Mleko", 10, "l", 3)
Mleko.wyswietl_produkt()
Mleko.ile_produktu()
print(Mleko.ile_kosztuje(10))

#Zadanie5
class CiagiArytmetyczne:

    def __init__(self, wyraz_1, r, ilosc):
        self.wyraz_1 = wyraz_1
        self.r = r
        self.ilosc = ilosc
        self.c = [self.wyraz_1+self.r*(x-1) for x in range(1, self.ilosc+1)]

    def wyswietl_dane(self):
        print(self.c)

    def pobierz_elementy(self, *c):
        self.c = [x for x in c]

    def pobierz_parametry(self, wyraz_1, r, ilosc):
        self.wyraz_1 = wyraz_1
        self.r = r
        self.ilosc = ilosc
        self.c = [self.wyraz_1 + self.r * (x - 1) for x in range(1, self.ilosc + 1)]

    def policz_sume(self):
        return sum(self.c)

    def policz_elementy(self):
        return ((self.c[-1]-self.wyraz_1)/self.r)+1


Ciag1 = CiagiArytmetyczne(2, 2, 6)
Ciag1.wyswietl_dane()
Ciag1.pobierz_elementy(1, 3, 5)
Ciag1.wyswietl_dane()
Ciag1.pobierz_parametry(5, 5, 10)
Ciag1.wyswietl_dane()
print(Ciag1.policz_sume())
print(Ciag1.policz_elementy())

#Zadanie6

class Robaczek():
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok
    def idz_w_gore(self,ile_krokow):
        self.x = self.x + ile_krokow * self.krok
    def idz_w_dol(self,ile_krokow):
        self.x = self.x - ile_krokow*self.krok
    def idz_w_lewo(self,ile_krokow):
        self.y = self.y - ile_krokow*self.krok
    def idz_w_prawo(self,ile_krokow):
        self.y = self.y + ile_krokow*self.krok
    def pokaz_gdzie_jestes(self):
        return print(self.x , self.y)

robaczek = Robaczek(0,0,5)

robaczek.idz_w_dol(2)
robaczek.idz_w_prawo(4)
robaczek.idz_w_prawo(10)
robaczek.idz_w_gore(11)
robaczek.pokaz_gdzie_jestes()
