#Дано целое число N (32 < N < 126). Вывести символ с кодом, равным N
N = int(input("Введите целое число"))
if N>32 and N<126:
  print(chr(N))
else:
  print("Введите число в диапозоне от 33 до 125 включительно")