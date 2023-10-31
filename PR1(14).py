import numpy as np

# Розмір матриці
n = 10

# Створюємо матрицю 10x10 з випадковими цілими числами від 1 до 100
matrix = np.random.randint(1, 101, (n, n))

# Виводимо матрицю
print("Матриця:")
print(matrix)

# Знаходимо найбільший елемент матриці
max_element = np.max(matrix)

# Виводимо найбільший елемент
print("Найбільший елемент матриці:", max_element)
