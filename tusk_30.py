# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

firstMember = int(input("Введите первый член прогрессии: "))
n = int(input("Введите количество элементов: "))
difference = int(input("Введите разницу прогрессии: "))
count = 1

for i in range(n):
    print(firstMember + (count - 1) * difference)
    count += 1

