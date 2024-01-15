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


# урок 2
# пустой список:
# list_1 = [] #пустой список
# list_1 = list() #функция лист
# list_1 = [1, 2, 3, 4, 5]
# # print(*list_1) #* звезда убирает скобки и любыее значеения
# # print(len(list_1)) #лен считает колличество в списке
# print(list_1[3])# в кадрат скобка ставим порядковый номер и пункт)

# заполненый список
# list_1 = [1, 2]
# print(list_1)
# list_1.append(8) #апенд позволяет один объект вернуть в конец списка
# print(list_1)
# list_1.append(85) #апенд позволяет один объект вернуть в конец списка
# print(list_1)
# пустой список, добавим данные в список - программа
# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# .pop удаление последнего элемента/но и возвращает
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]

# Удаление конкретного элемента из списка.
# # Надо указать значение индекса в качестве аргумента функции pop:
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
# print(list_1) # [7, -1, 21, 0]

# Добавление элемента на нужную позицию.
# Функция insert — указание индекса (позиции) и значения.
# Метод insert в Python нужен для того, чтобы добавить новый 
# элемент в любое место списка. Метод принимает 
# два параметра: индекс по которому будет вставлен элемент
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11)) #2- это что во второй пункт вставить 11
# print(list_1) # [12, 7, 11, -1, 21, 0]

# Срез списка
# Помните в конце первой лекции Вы прошли 
# срезы строк? Также существует срез
# списка, давайте научимся изменять наш список
# Отрицательное число в индексе — счёт с конца списка
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) #[9, 10]
# print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6]) # [1, 7]
# print(list_1[::6]) # [1, 7]

# Кортеж — это неизменяемый список.
# Тогда для чего нужны кортежи, если их нельзя изменить? В случае защиты
# каких-либо данных от изменений (намеренных или случайных). Кортеж занимает
# меньше места в памяти и работают быстрее, по сравнению со списками
# t = () # создание пустого кортежа
# print(type(t)) # class <'tuple'>
# t = (1,)
# print(type(t))
# t = (28, 9, 1990)
# print(type(t))
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')
# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# for e in t:
# print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support
# # (нельзя изменять кортеж)
# t = [1, 2, 3, 4]
# t[0] = 2
# print(t)

# Словари — неупорядоченные коллекции произвольных объектов с
# доступом по ключу.
# В списках в качестве ключа используется индекс элемента. В словаре для
# определения элемента используется значение ключа (строка, число).
# dictionary = {}
# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться
# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
# # del dictionary['left'] # удаление элемента
# for item in dictionary: 
#     for (k,v) in dictionary.items():
# print('{}: {}'.format(item, dictionary[item]))

# up: ↑
# down: ↓
# right: →
# Словари — неупорядоченные коллекции произвольных объектов с
# доступом по ключу.
# В списках в качестве ключа используется индекс элемента. 
# В словаре для определения элемента используется 
# начение ключа (строка, число).

# d = {}
# d = dict()

# d['q'] = 'qwerty'
# print(d)

# d['w'] = 'werty'
# print(d['w'])

# Множества содержат в себе уникальные элементы, 
# не обязательно упорядоченные.
# Одно множество может содержать значения любых типов. 
# Если у Вас есть два множества, 
# Вы можете совершать над ними любые стандартные операции,
# например, объединение, пересечение и разность. 
# colors = {'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# Операции со множествами в Python
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q =  a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

# Неизменяемое или замороженное множество(frozenset)
# — множество, с которым
# не будут работать методы удаления и добавления.
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

# List Comprehension
# У каждого языка программирования есть свои особенности и преимущества. Одна
# из культовых фишек Python — list comprehension (редко переводится на русский, но
# можно использовать определение «генератора списка»). Comprehension легко
# читать, и их используют как начинающие, так и опытные разработчики.
# List comprehension — это упрощенный подход к созданию списка, который
# задействует цикл for, а также инструкции if-else для определения того, что в итоге
# окажется в финальном списке.

# Урок 3. Функции, рекурсия, алгоритмы
