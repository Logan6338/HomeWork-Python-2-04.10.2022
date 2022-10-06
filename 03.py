# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

number = 8
line = []

for i in range(number):
    line.append(random.randint(100, 1000)/100)

max = float(0)
min = float(1)

for i in line:
    if max < i % 1:
        max = i % 1
    if min > i % 1:
        min = i % 1

print(line)
print(f'{max-min:.2f}')