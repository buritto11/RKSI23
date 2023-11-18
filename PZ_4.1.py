# Даны два целых числа A и B (A > B). Вывести в порядке убывания все целые числа, расположены между A и B (не включая числа A и B),
# а также количество N этих чисел.
a = input("Введите верхнюю границу")
b = input("Введите нижнюю границу")
while type(a) != int:
  try:
    a = int(a)
  except ValueError:
    print("Введите число а не строку в переменной a")
    a = input("")

while type(b) != int:
  try:
    b = int(b)
  except ValueError:
    print("Введите число а не строку в переменной b")
    b = input("")

n = 0
while b+1<a:
  a = a -1
  n = n +1
  print(a)
print("Количество цифр в цикле", n)
