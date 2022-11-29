# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

with open('polynom1.txt', 'r') as data:
    stroka1 = data.readlines()
with open('polynom2.txt', 'r') as data:
    stroka2 = data.readlines()
print(f"Первый многочлен: {stroka1}")
print(f"Второй многочлен: {stroka2}")
with open('polynom3.txt', 'w') as data:
    data.write(f"{stroka1} + {stroka2}")