# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: aaaaaaabbbbbbcccccccccd => 7a6b9c1d или 11a3b7c1d => aaaaaaaaaaabbbcccccccd

str_compression = "aaaaaaabbbbbbcccccccccd"
str_recovery = "11a3b7c1d"

string = ''

def compression(string):
 
    comp_str = "" 
    i = 0
    while i < len(string):
        count = 1
        while i + 1 < len(string) and string[i] == string[i + 1]:
            count += 1
            i += 1
        comp_str += str(count) + string[i]
        i += 1
 
    return comp_str

def recovery(string):
    sum = ''
    recovery_str = ''
    for char in string:
        if char.isdigit():
            sum += char 
        elif char.isalpha():
            recovery_str += char * int(sum)
            sum = ''
    return recovery_str

print(compression(str_compression))
print(recovery(str_recovery))