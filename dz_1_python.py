# # # Создать переменную типа string
# my_string = 'Hello Python '
# print(my_string)
# print(type(my_string))
# # Создать переменную типа integer
# param = 12
# print(param)
# print(type(param))
# # Создать переменную типа float
# param_1 = 3.14
# print(param_1)
# print(type(param_1))
# # создать переменную типа bytes
# b = bytes('john travolta','utf-8')
# print(b)
# print(type(b))
# # создать переменную типа list
# spisok = ['cat','dog','bird']
# print('cat','dog','bird')
# print(type(spisok))
# # создать переменную типа tuple
# kortezh = ('12','dragon','777',)
# print(kortezh)
# print(type(kortezh))
# # создать переменную типа set
# Set = {234234,'john wick','bond007'}
# print(Set)
# print(type(Set))
# # создать переменную типа frozen set
# set_1 = {12,23,34,34}
# fz = frozenset(set_1)
# print(fz)
# print(type(fz))
# # создать переменную тип dict
# word ={'word_1': 1, 'word_2': 2}
# print(word)
# print(type(word))
# # Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
# parametr = 'James '
# parametr_1 = 'Bond'
# parametr_2 =(parametr+parametr_1)
# print(parametr_2)
# # Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
# znak_1 = 10
# znak_2 = 35
# znak_3 = (znak_1 + znak_2)
# print(znak_3)
# # Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.
# znak_4 = (znak_2 / znak_1)
# print(znak_4)
# # Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.
# znak_5 = (znak_1 * znak_2)
# print(znak_5)
# # Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.
# znak_6 = (znak_2 // znak_1)
# print(znak_6)
# # Создать переменную в которой надо присвоить остаток от деления этих переменные Int. Вывести в консоль
# znak_7 = (znak_2 % znak_1)
# print(znak_7)
# # Создать 2 переменных типа String с разными значениями
# name = 'John'
# surname = 'Wick'
# # Создать 4 переменных типа Integer с разными значениями
# a = 5
# b = 10
# c = 15
# d = 20
# # Создать 3 переменных типа Float с разными значениями
# var_1 = 3.6
# var_2 = 7.5
# var_3 = 9.2
# # Реализовать варианты сравнения int переменных с операторами >, <, >=, <=, !=. Pезультаты вывести в консоль
# a_1 = a > b
# print(a_1)
# a_2 = a < b
# print(a_2)
# a_3 = b = a
# print(a_3)
# a_4 = c >= d
# print(a_4)
# a_5 = d != a
# print(a_5)
# a_6 = a <= d
# print(a_6)
# a_7 = a >= b
# print(a_7)
# # Реализовать  варианты сравнения Float переменных с операторами >, <, >=, <=, !=. Pезультаты весвести в консоль.
# varik = var_3 > var_1
# print(varik)
# varik_1 = var_2 == var_1
# print(varik_1)
# varik_2 = var_3 != var_2
# print(varik_2)
# varik_3 = var_2 < var_1
# print(varik_3)
# varik_4 = var_3 <= var_2
# print(varik_4)
# varik_5 = var_1 >= var_3
# print(varik_5)
# # Реализовать  варианты сравнения int переменных с операторами >, <, >=, <=, != и условными выражениями (end, or, not). Pезультаты вывести в консоль.
# w_1 = a < b and b > c
# print(w_1)
# w_2 = b <= c or c != b
# print(w_2)
# w_3 = a < b
# print(not 'a < b')
# # Сделать скрипт используя функцию input().
# #     1. Функция должна на вход принимать целое число.
# #     2. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) 30"
# x = int(input())
# y = int(30)
# if x < y:
#     print("вы ввели число = ",x, "которое < 30")
# elif x > y:
#     print("вы ввели число = ",x, "которое > 30")
# elif x == y:
#     print("вы ввели число = ",x, "которое равно 30")
#Сделать скрипт используя функцию input().
#Сделать скрипт используя функцию input().
 # 1. Функция должна на вход принимать целое число.
 #  2. Внутри функции должно сгенерироваться рандомное целое число (import random)...(random.randint(1, 100))
 #   3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) сгенерированному числу"
# import random
#
# cs = int(input())
# cs_1= random.randint(1,100)
# if cs > cs_1:
#     print('Вы ввели число= ', cs,'которое больше', cs_1)
# elif cs < cs_1:
#     print('Вы ввели число= ', cs,'которое меньше', cs_1)
# elif cs == cs_1:
#     print('Вы ввели число= ', cs,'которое равно', cs_1)
tuf = int(input())
import random

tuf_1 = random.randint(1,100)
tuf_2 = random.randint(1,100)
if tuf < tuf_1 and tuf > tuf_2:
    print('Вы ввели число= ', tuf,'которое меньше', tuf_1, 'и больше ', tuf_2)
elif tuf > tuf_1 and tuf < tuf_2:
    print('Вы ввели число= ', tuf,'которое больше', tuf_1, 'и меньше ', tuf_2)
elif tuf == tuf_1 and tuf < tuf_2:
    print('Вы ввели число= ', tuf,'которое равно', tuf_1, 'и меньше ', tuf_2)
elif tuf == tuf_1 and tuf > tuf_2:
    print('Вы ввели число= ', tuf,'которое равно', tuf_1, 'и больше ', tuf_2)
elif tuf > tuf_1 and tuf > tuf_2:
    print('Вы ввели число= ', tuf,'которое больше', tuf_1, 'и больше ', tuf_2)
elif tuf < tuf_1 and tuf < tuf_2:
    print('Вы ввели число= ', tuf,'которое меньше', tuf_1, 'и меньше ', tuf_2)