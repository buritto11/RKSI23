#Сформировать и вывести цнлочисленный список 10, содержащий степени двойки от первой до 10-й: 2,4,8,16,... .
a = 2
r = 0
y = []
for i in range(1,11):
  r = a**i
  y.append(r)
print(y)