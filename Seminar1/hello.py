print("hello world") #string
print(6) #integer
a=b=10
a=a+1
print(b) #10
a=int(input("Введите а "))
if a%2==0:
    print(True) #четное
else:
    print(False) #нечетное
#1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
#*Примеры:*
#- 5, 25 -> да
#- 4, 16 -> да
#- 25, 5 -> да
#- 8,9 -> нет
a=int(input("Введите первое число "))
b=int(input("Введите второе число "))
if b==a*a:
    print("второе число - квадрат первого")
elif a==b*b:
    print("первое число - квадрат второго")
else:
    print("числа не квадраты друг друга")

#2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#Примеры:

#- 1, 4, 8, 7, 5 -> 8
#- 78, 55, 36, 90, 2 -> 90