# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input("Введите число: "))

fib = [1, 0, 1]
while len(fib) < n*2+1:
    fib.insert(0, fib[1] - fib[0])
    fib.append(fib[-1] + fib[-2])
print(fib)





