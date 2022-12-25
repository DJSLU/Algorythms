"""Сложность: O(n)
Алгоритм считает сыгранны командами матчи.
Количество команд делится пополам.
Если остается одна лишняя команда - она проходит в следующий этап"""


def tournament(n):
    counter = 0  # Счетик сыгранных матчей
    while n != 1:  # Алгоритм будет работать, пока не останется одна команда
        if n % 2 == 0:  # Проверка на четность
            n = n / 2  # Деление команд поровну
            counter += int(n)  # Записываем количество сыгранных матчей
        else:
            counter += int(((n - 1) / 2))
            n = (n - 1) / 2 + 1
    return counter


print(tournament(12))






