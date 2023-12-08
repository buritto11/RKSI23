#AMean = (X+Y)/2 и средне геометрическое GMean = y/X Y двух положительных чисел X и Y.
#С помощью этой функции найти среднее арифметическое и средне геометрическое для пар (A,B),(A,C),(A,D), если даны A,B,C,D.
def Mean(X,Y):
  try:
    X = int(X)
    Y = int(Y)
  except:
    print("Введен неправельный параметр")
  else:
    AMean = (X+Y)/2
    GMean = Y/X
    print(AMean,"средне арифметическое",GMean,"средне геометриское для пары",X,Y)


A,B,C,D=input("").split()
Mean(A,B)
Mean(A,C)
Mean(A,D)