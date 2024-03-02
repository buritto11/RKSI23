# В матрице найти минимальный и максимальный элементы
import random
mat = [[random.randint(-100, 100) for i in range(0,3)] for i in range(0,3)]
print("Исходная матрица:",mat)
mat_max =max([max(i) for i in mat])
mat_min = min([min(i) for i in mat])
print("Максимальный элемент: ",mat_max,"Минимальный элемент: ",mat_min)