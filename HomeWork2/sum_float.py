# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = float(input("Введите вещественное число: "))
sum = 0
for i in str(number):
    if (i != "."):
        sum += int(i)
print(sum)

# s = '0.56'
# summ = 0
# for i in s:
# if i.isdigit():
# summ += int(i)
# print(summ)

# n = float(input('Введите число - '))
# while n % 1 > 0:
# n *= 10
# summ = 0
# while n > 0:
# summ += n % 10
# n //= 10
# print(int(summ))