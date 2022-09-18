# Задание 1 Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

n = float(input("введите n = "))
n = str(n)
n = n.split('.')
sum = 0
for i in n:
    p = list(i)
    p = [int(i) for i in p]
    for i in p:
        print(i, end = " ")
        sum = sum + i
print('=',sum)

