import numpy as np

# Розмір матриць
n = 3

# Створюємо дві матриці 3x3 з випадковими цілими числами від 1 до 10
matrix1 = np.random.randint(1, 11, (n, n))
matrix2 = np.random.randint(1, 11, (n, n))

# Виводимо матриці
print("Перша матриця:")
print(matrix1)
print("Друга матриця:")
print(matrix2)

# Знаходимо суму елементів діагоналі другої матриці
diagonal_sum = np.trace(matrix2)

# Виводимо суму
print("Сума елементів діагоналі другої матриці:", diagonal_sum)
