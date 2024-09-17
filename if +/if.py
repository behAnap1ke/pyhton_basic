# if a == 'Sharifjon':
#     print('Siz tizimda adminsiz')
# else:
#     print('Sizning logininingiz bazada topilmadi')
# parol = input('parolni kiriting: ')

# if parol == 'admin' or parol == '1234':
#     print('Tizimga xush kelibsiz')
# else:
#     print('Parol xato')
# a = int(input('Son kiriting: '))
# if a > 0:
#     a+=1
# else:
#     a=a
# print(a)


# a = int(input('Son kiriting: '))
# if a > 0:
#     a+=2
# else:
#     a=a
# print(a)


# a = int(input('son kiriting: '))
# if a > 0:
#     a+=1
# elif a < 0:
#     a-=2
# else:
#     a = 10
# print(a)


# a = int(input('son kiriting: '))
# if a > 0:
#     a+=1
# print(a)


# a = int(input('son kiriting: '))
# if a > 0:
#     a+=1
# else:
#     a < 0
# print(a)
    

# a = int(input('son kiriting: '))
# b = int(input('son kiriting: '))
# if a > b:
#     print(a)
# else:
#     b > a
# print(b)


# a = int(input('son kiriting: '))
# b = int(input('son kiriting: '))
# if a < b:
#     print("1 kichik")
# elif a > b:
#     print("2 kichik")
# else:
#     print("hamma si teng")
    

# a = int(input('son kiriting: '))
# b = int(input('son kiriting: '))
# if a > b:
#     print("2 kichik")
# elif a < b:
#     print("1 kichik")
# else:
#     print("hamma si teng")


# a = int(input('son kiriting: '))
# b = int(input('son kiriting: '))
# if a > b:
#     print('togri qildingiz')
# else:
#     a < b
#     print('a katta bolish kerak')


# a = int(input('son kiriting: '))
# b = int(input('son kiriting: '))
# if a == b:
#     a = 0
#     b = 0
# else:
#     a = a + b
#     b = a
# print(a)
# print(b)


# a = int(input('son kiriting: '))
# b = int(input('son kiriting: '))
# if  a == b:
#     ular = 0
# else:
#     ular = (a,b)
# print(a)


# a = int(input('son kiriting: '))
# b = int(input('son kiriting: '))
# c = int(input('son kiriting: '))
# if a > b:
#     print(a)
# elif b > c:
#     print(b)
# else:
#     print(c)


# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# c = int(input("Uchinchi sonni kiriting: "))
# if (a > b and a < c) or (a < b and a > c):
#     qwert = a
# elif (b > a and b < c) or (b < a and b > c):
#     qwert = b
# else:
#     qwert = c
# print(qwert)



# a = int(input("sonni kiriting: "))
# b = int(input("sonni kiriting: "))
# c = int(input("sonni kiriting: "))
# if a <= b and a <= c:
#     kichik = a
# elif b <= a and b <= c:
#     kichik = b
# else:
#     kichik = c

# if a >= b and a >= c:
#     katta = a
# elif b >= a and b >= c:
#     katta = b
# else:
#     katta = c
# print(kichik)
# print(katta)


# a = int(input("sonni kiriting: "))
# b = int(input("sonni kiriting: "))
# c = int(input("sonni kiriting: "))
# if a >= b and a >= c:
#     katta = a
# elif b >= a and b >= c:
#     katta = b
# else:
#     katta = c
    
# if a >= c and a >= b:
#     katt = a
# elif c >= a and c >= b:
#     katt = c
# else:
#     katt = b
# print(katt,katta)



# A = int(input("A sonini kiriting: "))
# B = int(input("B sonini kiriting: "))
# C = int(input("C sonini kiriting: "))

# if A < B < C:
#     A *= 2
#     B *= 2
#     C *= 2
# else:
#     A = -A
#     B = -B
#     C = -C

# print(A,B,C)

# A = int(input("A sonini kiriting: "))
# B = int(input("B sonini kiriting: "))
# C = int(input("C sonini kiriting: "))
# if (A < B < C) or (A > B > C):
#     A *= 2
#     B *= 2
#     C *= 2
# else:
#     A = -A
#     B = -B
#     C = -C
# print(A,B,C)


# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting: "))
# c = int(input("c sonini kiriting: "))
# if a == b and a != c:
#     print("3")
# elif a == c and a != b:
#     print("2")
# elif b == c and b != a:
#     print("1")
# else:
#     print("teng")


# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting: "))
# c = int(input("c sonini kiriting: "))
# d = int(input("d sonini kiriting: "))
# if a == b == c and a != d:
#     print("4")
# elif a == b == d and a != c:
#     print("3")
# elif a == c == d and a != b:
#     print("2")
# elif b == c == d and b != a:
#     print("1")
# else:
#     print("uchta teng son yo'q")

# import math

# a = float(input("A nuqtani kiriting: "))
# b = float(input("B nuqtani kiriting: "))
# c = float(input("C nuqtani kiriting: "))

# ab_distance = abs(a - b)
# ac_distance = abs(a - c)

# if ab_distance < ac_distance:
#     print(f"A nuqtaga eng yaqin nuqta B, ular orasidagi masofa {ab_distance}")
# else:
#     print(f"A nuqtaga eng yaqin nuqta C, ular orasidagi masofa {ac_distance}")

# x = int(input("X ni kiriting: "))
# y = int(input("Y ni kiriting: "))

# if x == 0 and y == 0:
#     print(0)
# elif x == 0:
#     print(2)  
# elif y == 0:
#     print(1) 
# else:
#     print(3)  


# x = int(input("X ni kiriting: "))
# y = int(input("Y ni kiriting: "))

# if x > 0 and y > 0:
#     print("1-chorak")
# elif x < 0 and y > 0:
#     print("2-chorak")
# elif x < 0 and y < 0:
#     print("3-chorak")
# else:
#     print("4-chorak")

# x1, y1 = int( input("1-chi nuqta koordinatalarini kiriting: "))
# x2, y2 = int(input("2-chi nuqta koordinatalarini kiriting: "))
# x3, y3 = int(input("3-chi nuqta koordinatalarini kiriting: "))

# if x1 == x2:
#     x4 = x3
# elif x1 == x3:
#     x4 = x2
# else:
#     x4 = x1

# if y1 == y2:
#     y4 = y3
# elif y1 == y3:
#     y4 = y2
# else:
#     y4 = y1

# print(f"To'rtinchi nuqta: ({x4}, {y4})")

# x = float(input("X ni kiriting: "))

# if x > 0:
#     result = 2 * math.sin(x)
# elif x < 0:
#     result = x - 6
# else:
#     result = "Hisoblanmagan holat"

# print("Funksiya qiymati:", result)

# x = float(input("X ni kiriting: "))

# if x < -2 or x > 2:
#     result = 2 * x
# else:
#     result = -3 * x

# print("Funksiya qiymati:", result)

# x = float(input("X ni kiriting: "))

# if x < 0:
#     result = -x
# elif 0 <= x < 2:
#     result = x ** 2
# else:
#     result = 4

# print("Funksiya qiymati:", result)

# x = float(input("X ni kiriting: "))

# if x < 0:
#     result = 0
# elif 0 <= x < 1 or 2 <= x < 3 or 4 <= x < 5:
#     result = 1
# else:
#     result = -1

# print("Funksiya qiymati:")

# year = int(input("Yilni kiriting: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("366 kun (kabisa yili)")
# else:
#     print("365 kun (kabisa yili emas)")

# number = int(input("Sonni kiriting: "))

# if number > 0:
#     if number % 2 == 0:
#         print("Musbat juft son")
#     else:
#         print("Musbat toq son")
# elif number < 0:
#     if number % 2 == 0:
#         print("Manfiy juft son")
#     else:
#         print("Manfiy toq son")
# else:
#     print("Son nolga teng")

# number = int(input("1-999 oraliqdagi sonni kiriting: "))

# if 1 <= number <= 9:
#     if number % 2 == 0:
#         print("Bir xonali juft son")
#     else:
#         print("Bir xonali toq son")
# elif 10 <= number <= 99:
#     if number % 2 == 0:
#         print("Ikki xonali juft son")
#     else:
#         print("Ikki xonali toq son")
# elif 100 <= number <= 999:
#     if number % 2 == 0:
#         print("Uch xonali juft son")
#     else:
#         print("Uch xonali toq son")
# else:
#     print("Berilgan son oraliqdan tashqarida")

#------------------------------------




# if parol.isalnum():
#     print('num')
#     if parol.islower():
        
#         print('Bu parolda katta harf mavjud emas')
#     else:
#         print(2)
#         if parol.isupper():
#             print('Sizda hamma harf katta va kichik harf qatnashmagan')
#         else:
#             print('Sizning Parolingiz Murakkab',parol)
    