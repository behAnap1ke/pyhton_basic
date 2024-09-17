# arraylar  oythonda 4 xil array bor
# list bu barcha turdagi ma`lumotlarni san xohlagandek saqlaydi va bu ma`lumotni xohlaganingcha o`zzgartirishing mumkin
# tuple bu ko`pincha immutible ma`lumot turiga mos keladi ya`niy o`zgarmas ma`lumotlar saqlanadi
# set bu bu m`lumotlarni saralash uchun mos keluvchi data type
# dict bunda ma`lumotlar kalit va qiymatko`rinishida saqlanadi

# -----------------LIST----------------

# sonlar = [1, 2, 3, 4, 5]
# for bilan integratsiyasi
# for i in sonlar:
#     print(i)
# ---------------TUPLE

# mevalar = ("Olma", "Anor", 'Nok')
#
# for i in mevalar:
#     print(i)
# ----------------------listfuction---------------------
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # .append(x)
# # Ro'yxat oxiriga yangi element qo'shadi.
# my_list.append(4)
#
# # .extend(iterable)
# # Ro'yxat oxiriga boshqa iterativ obyekt (masalan, ro'yxat) elementlarini qo'shadi.
# my_list.extend([4, 5, 6])
#
# # .insert(i, x)
# # Berilgan indeksga yangi element qo'shadi.
# # Qolgan elementlar bir qadam o'ngga suriladi.
# my_list.insert(1, 'A')
#
# # .remove(x)
# # Ro'yxatda topilgan birinchi mos keluvchi elementni o'chiradi.
# my_list.remove(2)
#
# # .pop([i])
# # Berilgan indeksdagi elementni olib tashlaydi va uni qaytaradi.
# # Indeks berilmasa, oxirgi elementni qaytaradi.
# my_list.pop()
#
# # .clear()
# # Ro'yxatni tozalaydi, ya'ni barcha elementlarni olib tashlaydi.
# my_list.clear()
#
# # .index(x[, start[, end]])
# # Ro'yxatda berilgan elementning birinchi indeksini qaytaradi.
# # Qidirish uchun boshlanish va tugash indekslarini berish mumkin.
# my_list.index(3)
#
# # .count(x)
# # Ro'yxatda berilgan elementning qancha marta uchrashganini hisoblaydi.
# my_list.count(3)
#
# # .sort(key=None, reverse=False)
# # Ro'yxatni o'sish tartibida saralaydi.
# # Agar reverse=True bo'lsa, kamayish tartibida saralaydi.
# my_list.sort()
#
# # .reverse()
# # Ro'yxat elementlarini teskari tartibda joylashtiradi.
# my_list.reverse()
#
# # .copy()
# # Ro'yxatning nusxasini yaratadi.
# my_list_copy = my_list.copy()
#
# # -------------------tupple----------------
# my_tuple = (1, 2, 3, 4, 5 ,6 ,7 ,8, 9)
# # .count(x)
# # Tuple ichida berilgan elementning necha marta uchrashganini hisoblaydi.
# my_tuple.count(3)
#
# # .index(x[, start[, end]])9749177080
# # Tuple ichida berilgan elementning birinchi indeksini qaytaradi.
# # Qidirish uchun boshlanish va tugash indekslarini berish mumkin.
# my_tuple.index(2)

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a = list1.pop(0)
# print(a)
# set
# birinchi_set = {1, 1, 2, 3, 4, 5, 5}
# birinchi_set.

# lugat = {
#     "meva": "Olma",
#     'Moshina': "BMW",
#     "Son": 2
# }
# print(lugat['meva'])

# for iu in lugat:
#     print(lugat[iu])


# # To'plam yaratish
# my_set = {1, 2, 3}
#
# # 1. add(element): Elementni to'plamga qo'shadi (agar element allaqachon mavjud bo'lmasa).
# my_set.add(4)  # Natija: {1, 2, 3, 4}
#
# # 2. remove(element): To'plamdan elementni o'chiradi. Agar element mavjud bo'lmasa, xato qaytaradi.
# my_set.remove(4)  # Natija: {1, 2, 3}
#
# # 3. discard(element): To'plamdan elementni o'chiradi. Agar element mavjud bo'lmasa, xato qaytarmaydi.
# my_set.discard(3)  # Natija: {1, 2}
#
# # 4. pop(): To'plamdan tasodifiy elementni o'chiradi va uni qaytaradi.
# element = my_set.pop()  # Natija: 1 (yoki 2), my_set: {2} yoki {1}
#
# # 5. clear(): To'plamni bo'shatadi, barcha elementlarni o'chiradi.
# my_set.clear()  # Natija: set()
#
# # 6. union(*others): Berilgan to'plamlar bilan birlashma hosil qiladi.
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# union_set = set1.union(set2)  # Natija: {1, 2, 3, 4, 5}
#
# # 7. intersection(*others): Berilgan to'plamlar bilan kesishmani hosil qiladi.
# intersection_set = set1.intersection(set2)  # Natija: {3}
#
# # 8. difference(*others): Berilgan to'plamlardan farqni hosil qiladi.
# difference_set = set1.difference(set2)  # Natija: {1, 2}
#
# # 9. symmetric_difference(other): Simmetrik farqni (birlashtiruvchi va kesishmani o'chiruvchi) hosil qiladi.
# sym_diff_set = set1.symmetric_difference(set2)  # Natija: {1, 2, 4, 5}
#
# # 10. update(*others): To'plamni berilgan to'plamlar bilan birlashtiradi.
# set1.update(set2)  # Natija: {1, 2, 3, 4, 5}
#
# # 11. intersection_update(*others): To'plamni berilgan to'plamlar bilan kesishma bo'yicha yangilaydi.
# set1.intersection_update(set2)  # Natija: {3, 4, 5}
#
# # 12. difference_update(*others): To'plamni berilgan to'plamlar bilan farq bo'yicha yangilaydi.
# set1.difference_update({3, 4})  # Natija: {5}
#
# # 13. symmetric_difference_update(other): To'plamni berilgan to'plam bilan simmetrik farq bo'yicha yangilaydi.
# set1.symmetric_difference_update({5, 6})  # Natija: {6}
#
# # 14. issubset(other): To'plam boshqa to'plamning kichik to'plami ekanligini tekshiradi.
# is_subset = {1, 2}.issubset({1, 2, 3})  # Natija: True
#
# # 15. issuperset(other): To'plam boshqa to'plamni qamrab olishini tekshiradi.
# is_superset = {1, 2, 3}.issuperset({1, 2})  # Natija: True
#
# # 16. isdisjoint(other): To'plamlar orasida umumiy element yo'qligini tekshiradi.
# is_disjoint = {1, 2}.isdisjoint({3, 4})  # Natija: True
#
# # 17. copy(): To'plamning nusxasini yaratadi.
# copy_set = set1.copy()  # Natija: set1 nusxasi


# Lug'at yaratish
my_dict = {'ism': 'Behruz', 'yosh': 25, 'kasb': 'Dasturchi'}

# 1. keys(): Lug'atning barcha kalitlarini qaytaradi.
kalitlar = my_dict.keys()  # Natija: dict_keys(['ism', 'yosh', 'kasb'])

# 2. values(): Lug'atning barcha qiymatlarini qaytaradi.
qiymatlar = my_dict.values()  # Natija: dict_values(['Behruz', 25, 'Dasturchi'])

# 3. items(): Lug'atning barcha (kalit, qiymat) juftliklarini qaytaradi.
elementlar = my_dict.items()  # Natija: dict_items([('ism', 'Behruz'), ('yosh', 25), ('kasb', 'Dasturchi')])

# 4. get(key, default=None): Berilgan kalit uchun qiymatni qaytaradi; agar kalit mavjud bo'lmasa, `default` qiymatni qaytaradi.
ism = my_dict.get('ism')  # Natija: 'Behruz'
manzil = my_dict.get('manzil', 'Noma’lum')  # Natija: 'Noma’lum'

# 5. pop(key, default=None): Berilgan kalitning qiymatini o'chiradi va uni qaytaradi; agar kalit mavjud bo'lmasa, `default` qiymatni qaytaradi.
yosh = my_dict.pop('yosh')  # Natija: 25, my_dict: {'ism': 'Behruz', 'kasb': 'Dasturchi'}

# 6. popitem(): Lug'atdan tasodifiy (kalit, qiymat) juftligini o'chiradi va qaytaradi (Python 3.7+ da oxirgi elementni qaytaradi).
oxirgi_juftlik = my_dict.popitem()  # Natija: ('kasb', 'Dasturchi'), my_dict: {'ism': 'Behruz'}

# 7. update([other]): Lug'atni boshqa lug'at yoki (kalit, qiymat) juftliklari bilan yangilaydi.
my_dict.update({'manzil': 'Toshkent', 'yosh': 26})  # Natija: {'ism': 'Behruz', 'manzil': 'Toshkent', 'yosh': 26}

# 8. clear(): Lug'atni bo'shatadi, barcha elementlarni o'chiradi.
my_dict.clear()  # Natija: {}

# 9. copy(): Lug'atning nusxasini yaratadi.
my_dict = {'ism': 'Behruz', 'yosh': 25}
my_dict_nusxa = my_dict.copy()  # Natija: {'ism': 'Behruz', 'yosh': 25}

# 10. fromkeys(seq, value=None): Berilgan kalitlar ro'yxati va qiymat bo'yicha yangi lug'at yaratadi.
yangi_dict = dict.fromkeys(['kalit1', 'kalit2', 'kalit3'], 0)  # Natija: {'kalit1': 0, 'kalit2': 0, 'kalit3': 0}

# 11. setdefault(key, default=None): Kalit mavjud bo'lmasa, berilgan `default` qiymat bilan yangi kalit yaratadi va qiymatni qaytaradi.
kasb = my_dict.setdefault('kasb', 'Noma’lum')  # 'kasb' mavjud emas, shuning uchun qo'shiladi. Natija: 'Noma’lum'

# 12. del: Berilgan kalit bo'yicha elementni lug'atdan o'chiradi.
del my_dict['yosh']  # Natija: {'ism': 'Behruz'}



