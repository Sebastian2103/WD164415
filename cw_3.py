# import random
# #zadanie1
# a=[1-x for x in range(1,11)]
# print(a)
# b=[4**x for x in range(1,8)]
# print(b)
# c=[x for x in b if x%2==0]
# print(c)

# #zadanie2
# lista1=[]
# for x in range(1,11):
#     lista1.append(random.randint(1,100))
# print(lista1)
# lista2=[x for x in lista1 if x%2==0]
# print(lista2)

# #zadanie3
# slownik={'mleko':'litry','jajka':'sztuki','cukierki':'kilogramy'}
# print(slownik)
# slownik2={value:key for key,value in slownik.items()}
# print(slownik2)

# #zadanie4
# def trojkat(a,b,c):
#     if(a**2+b**2==c**2):
#         print("Trójkąt jest prostokątny")
#         return 1
#     else:
#         print("Trójkat nie jest prostokątny")
#         return 1
# trojkat(3,4,5)
# trojkat(1,1,3)

# # #zadanie5
# def pole_trapezu(a=1,b=2,h=3):
#     if(h==0)&(a==0)&(b==0):
#         print("Niewłaściwe wartości")
#         return -1
#     else:
#         print('Pole trapeu wynosi')
#         return ((a+b)/2)*h
# print(pole_trapezu())
# print(pole_trapezu(10,21,23))

#zadanie6

# def iloczyn(a=1, b=4, ile=10):
#     if a == 0:
#         return 0
#     else:
#         ciag = []
#         for x in range(ile):
#             ciag.append(a*(b**x))
#         print(ciag)
#         iloczyn = 1
#         for x in ciag:
#             iloczyn *=x
#     return iloczyn
#
# print(iloczyn())


#Zadanie7
# def iloczyn(*ciag):
#     if len(ciag) == 0:
#         return 0
#     else:
#         iloczyn = 1
#         for x in ciag:
#             iloczyn *= x
#     return iloczyn
# print(iloczyn())

# Zadanie8
# def zakupy(** pl):
#     print("Wszystkich produktów jest", len(pl.keys()))
#     return sum(pl.values())
#
#
# print(zakupy(chleb=10, cukierki=24, jajka=30))

#Zadanie9

# from ciagi import *
#
# print(ciagi_arytmetyczne.n_wyraz(1,1,20))
# print(ciagi_geometryczne.n_wyraz(1, 5, 4))

