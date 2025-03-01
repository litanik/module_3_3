# 1. Функция с параметрами по умолчанию:
# Создаем функцию print_params(a = 1, b = 'строка', c = True),
# которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True)
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()  # Вывод значений параметров
print('--------------------------------')

# Вызываем функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params(2, 'столбец', False)
print_params(3, 'None')
print_params(a='один', b='два', c='три')
print_params(a='один', b='два')
print_params(b='два', c='три')
print_params(a='один', c='три')
print_params(a='один')
print_params(b='два')
print_params(c='три')
print_params()  # Вывод функции без аргументов
print('--------------------------------')

# Проверяем, работают ли вызовы print_params(b = 25) и print_params(c = [1,2,3])
print_params(b=25)
print_params(c=[1, 2, 3])
print('--------------------------------')

# 2. Распаковка параметров:
# Создаем список values_list с тремя элементами разных типов.
values_list = [9.8, 'const', True]
# Создаем словарь values_dict с тремя ключами, соответствующими
# параметрам функции print_params, и значениями разных типов.
values_dict = {'a': 'else', 'b': False, 'c': 0}
# Передаем values_list и values_dict в функцию print_params,
# используя распаковку параметров (* для списка и ** для словаря).
print_params(*values_list)
print_params(**values_dict)
print('--------------------------------')


# Можно передавать вот так (список создаётся локально, мы не влияем на его изменение вне функции)
def append_to_list(item, values_list=None):
    if values_list is None:
        values_list = []
        values_list.append(item)


print_params(*values_list)
print('--------------------------------')

# 3. Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка']  # Создаем список values_list_2 с двумя элементами разных типов
print_params(*values_list_2, 42)  # Проверяем, работает ли print_params(*values_list_2, 42)
