A = input("Введите целое число")
t = 0
try:
    A = int(A)
    if A % 2 == 0:
        t = A // 2
        print(t)
    else:
        print("Число является нечетным")
except:
    print("Что-то по шло не так")
finally:
    print("Программа закончена")