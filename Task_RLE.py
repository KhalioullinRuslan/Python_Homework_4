# Задача RLE. 
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных 
# (где только буквы присутствуют для простоты).

def encode(s):
 
    encoding = "" # сохраняет выходную строку
 
    i = 0
    while i < len(s):
        # подсчитывает количество вхождений символа в индексе `i`
        count = 1
 
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
 
        # добавляет к результату текущий символ и его количество
        encoding += str(count) + s[i]
        i = i + 1
 
    return encoding
 
 
if __name__ == '__main__':
 
    s = 'AAAABBBCCCCCDEEEEEFFGGGHHHIIIIJJKKKKKLMNNNNOOOPPPQQRRRSTTTTTUUUVVVVVWWXXXXXYZZZZZ'
    print(s)
    print(encode(s))

