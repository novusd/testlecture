# начало первой лекции
print('Start')
print('Исправляем ошибки')
# Работа с консолью можно запускать из гит или загрузить питон в консоли
# 2 + 2, - , * , **, /, //, %
# Операции сравнения < > == !=
# Вещественные числа
# Разные нотации (Записи) 0.5 или .5(американская нотация)
# Важно понимать что вещественные числа храняться в интерпретаторе с округлением. Пример:
# print(0.1561513215123156121511515121512151) # смотреть вывод на консоли число будет короче
# print(1/3)
# print(0.3 + 0.3 + 0.3 + 0.1)
# # не путать null и none !
#
# # Строки: сложение(+), умножение(*), стравнение(<, <=, >, >= , ==)
# print('abcd' > 'abcd')
# print('abcd' >= 'abcd')
# print('abce' > 'abcd')
# print('abcc' > 'abcd')
# # поддержка символов зависист от поддержки определенного юникода, пайтон хранит в себе практически все символы которые
# # существуют в мире (UTF8 наиболее распространенная таблица символов)
# # (https://ru.wikipedia.org/wiki/%D0%AE%D0%BD%D0%B8%D0%BA%D0%BE%D0%B4)
# print('hello'.encode())
# print('Привет'.encode())
# print(b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'.decode())
# # нужно для перевода "сырых" файлов в читаемый код. Например (.exe, dump)
# print(b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'.decode('utf8'))  # по умолчанию стоит UTF8
# print(b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'.decode('cp1251')) # кодировка для старых драйверов
# # Болеее подробно будем разбирать при создании и запаковки файлов
#
# # Индексация строк. Смотреть таблицу "helpa"
# print('qwertyu'[0])
# print('qwertyu'[-2])
# print('qwertyu'[2:4])
# print('qwertyu'[2:-1])
# print('qwertyu'[-3:-1])
# print('qwertyu'[:4])
# print('qwertyu'[2:])
# print('qwertyu'[:])
# print('qwertyu'[:4] +'qwertyu'[4:])
# print('qwertyuiopasdfghjkl'[0:20:2])
# print('qwertyuiopasdfghjkl'[0:20:-2])
# print('qwertyuiopasdfghjkl'[::-1])
# print(len('qwertyuiopasdfghjkl'))
#
# # Переменные, "ярлык" для объектав в области оперативной памяти, динамическая типизация
# # не может начинаться с числа. Python язык высокого уровная ( иногда сверх высокого), присутвует автоматический сборщик
# # мусора. как только теряется ссылка(яралык) на обьект он автоматически удаляется
# car = 'skoda'
# print(len(car))
# print(car[-1])
# print(car[::-1])
# my_car = car
# print(my_car)
# # Множественное присвоение
# x, y = 10, 20
# # Динамическая типизация
# print(id(car))
# print(id(car) == id(my_car))
#
# # Методы строк
# print(car.find('a'))
# print(car.replace('a', 'o'))
# print(car.upper())
# print(car.lower())
# print(car.isalpha())  # все ли символы в строке буквы
# print(car.isnumeric())  # все ли числа

# txt = "one one was a race horse, two two was one too."
# x = txt.replace("one", "three")
# print(x)

# Списки

# a = 'hello'
# my_list = list(a)
# my_list = [a]
# print(my_list)
#
# my_list_1 = [1, 2, 3, 4, 5, 6]
# print(my_list)
# #
# my_list.append(1)  # добавить список
# print(my_list)
# a = my_list[1]
# print(a)
#
#
# word = 'qwertuyiopfjgkfgjdfjgbfd'
# print(len(word))
# print(word[1:4])
# b = word[1:4]
# a = word[1:12:2]
# print(a)
# c = word[1:20:4]
# print(c)
# my_list = [a, b, c]
# print(my_list)
# my_list.insert(1, my_list_1)
# print(my_list[1])
# h = my_list[1]
# print(h[1])
#
# my_list = [1, 3, 5, 6, 7, 8, 90, 4, 3, 2, 67, 8, 9]
# # my_list.sort()
# print(my_list)
# print(len(my_list))
# print(my_list[12])

# my_tuple = (23, 34)

# my_list = [2, 'hello', 'hello world', 520]
# print(my_list)
# spisok = list('555gfd69jhgk')
# print(spisok)
# a = int(spisok[0])
# b = int(spisok[1])
# print(a+b)
# print(spisok)

# my_list = [1, 2, 3, 4, 5]
# my_list_2 = [7, 8, 9, 10]
# print(my_list)
# print(my_list_2)
# my_list.append(6)
# print(my_list)
# my_list.extend(my_list_2)
# print(my_list)
# a = my_list[0:9:2]
# print(a)
#
# my_list = [4,7,5,6,1,0,9,3,2,0,9,5,6,4,8,7,3,2,6,7,6,2,8,5,7,8,9]
# my_list.sort()
# print(my_list)
# my_list[1] = 1
# print(my_list)
# tuple_1 = tuple('hello')
# print(tuple_1)
# # tuple_1.append(6)
# tuple_1[1] = 2
# print(tuple_1)
# my_tuple = (0, 0, 1, 2, 2, 2, 3, 9)
# print(my_tuple)
# # # my_tuple[1] = 1
# # # print(my_tuple)
# my_tuple_list = list(my_tuple)
# print(my_tuple_list)
# my_tuple_list[1] = 1
# print(my_tuple_list)
# my_tuple = tuple(my_tuple_list)
# print(my_tuple)

my_dict = {'hello': 1, 'world': 2, 'word': 5, 12: '20'}
# print(my_dict)
# print(my_dict['hello'])
# a = dict(((1,(1,2)), (2,2), (3,3)))
# print(a)
# b = a[1]
# print(b[0] + b[1])
# my_dict['hello'] = 'world'
# print(my_dict)
# # b = len(my_dict['hello'])
# # print(b)
# c = my_dict['hello']
# print(c[0])
# print(my_dict.keys())
# my_list = [1, 2, 3, 4, 5]
# my_list_1 = ["Имя", 3, 4, 5]
# print(f'Рост {my_list_1[0]} = {my_list[2]}cm')
# a = set('hellogakwclfjhdsgvhgjhggvhjgjhjhjhjgkhjjhgj')
# c = set('sjdhgfhsdvfjsdfjdsjfhjhsdfdsjhfghsjfsdjfjsfj')
# print(a)
# print(c)
# b = {5, 6, 8, 9, 7, 7, 2, 5, 5, 5}
# print(b)
# print(a.intersection(c))