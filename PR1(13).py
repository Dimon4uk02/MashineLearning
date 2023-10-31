import numpy as np

# Розмір матриць
n = 2

# Створюємо дві матриці 2x2 з випадковими цілими числами від -10 до 10
matrix1 = np.random.randint(-10, 11, (n, n))
matrix2 = np.random.randint(-10, 11, (n, n))

# Виводимо матриці
print("Перша матриця:")
print(matrix1)
print("Друга матриця:")
print(matrix2)

# Знаходимо добуток їх елементів
product = np.prod(matrix1) * np.prod(matrix2)

# Виводимо результат
print("Добуток елементів матриць:", product)
