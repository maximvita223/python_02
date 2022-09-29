# Реализуйте алгоритм перемешивания списка.
import random

kit = []
for i in range(int(input('Введите количество элементов - '))):
    kit.append(int(input('Введите число - ')))
print('Было',kit)
random.shuffle(kit)
print('Стало',kit)