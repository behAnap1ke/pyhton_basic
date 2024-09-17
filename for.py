# k = 12
# n = 1
# for i in range(n):
#     print(k)

# a = 1
# b = 3
# for i in range(a):
#     print(b)


# a = 1
# b = 6
# for i in range(a -1, b-1):
#     print(i)


# a = 12000
# for i in range(1 ,11):
#     print(i * a)

# a = 12000
# for i in range(1 , 12):
#     print(i * a)


# a = 12000
# for i in range(6):
#     b = 1.2 + i * 0.2
#     c = b * a
#     print(b,c)


# a = 2
# b = 5
# for i in range(a,b + 1):
#     print(a,b)

# a = 2
# b = 5
# for i in range(a,b * 2):
#     print(a,b)


# a = 2
# b = 5
# for i in range(a,b +1):
#     c += i **2
#     print(a,b,c)


# n = 3
# for i in range(n):
#     s += 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1
#     print(s)

# n = 3
# S = 0
# for i in range(n, 2*n + 1):
#     S += i ** 2
# print(S)


# n = 2
# b = 1
# for i in range(1, n + 1):
#     b *= (1 + 0.1 * i)
#     print(b)


# n = 3
# b = 1
# for i in range(1, n + 1):
#     b *= (1 + 1.1 * i)
#     print(b)


# n = 2
# b = 1
# for i in range(1 + 3 + 5 + (2*n -1)):
#     b *= (1 + 1.1 * i)
#     print(b)


# n = 1
# a = 4
# b = 1
# for i in range(n):
#     b *= a
#     print(a,n,b)


# n = 1
# a = 4
# b = 2
# for i in range(n):
#     b *= a
#     print(a,n,b)


# n = 2
# a = 2
# b = 1
# c = 0
#
# for i in range(1, n + 1):
#     b *= a
#     c += b
#     print(b)
# print(b,c,a)


# n = 2
# a = 5
# b = 1
# c = 2
# for i in range(1, n + 1):
#     b *= a
#     c += b
#     print(b)
# print(b,c,a)


# n = 3
# b = 1
# for i in range(1, n+1):
#     b *= i
# print(n ,b)
#
#
# n = 1
# b = 0
# c = 1
# for i in range(1, n+1):
#     c *= i
#     b += c
# print(b)
#
#
# n = 2
# b = 1.0
# c = 1
# for i in range(1, n+1):
#     c *= i
#     b += 1 / c
# print(b)
#
#
# n = 2
# x = 3
# b = 1 + x
# c = 1
# for i in range(2, n+1):
#     b *= i
#     b += (x ** i) / b
# print(f"Сумма: {b}")
#
#
# n = 3
# x = 3
# c = xbl = 1
# sign = -1
# for i in range(1, n+1):
#     b *= (2*i) * (2*i+1)
#     c += sign * (x ** (2*i+1)) / b
#     sign *= -1
# print(c)
#
#
# n = 3
# x = 1
# c = 1
# b = 1
# sign = -1
# for i in range(1, n+1):
#     b *= (2*i-1) * (2*i)
#     c += sign * (x ** (2*i)) / b
#     sign *= -1
# print(c)
#
#
# n = 1
# x = 4
# c = x
# for i in range(2, n+1):
#     c += (-1)**(i-1) * (x**i) / i
# print(c)
#
#
# n = 4
# x = 8
# c = x
# for i in range(1, n):
#     c += (-1)**i * (x**(2*i+1)) / (2*i+1)
# print(c)
#
#
# n = 4
# x = 2
# b = x
# c = 1
# for i in range(1, n+1):
#     c *= 2*i * (2*i+1)
#     b += (x**(2*i+1)) / c
# print(b)
#
#
#
# n = 2
# x = 1
# b = 1
# c = 1
# d = 1
# for i in range(1, n+1):
#     c *= (2*i-1) * 2*i
#     d *= -1
#     b += sign * (x**i) / c
# print(b)
#
#
# n = 3
# a = 1
# b = 6
# d = (b - a) / n
# for i in range(n+1):
#     print(a + i * d)
#
#
# import math
#
# n = 3
# a = 2
# b = 1
# step = (b - a) / n
# for i in range(n+1):
#     x = a + i * step
#     print(x)
#
#
#
# n = 2
# a = 2
# print(a)
# for k in range(1, n):
#     A = 2 + 1/a
#     print(a)
#
#
#
# n = 2
# a = 1
# for i in range(1, n):
#     a = (a + 1) / (i + 1)
#     print(a)
#
#
# n = 2
# a, b = 1, 1
# print(a)
# print(b)
# for i in range(3, n+1):
#     a, b = b, a + b
#     print(b)
#
#
# n = 3
# a1, a2 = 1, 2
# for i in range(3, n+1):
#     a = (a1 + 2*a2) / 3
#     print(a)
#
#
# n = 3
# a1, a2, a3 = 1, 2, 3
# for i in range(4, n+1):
#     a = a3 + a2 - 2*a1
#     print(a)
#
#
# iterator bu siklga mos o`zgaradigan o`zgaruvchi bu
# n = 3
# k = 4
# b = 0
# for i in range(1, n+1):
#     b += i**i
# print(b)
#
#
# n = 9
# b = 0
# for i in range(1, n+1):
#     b += i**i
# print(b)
#
#
# n = 2
# b = 0
# for i in range(1, n+1):
#     b += i**(n-i+1)
# print(b)
#
#
# a = 3
# b = 3
# for i in range(a, b+1):
#     print(i * i)
#
#
# a = 3
# b = 6
# for i in range(a, b+1):
#     print(i * b)
