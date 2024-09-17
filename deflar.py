# 31
# def ispilindrom(n):
#     if n > 0:
#         return True
#     else:
#         return False
#
#
# a = int(input("a ni kiriting"))
# b = int(input("b ni kiriting"))
# d = int(input("d ni kiriting"))
# e = int(input("e ni kiriting"))
# c = int(input("c ni kiriting"))
#
# a1 = ispilindrom(a)
# b1 = ispilindrom(b)
# c1 = ispilindrom(c)
# d1 = ispilindrom(d)
# e1 = ispilindrom(e)
#
# print(a1, b1, c1, d1, e1)


# 32
# import math
#
# def radius(d):
#     return d * (math.pi / 180)
#
#
# d = int(input("kirit blyat"))
#
# d1 = radius(d)
#
# print(d1)


# 33

# import math
#
# def radius(d):
#     return d * (math.pi / 180)
#
#
# d = int(input("kirit blyat"))
# a = int(input("kirit blyat"))
# c = int(input("kirit blyat"))
#
# d1 = radius(d)
# a1 = radius(a)
# c1 = radius(c)
#
# print(d1, a1, c)


# 34

# def ispilindrom(n):
#     if n > 0:
#         return True
#     else:
#         return False
#
#
# a = int(input("a ni kiriting"))
# b = int(input("b ni kiriting"))
# d = int(input("d ni kiriting"))
# e = int(input("e ni kiriting"))
# c = int(input("c ni kiriting"))
#
# a1 = ispilindrom(a)
# b1 = ispilindrom(b)
# c1 = ispilindrom(c)
# d1 = ispilindrom(d)
# e1 = ispilindrom(e)
#
# print(a1, b1, c1, d1, e1)


# 35

# def fact2(n):
#     qwerty = 1
#     while n > 0:
#         qwerty *= n
#         n -= 2
#     return qwerty
#
#
# a = [4, 8, 7]
# b = [fact2(b) b in a]
# print(fact2(a))


# 36

# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     a, b = 1, 1
#     for _ in range(3, n + 1):
#         a, b = b, a + b
#     return b
#
#
# a = [4, 7, 3]
# qwerty = [fib(number) for number in a]
# print(qwerty)

# 37
# def powera1(a, b):
#     return a ** b
#
#
# a1 = 1345
# a2 = 646
# b = 4
#
# q = powera1(a1, b)
# w = powera1(a2, b)
#
# print(q, w)


# 38

# def power2(a, n):
#     if n == 0:
#         return 1
#     elif n > 0:
#         return a ** n
#     else:
#         return 1 / (a ** n)
#
# n = 2
# a = 123
# b = 1234
# a1 = power2(a, n)
# b1 = power2(b, n)
# print(a1, b1)


# 39

# def power2(a, n):
#     if b == 0:
#         return 1
#     elif b > 0:
#         return a ** b
#     else:
#         return 1 / (a ** b)
#
# a = 123
# b = 21
# a1 = power2(a, b)
# print(a1)

# 40

# def exp1(x, s, a, n, b):
#     a = a * x / n
#     b += a
#     return exp1(x, s, a, n, b)
#
#
# a = 234
# b = 1234
#
# a1 = exp1(a, 3, 4, 5)
# b1 = exp1(a, 3, 4, 5)
#
# print(a1, b1)


# 41

# def sin1(a, b, c=None, d=0, e=0):
#     if c is None:
#         c = a
#     if abs(c) < b:
#         return e
#     else:
#         e += c
#         c = -c * a * a / ((2 * d + 2) * (2 * d + 3))
#         return sin1(a, b, c, d + 1, e)
#
# a = 1.0
# b1 = 0.1
# b2 = 0.01
# b3 = 0.001
# b1 = sin1(a, b1)
# b2 = sin1(a, b2)
# b3 = sin1(a, b3)
# print(b1)
# print(b2)
# print(b3)


# 42

# def cos1(a, b, c=None, d=0, e=0):
#     if c < b:
#         return e
#     else:
#         e += c
#         c = -c * a * a / ((2 * d + 1) * (2 * d + 2))
#         return cos1(a, b, c, d + 1, e)
#
#
# a = 21
# b1 = 21
# b2 = 1
# b3 = 4
#
# b1 = cos1(a, b1)
# b2 = cos1(a, b2)
# b3 = cos1(a, b3)
#
# print(b1, b2, b3)


# 43


# def ln1(a, b, c=None, d=0, e=0):
#     if c < b:
#         return e
#     else:
#         e += c
#         return ln1(a, b, c, d, e)
#
#
# a = 1.5
# b1 = 32
# b2 = 21
# b3 = 12
#
# b1 = ln1(a, b1)
# b2 = ln1(a, b2)
# b3 = ln1(a, b3)
#
# print(b1, b2, b3)


# 44

# def arctg(c=None, d=0, e=0):
#     if c < b:
#         return e
#     else:
#         e += c
#         c *= -a**2 / (2*d - 1)
#         return arctg(a, b, c,)
#
#
# a = 212
# b = 21
#
# a1 = arctg(a, b)
#
# print(a1)


# 45

# def powera4(a, b):
#     return a ** b
#
#
# a1 = 1332345
# a2 = 12
# b = 1
#
# q = powera4(a1, b)
# w = powera4(a2, b)
#
# print(q, w)


# 46

# def ekub(a,b):
#     return a//b
#
# a = 23456
# b = 42
#
# a1 = ekub(a, b)
# print(a1)


# 47


# def ekub(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#
# a = 32
# b = 12
#
# a1 = ekub(a)
# b1 = ekub(b)
#
#
# print(a1, b1)


# 48

# import math
# def ekuk(a, b):
#     return (a * b) // math.gcd(a, b)
#
# a = 23
# b = 43
#
# print(ekuk(a, b))


# 49


import math

# def ekuk(y, d):
#     return y // d
#
# a = 32.0
# b = 32.5
# c = 21.9
#
# d = 2
#
# a1 = ekuk(a, d)
# b1 = ekuk(b, d)
# c1 = ekuk(c, d)
#
#
# print(a1, b1, c1)


# 50


# def time(h, m, s, t):
#     return h*60+m*60
#
#
# h = 12
# m = 21
# s = 21
# t = 32
#
#
# print(time(h, m, s, t))


# 51

# def time(h, m, s, t):
#     return h*60+m*60+s*60
# h = 12
# m = 21
# s = 21
# t = 32
#
#
# print(time(h, m, s, t))


# 52


# def isleap(x):
#     if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
#         return True
#     else:
#         return False
#
# year = [2000, 2001, 1900, 2024, 2100]
#
# for y in year:
#     print(y)


# 53

# def isleap(m, y):
#
#     day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#     if m == 2 and isleap(y):
#         return 29
#     else:
#         return day[m - 1]
#
#     y = 1999
#     m1 = 2
#     m2 = 4
#     m3 = 18
#
#     print(isleap(m1, y))


# 54


# def months(d, m, y):
#     if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
#         return True
#     else:
#         return False
#     day = [31, 29, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#
# d = int(input("Enter day:  "))
# m = int(input("Enter month:  "))
# y = int(input("Enter year:  "))
#
# print(months(d, m, y))


# 55

# def month(d, m, y):
#     if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
#         return True
#     else:
#         return False
#     day = [31, 29, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#     if d < day:
#         d += 1
#     else:
#         d = 1
#         if m == 12:
#             m = 1
#             y += 1
#         else:
#             m += 1
#
#
# d = int(input("Enter day:  "))
# m = int(input("Enter month:  "))
# y = int(input("Enter year:  "))
#
#
# print(month(d, m, y))


# 56
# import math

# def legn(x1, y1, x2, y2):
#     return math.sqrt((x2-x1)**2 + (y2-y1))
#
# x1 = float(input("enter x coordinate: "))
# y1 = float(input("enter y coordinate: "))
# x2 = float(input("enter x coordinate: "))
# y2 = float(input("enter y coordinate: "))
#
#
# print(legn(x1, y1, x2, y2))
#
#
#
# #57


import math


# def Leng(X1, Y1, X2, Y2):
#     return math.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2)
#
#
# def Perim(XA, YA, XB, YB, XC, YC):
#     AB = Leng(XA, YA, XB, YB)
#     BC = Leng(XB, YB, XC, YC)
#     CA = Leng(XC, YC, XA, YA)
#
#     return AB + BC + CA
#
#
# # Test qilish
# XA, YA = 0, 0
# XB, YB = 3, 0
# XC, YC = 0, 4
#
# print(Perim(XA, YA, XB, YB, XC, YC))


#58


import math


# def Leng(X1, Y1, X2, Y2):
#     return math.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2)
#
#
# def Perim(XA, YA, XB, YB, XC, YC):
#     AB = Leng(XA, YA, XB, YB)
#     BC = Leng(XB, YB, XC, YC)
#     CA = Leng(XC, YC, XA, YA)
#
#     return AB + BC + CA
#
#
# # Test qilish
# XA, YA = 0, 0
# XB, YB = 3, 0
# XC, YC = 0, 4
#
# print(Perim(XA, YA, XB, YB, XC, YC))



#60


# import math
#
# def leng(X1, Y1, X2, Y2):
#     return math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
#
# def area(XA, YA, XB, YB, XC, YC):
#     return (XA * (YB - YC) + XB * (YC - YA) + XC * (YA - YB)) / 2
#
# def dist(XA, YA, XB, YB, XP, YP):
#     AB_length = leng(XA, YA, XB, YB)
#     spab = area(XA, YA, XB, YB, XP, YP)
#     if AB_length == 0:
#         return 0
#     return (2 * spAB) / AB_length
#
# XA, YA = 0, 0
# XB, YB = 4, 0
# XP, YP = 2, 3
#
# print(dist(XA, YA, XB, YB, XP, YP))






