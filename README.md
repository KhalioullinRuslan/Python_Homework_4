# Python_Homework_4

***Задача 22:***

Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого списка. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.

11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12


***Задача 24:***

В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.

4 -> 1 2 3 4
9



***Задача RLE***

Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных 
(где только буквы присутствуют для простоты).


***Задача FOOTBALL необязательная***
 Напишите программу, которая принимает на стандартный вход список игр 
 футбольных команд с результатом матча и выводит на стандартный вывод 
 сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

_Формат ввода следующий:_

В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой

*Вывод программы необходимо оформить следующим образом:*
Команда:Всегоигр Побед Ничьих Поражений Всегоочков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

Sample Input: 3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15
Sample Output:

Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
