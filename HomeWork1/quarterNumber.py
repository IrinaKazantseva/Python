# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
## Пример:
## - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input("Введите координату по оси Х: "))
y = int(input("Введите координату по оси Y: "))
if x == 0 or y ==0:
    print("Координаты не должны быть равны 0 по условию задачи")
elif x > 0 and y > 0:
    print(f"Точка с координатами ({x},{y}) находится в I четверти")
elif x > 0 and y < 0:
    print(f"Точка с координатами ({x},{y}) находится в IV четверти")
elif x < 0 and y > 0:
    print(f"Точка с координатами ({x},{y}) находится во II четверти")
elif x < 0 and y < 0:
    print(f"Точка с координатами ({x},{y}) находится в III четверти")
