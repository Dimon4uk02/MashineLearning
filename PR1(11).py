import numpy as np

# Створюємо матрицю 2x3 з випадковими дійсними числами від 0 до 1
matrix = np.random.rand(2, 3)

# Створюємо вектор з випадковими дійсними числами від 0 до 1
vector = np.random.rand(3)

# Виводимо матрицю
print("Матриця:")
print(matrix)

# Виводимо вектор
print("Вектор:")
print(vector)

# Знаходимо добуток матриці на вектор
result = np.dot(matrix, vector)

# Виводимо результат
print("Добуток матриці на вектор:")
print(result)
