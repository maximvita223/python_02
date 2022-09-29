# Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода и зависит от количества элементов в списке) в одной строке одно число

N = int(input("Введите число:"))
kit = []
for i in range(-N,N+1):
    kit.append(i)
print(kit)
date = open('position.txt', 'r')
# date.write('3\n')
date.close
kit_2 = date.readlines()
print(kit_2)
sum = 1
for j in kit_2:
    sum*=kit[int(j)]
print(sum)