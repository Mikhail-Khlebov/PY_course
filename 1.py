# print('нам нужно ввести первое число: ')
# a = int(input())
# b = int(input('Введите второе число: '))
# print(a, '+', b, '=', a + b)

# c = 1.89
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))

# a = 5.89956
# b = 6.556551
# print(round(a*b, 3))
# round(1.56566, 2)

# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5

# a = 1 > 4
# print(a)
# a = 1 < 4 and 5 > 2
# print(a)
# a = 1 == 2
# print(a)
# a = 1 != 2
# print(a)
# a = 'qwe'
# b = 'qwe'
# print(a == b)
# a = 1 < 3 < 3 < 5 < 10
# print (a)

# username = input ('Напиши имя:')
# if username == 'Маша':
#     print('Ура, это МАША!')
# elif username == 'Марина':
#     print('Марина цветом как малина')
# elif username == 'Гузелл':
#     print('Гузелл возьми себе чупочупс иксиксэл')
# else:
#     print('Привет, ', username)

# a = 'qwerty'
# for i in a:
#     print(i)
# # print (a[2])
 
# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "+"
#         print(line)

# text = 'Съешь еще картофиля и сходи в туалеТ'
# # print(len(text)) #размер страки
# print('еще' in text) #есть ли такое значение true\false

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
# # uniqe_nums = set(list_2)
# # print(len(uniqe_nums))
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

# unique_values = set()

# for cur_dict in list_dicts:
#     for key in cur_dict:
#         unique_values.add(cur_dict[key].strip())
        
# print(unique_values)

# # 2
# list_dicts = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "},
#               {" VIII ":" S007 "}]

# unique_values = set()

# for cur_dict in list_dicts:
#     for key in cur_dict.keys():
#         unique_values.add(cur_dict[key].strip())
        
# print(unique_values)

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

