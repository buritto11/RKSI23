#Условие задачи:Дано расстояние L в сантиметрах. Используя операцию деленеия нацело, найти количество полных метров в нем(1 метр = 100см)
#M является обозначением метр и ровняется 100 см
try:
  L = int(input("Введите число в сантиметрах:"))  #Сантиметров
  M = 100  #cm
  S = L // M   #Нахождение целых метров
  if L >= 0:
      print(S, "Метров ")
  else:
      print("Отрицательное число нельзя записывать")
except:
    print("Что-то пошло не так")