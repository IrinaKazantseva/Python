# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.

n = int(input("Введите число N: "))
numbers = list(range(-n, n+1)) #верно для положительных чисел
print(numbers)

with open('file.txt', 'w') as file:
    for i in range(n*2+1):
        file.write(f'{i}\n')
