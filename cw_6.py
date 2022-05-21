import numpy as np
import math

#ZADANIE 1

# a = np.arange(3)
# b = np.array([10,20,30])
#
# c = a*b
# print(c)

#ZADANIE 2

a = np.array([[3, 7, 5], [6, 1, 9], [2, 7, 8]])
b = np.array([[5, 1, 6, 8], [3, 6, 2, 7], [9, 3, 7, 5], [4, 4, 2, 1]])

print(a)
print(b)

print(np.amin(a, axis=0))
print(np.amin(a, axis=1))
print(np.amin(b, axis=0))
print(np.amin(b, axis=1))


#ZADANIE 3

# c1 = a.dot(b)

#ZADANIE 4

# a = np.array([1.2,1.3,1.7])
# b = np.array([4,5,6])
# c = a*b
# print(c)

#ZADANIE 5

# a = np.array([1,2,3,4,5,6]).reshape((2,3))
#
# c = np.sin(a)
# print(c)

#ZADANIE 6
# a = np.array([1,2,3,4,5,6]).reshape((2,3))
# #
# # c = np.cos(a)
# # print(c)

#ZADANIE 7

# dodawanie = np.add(a,b)
# print(dodawanie)

#ZADANIE 8
#
# a = np.arange(9).reshape((3,3))
# for i in a:
#     print(i)
#     print("")

#ZADANIE 9

# a = np.array([[3, 7, 5], [6, 1, 9], [2, 7, 8]])
# for b in a.flat:
#     print(b)
#     print("")
# zadanie 10

# macierz = np.arange(0,81,1).reshape(9,9)
# print(macierz)
#
# macierz_1 = macierz.reshape(3,27)
# print(macierz_1)
# macierz_2 = macierz.reshape(27,3)
# print(macierz_2)
# macierz_3 = macierz.reshape(81,1)
# print(macierz_3)
# macierz_4 = macierz.ravel()
# print(macierz_4)

# wielkość macierzy musi się zgadzać z ilością elementów dlatego w przykładzie 9 * 9 = 81 = 27 * 3


# zadanie 11

a = np.array([3, 7, 5, 6, 1, 9, 2, 7, 8, 6, 3, 6])
print(a)
macierz_1 = a.reshape(3, 4)
print(macierz_1)
print(macierz_1.ravel())
macierz_2 = macierz_1.reshape(4,3)
print(macierz_2)
print(macierz_2.ravel())
macierz_3 = macierz_1.reshape(2,6)
print(macierz_3)
print(macierz_3.ravel())

# wyniki są takie same
