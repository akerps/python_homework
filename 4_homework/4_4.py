# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

from random import randint
  
k = int(input("Введите натуральную степень k: "))

path1 = 'pol1.txt'
path2 = 'pol2.txt'

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
