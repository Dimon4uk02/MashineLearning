# Імпортуємо бібліотеку для обчислення факторіалів
import math

# Розмір матриці
n = 3

# Ініціалізуємо порожню матрицю
matrix = [[0] * n for _ in range(n)]

# Заповнюємо матрицю факторіалами чисел плюс їх попередніми значеннями
for i in range(n):
    for j in range(n):
        number = i * n + j + 1
        matrix[i][j] = math.factorial(number) + (number - 1)

# Виводимо матрицю
for row in matrix:
    print(row)
