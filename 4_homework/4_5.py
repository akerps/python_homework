# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0
# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

from random import randint


k = int(input("Введите натуральную степень k: "))

path1 = 'pol1_2.txt'
path2 = 'pol2_2.txt'
result = 'result.txt'

def rand_coef():
    return randint(-100,100)

def create_polymonial(k):
    string = ''
    for i in range(k, -1, -1):
        coef = rand_coef()
        if len(string) == 0 and coef != 0:
            string += f"{coef}*x^{i}"
        elif i not in [0,1] and coef != 0:
            if coef > 0:
                string += f" + {coef}*x^{i}"
            else:
                string += f" - {abs(coef)}*x^{i}"
        elif i == 1 and coef != 0:
            if coef > 0:
                string += f" + {coef}*x"
            else:
                string += f" - {abs(coef)}*x"            
        elif i == 0 and coef != 0:
            if coef > 0:
                string += f" + {coef} = 0"
            else:
                string += f" - {abs(coef)} = 0" 
                         
    return string

with open(path1, 'w', encoding='UTF-8') as data:
    data.write(create_polymonial(k))

with open(path2, 'w', encoding='UTF-8') as data:
    data.write(create_polymonial(k))

# само решение 5 задачи:

def leave_numbers(path):   #убираем все лишнее, оставляем только цифры

    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readline()

    data_file = file.replace(' = 0', '').replace(' + ', ' ').replace(' - ', ' -').replace('*x^', ' ').replace('*x', ' 0').split()
    if len(data_file) % 2 == 1:
        data_file.append('0')
    clear_num = [data_file[i] for i in range(0, len(data_file), 2)] #убираем степени

    for i in range (len(clear_num)):   #переводим список в численный
        clear_num[i] = int(clear_num[i])
    
    print(clear_num)

    return clear_num


path1_list = leave_numbers(path1)   
path2_list = leave_numbers(path2)   
result_list =  [path1_list[i] + path2_list[i] for i in range(len(path1_list))]  

def create_result(pol, k):
    list= pol[::-1]
    string = ''
    for i in range(k, -1, -1):
        if len(string) == 0 and int(list[i]) != 0:
            string += f"{list[i]}*x^{i}"
        elif i not in [0,1] and int(list[i]) != 0:
            if int(list[i]) > 0:
                string += f" + {list[i]}*x^{i}"
            else:
                string += f" - {abs(int(list[i]))}*x^{i}"
        elif i == 1 and int(list[i]) != 0:
            if int(list[i]) > 0:
                string += f" + {list[i]}*x"
            else:
                string += f" - {abs(int(list[i]))}*x"            
        elif i == 0 and int(list[i]) != 0:
            if list[i] > 0:
                string += f" + {list[i]} = 0"
            else:
                string += f" - {abs(int(list[i]))} = 0" 
                                         
    return string

with open(result, 'w', encoding='UTF-8') as data:
    data.write(create_result(result_list, k))