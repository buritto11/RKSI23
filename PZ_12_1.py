#Организовать и вывести последовательность А из n чисел (n - четное). Из последовательности А получить
#две последовательности В и С: в последовательности В - первая половина элементов А, в С - вторая половина элементов А.
# Найти произведение соответствующих элементов последовательностей В и С. Найти среднее арифметической полученной последовательности.
A = [int(input("Введите челое число: ")) for i in range(0,int(input("Введите четное число для длины списка: ")))]
print("Список А",A)
B = [A[i] for i in range(0,len(A)//2)]
print("Первая половина А записанная в В",B)
C = [A[i] for i in range(len(A)//2,len(A))]
print("Вторая половина А записанная в С",C)
res = [x*y for x,y in zip(B,C)]
print("Произведение полученной последовательности", res)
print("Среднее арифметической полученной последовательности",sum(res)/len(res))