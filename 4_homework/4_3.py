# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

from random import randint
myList = [randint(0, 9) for i in range(randint(5, 10))]
print(f'Изначальная последовательность => {myList}')

resultList = []

for i in myList:
    count = 0
    for j in myList:
        if i == j:
            count += 1
    if count == 1:
        resultList.append(i)
print(f'Список неповторяющихся элементов => {resultList}')