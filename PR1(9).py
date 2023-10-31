import numpy as np

# Розмір матриці
n = 4

# Створюємо матрицю 4x4 з випадковими дійсними числами від 0 до 10
matrix = np.random.uniform(0, 10, (n, n))

# Виводимо початкову матрицю
print("Початкова матриця:")
print(matrix)

# Транспонуємо матрицю
transposed_matrix = np.transpose(matrix)

# Виводимо транспоновану матрицю
print("Транспонована матриця:")
print(transposed_matrix)
