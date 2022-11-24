# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

numbers = list(map(int, input("Введите числа через пробел: ").split()))
multiply = []
if len(numbers)%2 == 0:
   for i in range(len(numbers) // 2):
      multiply.append(numbers[i] * numbers[len(numbers) - 1 - i])
else:
   for i in range(len(numbers)//2+1):
      multiply.append(numbers[i]*numbers[len(numbers)-1-i])
print(multiply)