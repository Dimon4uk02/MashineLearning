import numpy as np

# Створюємо два вектори з довільними дійсними числами
vector1 = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
vector2 = np.array([6.0, 5.0, 4.0, 3.0, 2.0, 1.0])

# Обчислюємо скалярний добуток векторів
scalar_product = np.dot(vector1, vector2)

# Виводимо вектори та скалярний добуток
print("Вектор 1:", vector1)
print("Вектор 2:", vector2)
print("Скалярний добуток:", scalar_product)
