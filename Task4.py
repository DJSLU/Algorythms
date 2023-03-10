'''
Сложность: O(n*log(n)) + O(n) + O(n) ==> O(n*log(n))
Алгоритм находит минимальный модуль (одинаковых) разницы между 2 числами
зписывает значение в виде списка с двумя этими числами
'''

def minimalniamodule(arr):
    arr.sort()  # Применяем сортировку
    para = []  # Создаем список для пар, огромное число для замены и словать
    diff = 10**10  # Создаем, большое число для того чтобы использовать в качестве замены
    dct = {}  # Создаем словать
    for i in range(len(arr) - 1):  # Запускаем цикл по длине списка для поиска минимальной разницы
        diff = min(diff, abs(arr[i] - arr[i + 1]))  # Записываем в diff значение модуля разницы двух соседних чисел
        dct[arr[i]] = 1  # Записываем значение как 1
    dct[arr[-1]] = 1  # Не забываем смотреть тоже последний элемент
    for i in range(len(arr)):  # Запускаем цикл по длине списка
        if arr[i] + diff in dct:  # Если чило + разница есть  в словаре
            para.append([arr[i], arr[i] + diff])  # Добавляем пары у которых разница по модолю равна
    return para  # Возвращаем список пар
print(minimalniamodule([2,4,21,-23,19,6,-50,33]))
