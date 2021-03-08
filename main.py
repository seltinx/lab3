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

from teksty import litery

a = "Ala ma kota"

litery.wyswietl(a)
print(litery.dlugosc(a))

