# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

n = int(input('Введите размер списка: '))
line1 = []
line2 = []
for i in range(n):
    line1.append(random.randint(0,10))

if len(line1) % 2 == 0:
    l = int((len(line1) / 2))
else:
    l = int((len(line1)/2)+1)

for i in range(l):
    line2.append(line1[i]*line1[-(i+1)])

print(line1)
print(line2)