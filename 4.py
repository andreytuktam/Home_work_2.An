# Задание 4 Задайте список из N элементов, заполненных числами 
# из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

n = int(input("введите n = "))
a = int(input("введите a = "))
b = int(input("введите b = "))
mas = []
for i in range(-n, n + 1):
    mas.append(i)  
print(mas)   
print("произведение значений mas на позициях a и b = ", mas[a] * mas[b])

