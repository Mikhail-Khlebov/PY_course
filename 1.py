
# семинар
# задача 1
# 20

# задача 2
# people1 = int(input ("Введите кол-во учащихся в первом классе: "))
# people2 = int(input ("Введите кол-во учащихся в первом классе: "))
# people3 = int(input ("Введите кол-во учащихся в первом классе: "))

# class1 = (people1 + 1)//2
# class2 = (people2 + 1)//2
# class3 = (people3 + 1)//2

# print("Всего парт необходимо: ", class1 + class2 + class3)

# задача 5
# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.

# i = int(input("Ввидите номер вагона по билету Витя: "))
# j = int(input("Ввидите номер вагона который указан в поезде: "))
# if i == j:
#     print("Чтобы посчитать кол-во вагонов инфы не достаточно")
# else:
#     print(f"кол-во вагон: {i + (j - 1)}")

"""
print(n)
print(n)
print(n)
print(n)
"""
# a = 5
# b = 2.56
# c = 'Hello'

# print("{} - {} - {}".format(a,b,c))
# print ('Vvedite chto-to:')
# a = int(input())
# b = int(input('введите второе число: '))

# print(a, ' + ', b, ' = ', a + b)

# a = 5.89956
# b = 6.55611
# print(round(a*b, 3))

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура это Маша!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Миша':
#     print('Миша такой Миша')
# else:
#     print('Привет, ', username)

# from math import ceil

# Семинар №1
# s = int(input("Введите расстояное: "))
# n = int(input("Введите скорость:"))

# # print(ceil(s/n))3
# print((s+(n-1))//n)

# задача №3
# import  math
# first_class = int(input("Введите количество учеников 1 кл"))
# second_class = int(input("Введите количество учеников 2 кл"))
# thid_class = int(input("Введите количество учеников 3 кл"))

# print(math.ceil(first_class / 2) + math.ceil(second_class / 2) + math.ceil(thid_class / 2))

# задача №5
# import  math

# i=int(input("введите номер от головы i="))
# j=int(input("введите номер вагона j="))

# if i==j:
#     print("не могу сказать")
# else:
#     print(i+j-1)

# Задача №7. Решение в группах
# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# year = int(input("Введите год:"))

# if year%400==0 or year%100!=0 and year%4==0:
#     print("YES")
# else:
#     print("NO")
# ДЗ
# n = 123 -> res = 6 (1 + 2 + 3)

# n = 100 -> res = 1 (1 + 0 + 0)

# 

# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

# n = int(input('Введите число больше 1: '))

# count = 1
# fib1 = 0
# fib2 = 1
# temp = 0

# while fib2 <= n:
#     temp = fib1
#     fib1 = fib2
#     fib2 += temp
#     count += 1
# if n == fib1:
#     print(count)
# else:
#     print(-1)
    
# n = int(input("Введите число больше 1:"))

# count = 4
# fib1 = 1
# fib2 = 1
# fib_res = 2

# while fib_res < n:    
#     fib1 = fib2
#     fib2 = fib_res
#     fib_res = fib2 + fib1
#     count += 1

# if fib_res == n:
#     print(count)
# else:
#     print(-1)

# Пользователь вводит число N (1 ≤ N ≤ 10). 
# Далее построчно N чисел от -50 до 50. 
# Нужно вывести наибольшее количество идущих подряд положительных 
# чисел.
# 1
# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2
# import random

# num = int (input("Введите кол-во дней: "))
# count = 0
# max_count = 0
# for i in range(num):
#     temp = random.randint(-50, 50)
#     print(temp, end= " ")
#     if temp <= 0:
#         count += 1
#         if max_count < count:
#             max_count = count
#     else:
#         count = 0
# print()
# print(max_count)
# 2
# import random

# num = int(input("Введите кол-во дней от 1 до 10: "))
# count = 0
# max_count = 0

# for i in range(num):
#     temperature = random.randint(-50, 50)
#     print(temperature, end= " ") 
#     if temperature > 0:
#       count += 1      
#     else:
#        if max_count < count:
#         max_count = count
#        count = 0

# if max_count < count:
#     max_count = count       
# print()       
# print(max_count)

# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!

# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# from random import randint

# count = input("Введение кол-ва чисел:")

# max_num = 0
# min_num = 1000

# for _ in range(count):
#     current_num = randint(1, 10)
#     print(current_num, end=" ")
#     if max_num < current_num:
#         max_num = current_num
#     if min_num > current_num:
#         min_num = current_num
# print()
# print(min_num, max_num)
# 1
# from random import randint

# count = int(input("Введите количество чисел"))

# max_num = 0
# min_num = 1000

# for _ in range(count):
#     current_num = randint(1, 10)
#     print(current_num, end=" ")
#     if max_num < current_num: 
#         max_num = current_num
#     if min_num > current_num:
#         min_num = current_num
        

# print()
# print
# 2
# from random import randint


# count = int(input("Введите количество чисел"))
# current_num = randint(1, 10)
# max_num = current_num
# min_num = current_num

# for _ in range(count - 1):
#     current_num = randint(1, 10)
#     print(current_num, end=" ")
#     max_num = max(max_num, current_num)
#     min_num = min(min_num, current_num)
        

# print()
# print(min_num, max_num)

# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# from random import randint

# size = int (input('Ввидите размер списка: '))
# # list_1 = []
# # for _ in range(size):
# #     list_1.append(randint(-5,5))
    
# list_2 = [randint(-5,5) for _ in range(size)]
# print(list_2)
# # uniq_symbolse_nums = set(list_2)
# # print(len(uniq_symbolse_nums))
# print(len(set(list_2)))
# print(len(set([randint(-5,5) for _ in range(size)])))

# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# from random import randint

# list_1 = [i for i in range(1,randint(7,10))]
# print (list_1)

# k = int(input('введите число: '))
# # print(list_1.pop())
# # for _ in range(k):
# #     last_el = list_1.pop()
# #     list_1.insert(0, last_el)
# # print(list_1)
# print(list_1[-k:] + list_1[:-k])

# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# 1
# list_dicts = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "},
#               {" VIII ":" S007 "}]

# uniq_symbolsue_values = set()

# for cur_dict in list_dicts:
#     for key in cur_dict:
#         uniq_symbolsue_values.add(cur_dict[key].strip())
        
# print(uniq_symbolsue_values)

# # 2
# list_dicts = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "},
#               {" VIII ":" S007 "}]

# uniq_symbolsue_values = set()

# for cur_dict in list_dicts:
#     for key in cur_dict.keys():
#         uniq_symbolsue_values.add(cur_dict[key].strip())
        
# print(uniq_symbolsue_values)

# Задача №23. Общее обсуждение
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# array = [0, -1, 5, 2, 3]
# count = 0

# for i in range(len(array) -1):
#     if array[i] < array[i + 1]:
#         count += 1
# print(count)

# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# text = ('a a a b c a a d c d d')
# list_symbols = text.split()
# print(list_symbols)
# uniq_symbols = dict()
# print(uniq_symbols)
# for symbol in list_symbols:
#     if symbol not in uniq_symbols:
#        uniq_symbols[symbol] = 0
#        print(symbol, end=" ")
#     else:
#         uniq_symbols[symbol]+=1
#         print(f"{symbol}_{uniq_symbols[symbol]}", end=" ")
    # print(uniq_symbols)


# 2
# text="a a a b c a a d c d d"
# list_symbols=text.split()
# print(list_symbols)
# uniq_symbols=dict()
# print()
# result=""
# for symbol in list_symbols:
#     if symbol not in uniq_symbols:
#         result+=f"{symbol} "
#     else:
#         result+=f"{symbol}_{uniq_symbols[symbol]} "
#     uniq_symbols[symbol]=uniq_symbols.get(symbol,0)+1
# print(result.strip())

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea"
# list_words = text.lower().split()
# set_words = set(list_words)
# print(len(set_words))
# print(len(set(text.lower().split())))

# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих
# слайдах

# n = int(input())
# max_number = -1
# while n > 0:
#     if max_number < n:
#         max_number = n
#     n = int(input())
# print(max_number)

# n = int(input())
# max_number = n
# while n != 0:
#     n = int(input())
#     if max_number < n:
#         max_number = n
# print(max_number)

# Петя:
# n = int(input())
# max_number = -1
# while n > 0:                         # 1)while n < 0:
#     if max_number < n:
#        max_number=n                  # 3)n = max_number
#     n = int(input())                 # 2)был на 73 строке
# print(max_number)                    # 4) print(n)


# n = int(input())
# max_number = n                   # 1) некорректное число max_number = 1000 
# while n != 0:
#    n = int(input())
#    if max_number < n:           # 2) max_number > n:
#        max_number = n
# print(max_number)

# Задача №35. Общее обсуждение
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# def prime_num(num):
#     if num != 2 and num % 2 == 0:
#         return False
#     for div in range(3,int(num ** 0.5) + 1, 2):
#         if num % div == 0: 
#             return False
#     return True

        
# num=int(input("Введите число: "))
# print(prime_num(num))

# Задача №37. Решение в группах
# 15 минут
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def revers_nums(n):
#     if n == 0:
#         return ' '
#     k = int(input("Vveditte chisla:"))
#     return f'{revers_nums(n-1)} {k}'
    
    
# num = int(input("Введите числа: "))
# print (revers_nums(num))


# def reverse_nums(n):
#     if n == 1:
#         return ' '
#     k = int(input("Введите число последовательности: "))
#     return f'{reverse_nums(n-1)} {k}'


# num = int(input('Введите количество чисел: '))
# print(reverse_nums(num))

# [выражение for val in коллекция]
# [вырадение for val in коллекция if условие]
# import random
# a = [random.randint(-10,10) for i in range(10)]
# print(a)
# b = [elem+1 for elem in a]
# print(b)

# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:             Вывод:
# 7                 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1    (каждое число вводится с новой строки)

# from random import randint

# size_1 = int(input('введите размер массива первого:'))
# size_2 = int(input('введите размер массива второго:'))

# list_1 = []
# list_1 = [randint(0, 5) for i in range(size_1)]
# print(list_1) 

# list_2 = []
# list_2 = [randint(0, 5) for i in range(size_2)]
# print(list_2)  

# set_2 = set(list_2)
# for el in list_1:
#     if el not in set_2:
#         print(el, end= '')

# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод:         Ввод:
# 5             5
# 1 2 3 4 5     1 5 1 5 1
# Вывод:        Вывод:
# 0             2

# from random import randint
# size_list=10
# list_1=[randint(1,50) for _ in range(size_list)]
# print(list_1)

# count=0

# for i in range(1, size_list-1):
#     if list_1[i-1]<list_1[i]>list_1[i+1]:
#         count+=1
# print(count)

# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:         Вывод:
# 1 2 3 2 3 2    2

# from random import randint

# size = int(input('введите размер массива: '))
# list_1=[randint(0,5) for _ in range(size)]
# print(list_1)

# counter = 0

# for i in range(size-1):
#     counter += list_1[i+1:].count(list_1[i])
# print(counter)

# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105.
# Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:       Вывод:
# 300         220 284

# def div_sum(number):
#     sum_divs = 1
#     for i in range(2, number):
#         if number%i == 0:
#             sum_divs += i
#     return sum_divs


# size = int(input('Введите предельное число К: '))

# for num_1 in range(size):
#     for num_2 in range(size):
#         if div_sum(num_1) == num_2 and div_sum(num_2) == num_1 and num_1 < num_2:
#             print(num_1, num_2)