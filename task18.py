# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6
import random


arrayA = []
N = int(input('N:'))
X = int(input('X:'))

for i in range(0, N):
    RandomNum = round(random.randint(1,N))
    arrayA.append(RandomNum) 
print(arrayA)

num = 0
for i in range(0, len(arrayA)):
    if (arrayA[i] < X) & (arrayA[i] > num):
        num = arrayA[i]

print(num)

num2 = N
for i in range(0, len(arrayA)):
    if (arrayA[i] > X) & (arrayA[i] < num2):
        num2 = arrayA[i]

print(num2)

if (X - num) < (num2 - X):
    print('число:', num, '-ближе всего к Х')
elif (X - num) > (num2 - X):
    print('число:', num2, '-ближе всего к Х')
elif (X - num) == (num2 - X):
    print('число:', num, '-наименьшее число и наиближайших')
 



