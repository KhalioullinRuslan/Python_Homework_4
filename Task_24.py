# Задача 24: 
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

import random

n = int(input('Введите количетство кустов, но не меньше трёх: '))
while n < 3:
    n = int(input('Введите количетство кустов но не меньше трёх: '))
blueber = random.randint(1, 100)
list_blueber = [random.randint(1, 10) for i in range(blueber)]
max_blueber = list_blueber[-1] + list_blueber[0] + list_blueber[1]
for i in range(1, len(list_blueber) - 1):
    temp = list_blueber[i - 1] + list_blueber[i] + list_blueber[i + 1]
    if max_blueber < temp:
        max_blueber = temp
if max_blueber < list_blueber[-1] + list_blueber[-2] + list_blueber[0]:
    max_blueber = list_blueber[-1] + list_blueber[-2] + list_blueber[0]
print(*list_blueber)
print(max_blueber)

# n = int(input('Введите количетство кустов, но не меньше трёх: '))
# lis = [int(x) for x in input().split()]
# n = len(lis)
# lis = lis + lis[:2]
# ma = 0
# for i in range(n):
#     ma = max(ma, lis[i] + lis[i+1] + lis[i+2])
# print(ma)