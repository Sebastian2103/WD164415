import numpy as np
import math

#ZADANIE 1

# a = np.arange(3)
# b = np.array([10,20,30])
#
# c = a*b
# print(c)

#ZADANIE 2

# a2 = np.arange(5, 5*9+1, 5).reshape((3, 3))
# b2 = np.arange(16).reshape((4, 4))

# print(np.amin(a2, axis=0))
# print(np.amin(a2, axis=1))
# print(np.amin(b2, axis=0))
# print(np.amin(b2, axis=1))


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

# print (a+b)

#ZADANIE 8
#
# a = np.arange(9).reshape((3,3))
# for i in a:
#     print(i)

#ZADANIE 9

# a = np.arange(9).reshape((3,3))
# for i in a.flat:
#     print(i)
# zadanie 10

# w = np.arange(81).reshape((9, 9))
# print(w)

# w = np.reshape(w, newshape=(27,3))
# print(w)

# w = np.reshape(w, newshape=(81,1))

# wielkość macierzy musi się zgadzać z ilością elementów dlatego w przykładzie 9 * 9 = 81 = 27 * 3


# zadanie 11

# o = np.arange(12).reshape((3, 4))
# o2 = np.reshape(o, newshape=(4, 3))
# o3 = np.reshape(o, newshape=(2, 6))

# for i in o.flat:
#     print(i)

# for i in o2.flat:
#     print(i)

# for i in o3.flat:
#     print(i)

# wyniki są takie same
