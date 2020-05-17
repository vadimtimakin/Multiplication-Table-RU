# Multiplication table creator  # Создатель таблицы умножения
# (Custom numbers)              # (пользовательские числа)
# [RU]-version                  # Русская версия

import pandas as pd                        # Создание DataFrame(таблицы)
import matplotlib.pyplot as plt            # Вывод таблицы (графически)
import warnings                            # Для отключения предпреждений


def quicksort(array):
    """Быстрая сортировка списка."""
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def get_count():
    """Получение и проверка количества чисел в списке."""
    count = input('Введите количество чисел(натуральное число): ')
    if count.isdigit() is False or float(count) % 1 != 0 or float(count) < 1:
        print('Вы ввели некорректные данные. Попробуйте снова.')
        count = get_count()
    return int(count)


def get_numbers(quantity):
    """Получение и проверка каждого числа в списке."""
    nmbrs = []
    print('\nВводите числа по одному(рациональное число)'
          '\n(некорректные значения учитываться не будут):')
    for keep in range(quantity):
        number = input()
        if number.replace('.', '').isdigit() is False:
            pass
        else:
            nmbrs.append(float(number))
    if not nmbrs:
        print('Вы не ввели корректных чисел. Попробуйте снова.')
        return get_numbers(quantity)
    return nmbrs


def sort_flag(numbers_list):
    """Задание условия сортировки списка."""
    flag = input('Отсортировать введённые числа?'
                 '(0 -нет, 1 - по возрастанию, 2 - по убыванию): ')
    if flag == '0':
        pass
    elif flag == '1':
        numbers_list = quicksort(numbers_list)
    elif flag == '2':
        numbers_list = quicksort(numbers_list)
        numbers_list = numbers_list[::-1]
    else:
        print('\nВвдите корректный ответ.')
        sort_flag(numbers_list)
    return numbers_list


def get_int(my_numbers):
    """Преобразует числа без дробной части в списке в тип Int."""
    for i in my_numbers:
        if i % 1 == 0:
            ind = my_numbers.index(i)
            i = int(i)
            my_numbers[ind] = i
    return my_numbers


print('\n---Создание таблицы умножения---\n')

# Выполнение функций последовательно.

count_numbers = get_count()

numbers = get_numbers(count_numbers)

numbers = sort_flag(numbers)

numbers = get_int(numbers)

# Создание (генерация)  двух словарей и объедение их в один с целью получения
# словаря, в котором первая пара key & value будет создавать
# первый столбец таблицы с перемножаемыми числами (value = numbers).

# Создание словаря, опеределяющего DataFrame перемноженных чисел.
mydict = {str(num):
          [str(int(i*num)) if (i*num) % 1 == 0 else i*num for i in numbers]
          for num in numbers}

# Создание словаря, определяющего столбец(Series) перемножаемых чисел.
pydict = {'x': [str(int(q)) if q % 1 == 0 else q for q in numbers]}

# Объединение их в один словарь, определяющий весь DataFrame таблицы.
for k, v in mydict.items():
    pydict[k] = v

# Создание DataFrame.
data = pd.DataFrame(pydict,
                    index=[str(i) if i % 1 == 0 else i for i in numbers])

warnings.filterwarnings('ignore')  # Отключение предупреждений

# Создание экземпляра класса figure и его настройка параметров.
param = len(numbers)
fig = plt.figure(figsize=(param+1, param+1), dpi=int(80 - param*2))

ax = fig.add_subplot()
fig.set(facecolor='yellow')

# Создание самой таблицы и настройка её параметров.
the_table = plt.table(cellText=data.values,    # Содержимое ячеек таблицы
                      colLabels=data.columns,  # Названия столбцов таблицы
                      loc='center',            # Выравнивание таблицы в окне
                      cellLoc='center')        # Выравнивание текст внутри ячеек

the_table.auto_set_font_size(False)
the_table.set_fontsize(20)                      # Размер шрифта в таблице
the_table.scale(1, 5)                           # Размер таблицы

# Измение цветов некоторых (крайних) ячеек таблицы.
cell = the_table[0, 0]
cell.set_color('blue')
for i in range(1, len(numbers)+1):
    obj = the_table[0, i]
    obj.set_color('green')
    objct = the_table[i, 0]
    objct.set_color('green')

# Задание названия окну matplotlib.
man = plt.get_current_fig_manager()
man.canvas.set_window_title('Таблица умножения')
# Скрытие осей.
plt.axis('off')
# Отображение таблицы.
plt.show()
