# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input("Введите число, обозначающее день недели: "))
if a<1 or a>7:
    print("Введите число от 1 до 7")
elif a>=1 and a<=5:
    print("День не является выходным")
else:
    print("Выходной день")