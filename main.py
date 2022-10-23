import numpy as np
from numpy import linalg

row = int(input("Введите размерность квадратной матрицы от 1 и до 31: "))

while row < 1 or row > 31:
    row = int(input("Неверное число!\nВведите размерность квадратной матрицы от 1 и до 31: "))
x = np.random.randint(5, size=(row, row))
rank = np.linalg.matrix_rank(x)

print("Матрица:\n", x)
print("Ранг матрицы:", rank)

t = int(input("Введите количество знаков после запятой при вычислении неточности: "))
t = 0.1 ** t

n = 1
factorial, res = 1, 1
summa, bef = 0, 0

while abs(res) > t:
    bef += summa
    summa += (np.linalg.det(linalg.matrix_power(x, 3 * n - 1))) / factorial
    n += 1
    factorial = factorial * (3 * n - 1) * (3 * n - 2)
    res = abs(bef - summa)
    bef = 0
    print(n - 1, ':', summa, ' ', res)
print("Сумма знакопеременного ряда:", summa)
