import numpy as np

# Розмір матриці і вектора
rows = 3
cols = 4

# Створюємо матрицю 3x4 з випадковими дійсними числами від 0 до 1
matrix = np.random.rand(rows, cols)

# Створюємо вектор з випадковими дійсними числами від 0 до 1
vector = np.random.rand(cols)

# Виводимо матрицю
print("Матриця:")
print(matrix)

# Виводимо вектор
print("Вектор:")
print(vector)

# Знаходимо суму елементів матриці
sum_of_matrix_elements = np.sum(matrix)

# Виводимо суму
print("Сума елементів матриці:", sum_of_matrix_elements)
