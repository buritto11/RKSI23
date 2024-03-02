# В матрице найnи сумму отрицательных элементов в первой трети матрицы
import random
mat = [[random.randint(-100, 100) for i in range(0,3)] for i in range(0,3)]
print("Исходная матрица:",mat)
mat_otr_sum = sum([sum([t for t in i if t<0]) for i in mat])
mat_otr_sum_tret = sum([i for i in mat[0] if i<0])
print("Сумма отрицательных элементов в первой трети: ",mat_otr_sum_tret)