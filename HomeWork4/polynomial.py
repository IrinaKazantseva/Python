# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = int(input("Задайте натуральную степень k = "))
koeflist = [random.randint(0, 101) for i in range(k+1)]

list = koeflist[::-1]
stroka=""
if len(list) < 1:
    stroka = 'x = 0'
else:
    for i in range(len(list)):
        if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
            stroka += f'{list[i]}x^{len(list) - i - 1}'
            if list[i + 1] != 0:
                stroka += ' + '
        elif i == len(list) - 2 and list[i] != 0:
            stroka += f'{list[i]}x'
            if list[i + 1] != 0:
                stroka += ' + '
        elif i == len(list) - 1 and list[i] != 0:
            stroka += f'{list[i]} = 0'
        elif i == len(list) - 1 and list[i] == 0:
            stroka += ' = 0'
print(stroka)

# with open('polynom1.txt', 'w') as data:
#     data.write(stroka)
#
# Для следующей задачи:
with open('polynom2.txt', 'w') as data:
    data.write(stroka)

