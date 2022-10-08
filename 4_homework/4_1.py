# Вычислить число ПИ c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# d от 0.1 до 0.0000000001

from math import pi

d = float(input("Введите заданную точность числа Pi от 0.1 до 0.0000000001: "))
print(f'd = {d}')
count = 0
while d < 1:
    count += 1
    d = d*10
print(f'π = {round(pi, count)}')