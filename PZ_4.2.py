# Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от деления определить, имеются ли в записи числа N
# нечетные цифры. Если имеются, то вывести TRUE, если нет -- вывести FALSE.
n = input("Введите целое число: ")
f = True
try:
  n = int(n)
  while n > 0:
    q = n % 10
    n = n // 10
    y = n % 10
    if y % 2 != 0 or q % 2 != 0:
      f = True
      break
    else:
      f = False
  if f == True:
    print(True)
  else:
    print(False)
except:
  print("Что-то пошло не так")