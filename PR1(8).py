import numpy as np

# Розмір матриці
n = 3

# Створюємо матрицю 3x3 з випадковими цілими числами від 1 до 15
matrix = np.random.randint(1, 16, (n, n))

# Виводимо початкову матрицю
print("Початкова матриця:")
print(matrix)

# Перевіряємо, чи матриця є невиродженою (має ненульовий детермінант)
if np.linalg.det(matrix) != 0:
    # Знаходимо обернену матрицю
    inverse_matrix = np.linalg.inv(matrix)
    print("Обернена матриця:")
    print(inverse_matrix)
else:
    print("Матриця є виродженою, обернена матриця не існує.")
