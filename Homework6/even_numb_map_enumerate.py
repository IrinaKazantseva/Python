# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

numbers = list(map(int, input("Введите числа через пробел: ").split()))
news = []
for index, new in enumerate(numbers):
    if index%2:
        news.append(new)
print(news)
print(sum(news))

