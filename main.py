# import math
#
# def rownanie_kwadratowe(a,b,c):
#     delta = b**2 - 4 * a * c
#     if delta < 0:
#         print('brak pierwiastków')
#         return -1
#     elif delta == 0:
#         print('jeden pierwiastek')
#         x = (-b)/(2*a)
#         return x
#     else:
#         print('dwa pierwiastki')
#         x1 = (-b - math.sqrt(delta))/(2*a)
#         x2 = (-b + math.sqrt(delta))/(2*a)
#         return x1,x2
#
# print(rownanie_kwadratowe(6,1,3))
# print(rownanie_kwadratowe(1,2,1))
# print(rownanie_kwadratowe(1,4,1))

# import math
#
# def dlugosc_odcinka9(x1=0,y1=0,x2=0,y2=0):
#     return math.sqrt((x2-x1)**2 + (y2-y1)**2)
# #dla argumentów domyślnych
# print(dlugosc_odcinka9())
# # dla argumentów pozycyjnych
# print(dlugosc_odcinka9(1, 2, 3, 4))
# # dwie pierwsze to x1 i y1, przypisywanie wartosci do x2 i y2
# print(dlugosc_odcinka9(2, 2, y2=2, x2=1))

# oznacza dowolną ilość argumentów przechowywanych w krótce
# def ciag(* liczby):
#     if len(liczby) == 0:
#         return 0
#     else:
#         suma = 0
#         for i in liczby:
#             suma += 1
#             return suma
# print(ciag())
#
# print(ciag(1, 2, 3.5, 4, 5, 6, 7))

# def to_lubie (** rzeczy):
#     for cos in rzeczy:
#         print("To jest ")
#         print(cos)
#         print("co lubie")
#         print(rzeczy[cos])
#
# to_lubie(slodycze= 'czekolada', rozrywka = ['gry','filmy'])

# from teksty import litery
#
# a = "Ala ma kota"
#
# litery.wyswietl(a)
# print(litery.dlugosc(a))
#

# Zadanie 1 #
zadanie1="Zadanie 1"
print(zadanie1)

a = [1 - x for x in range(1,11)]
print(a)

b = [4 ** x for x in range(0,8)]
print(b)

c = [x for x in b if x % 2 == 0]
print(c)

znakiod = "-------------------------------------"
print(znakiod)

# Zadanie 2 #

zadanie2 = "Zadanie 2"
print(zadanie2)

import random
listy1 = [random.randint(1, 100) for _ in range(10)]
listy2 = [x for x in listy1 if x % 2 == 0]
print(listy2)

znakiod = "-------------------------------------"
print(znakiod)

# Zadanie 3 #

zadanie3 = "Zadanie 3"
print(zadanie3)

slownik = {'mleko': '1', 'mąka': 'kg', 'jajka': 'sztuki'}
print(slownik)

slownik2 = {key: value for value, key in slownik.items()}
print(slownik2)

znakiod = "-------------------------------------"
print(znakiod)

# Zadanie 4 #

zadanie4 = "Zadanie 4"
print(zadanie4)

def check(a, b, c):
    if a == b == c:
        return 'Trójkąt równoboczny'
    if a >= b and a >= c:
        if a ** 2 == b ** 2 + c ** 2:
            return 'Trójkąt prostokątny'
        else:
            return 'Trójkąt nie jest prostokątny'
    elif b >= a and b >= c:
        if b ** 2 == a ** 2 + c ** 2:
            return 'Trójkąt prostokątny'
        else:
            return 'Trójkąt nie jest prostokątny'
    else:
        if c ** 2 == b ** 2 + a ** 2:
            return 'Trójkąt prostokątny'
        else:
            return 'Trójkąt nie jest prostokątny'


print(check(5, 4, 3))

znakiod = "-------------------------------------"
print(znakiod)

# Zadanie 5 #

zadanie5 = "Zadanie 5"
print(zadanie5)

def polet(a=2, b=4, h=6):
    return ((a + b) * h) / 2

print(polet())

znakiod = "-------------------------------------"
print(znakiod)

# Zadanie 6 #

zadanie6 = "Zadanie 6"
print(zadanie6)

def iloczyn(a = 1,b = 2, ilosc = 5):
    for element in range(a, ilosc):
        print(element * b)

iloczyn(5,5,11)

znakiod = "-------------------------------------"
print(znakiod)

# Zadanie 7 #

zadanie7 = "Zadanie 7"
print(zadanie7)

def funkcja(*liczba):
    if len(liczba) != 3:
        print('Błąd!!! Podaj tylko trzy liczby')

    for element in range(liczba[0], liczba[1]):
        print(element * liczba[1])

funkcja(1,3,4)