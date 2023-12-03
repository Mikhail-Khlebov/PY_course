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