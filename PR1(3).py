import numpy as np

# Розмір матриці
n = 9

# Створюємо матрицю з випадковими цілими числами від -5 до 5
matrix = np.random.randint(-5, 6, (n, n))

# Знаходимо суму модулів елементів матриці
sum_of_abs = np.sum(np.abs(matrix))

# Виводимо матрицю
print("Матриця:")
print(matrix)

# Виводимо суму модулів елементів
print("Сума модулів елементів:", sum_of_abs)
