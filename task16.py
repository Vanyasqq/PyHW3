# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 1

# 1 2 1 2 2
# Вывод: 2

import random

N = int(input('введите число:'))
x = round(random.randint(1,N/2))
print('x=',x)
array = []
count = 0

for i in range(0, N):
    RandomNum = round(random.randint(1,N/2))
    array.append(RandomNum) 
print(array)

for i in range(0, len(array)):
    if array[i] == x:
        count +=1

print(count)