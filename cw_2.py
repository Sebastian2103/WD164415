
#Zadanie1

ulubione_sporty=['piłka_nozna','tenis_stołowy','pływanie']
ulubione_sporty.reverse()
print(ulubione_sporty)
ulubione_sporty.append('golf')
print(ulubione_sporty)

#Zadanie2

slownik={'itp':'i tym podobne','faq':'czesto zadawane pytania','asap':'jak najszybciej'}
print(slownik['itp'])
print(slownik['faq'])
print(slownik['asap'])

#Zadanie3

ulubione_gry={'TWW2':'Total War Warhammer 2','HM&M5':'Heroes Might & Magic 5','W3DG':'Wiedźmin 3 Dziki Gon','C6':'Civilization 6'}
print(len(ulubione_gry))

#Zadanie4

b= input('Wpisz zdanie')
print(b.count('a'))

#Zadanie5

a=input("podaj pierwsza liczbe")
b=input("podaj druga liczbe")
c=input("podaj trzecia liczbe")
a=int(a)
b=int(b)
c=int(c)
d= a**b+c
print(d)

#Zadanie6

a=input("podaj pierwsza liczbe")
b=input("podaj druga liczbe")
c=input("podaj trzecia liczbe")
a=int(a)
b=int(b)
c=int(c)
if (a>b)&(a>c):
    print(str(a)+" jest najwieszką liczbą")
elif (b>a)&(b>c):
    print(str(b)+"jest najwiekszą liczba")
else:
    print(str(c)+"jest najwiekszą liczba")

#Zadanie7

list=[4,4.5]
for a in list:
    a=a**2
    print(a)

#Zadanie8

list=[]
a=1
while (a<11):
    print(a)
    a+=1
    if (a%2==0):
        list.append(a)
print(list)

#Zadanie9

import math
a=input("wpisz liczbe")
a=int(a)

if (a<0):
    print("Nie Da sie wykonać pierwiasktkowania, liczba jest ujemna")
else:
    print(math.sqrt(a))





