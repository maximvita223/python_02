# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

num = int(input('Введите число: '))
product_of_numbers = 1
for i in range(1,num+1):
    product_of_numbers*=i
    print(product_of_numbers)