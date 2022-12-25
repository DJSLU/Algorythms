"""Сложность: О(n)
Алгоритм ищет совпадения в строках и прибавляет единицу если найдено совпадение"""
def numJewelsInStones(jewels, stones):
    count = 0  # Переменная счётчик
    for i in stones:  # Проходим по строке
        if i in jewels: # Пррверяем есть ли подстрока в строке
            count += 1  # Если есть к счётчику добавляем 1
    return count  # Возвращаем ответ

print(numJewelsInStones('z', 'zzz'))