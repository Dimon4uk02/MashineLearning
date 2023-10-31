import numpy as np

# Розмір масиву
n = 5

# Створюємо два масиви з випадковими дійсними числами від 0 до 1
array1 = np.random.rand(n)
array2 = np.random.rand(n)

# Виводимо початкові масиви
print("Масив 1:", array1)
print("Масив 2:", array2)

# Виконуємо поелементні операції
sum_result = array1 + array2
subtraction_result = array1 - array2
multiplication_result = array1 * array2

# Виводимо результати операцій
print("Додавання:", sum_result)
print("Віднімання:", subtraction_result)
print("Множення:", multiplication_result)
