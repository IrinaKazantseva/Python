# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

numbers = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
unique_numbers = []
for number in numbers:
    if number in unique_numbers:
        continue
    else:
        unique_numbers.append(number)
print(unique_numbers)