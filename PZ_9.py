#Дана строка "Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4".Преобразовать информацию из строки в словарь, найти среднее
#арифметическое оценок, результаты вывести на экран.
stroka = "Петров Иван ПОКС-29 5 4 3 2 5 5 4 4 5 4"
student = {}
ocenki = []
spicok=stroka.split()
student["Фамилия"]=spicok[0]
student["Имя"]=spicok[1]
student["Группа"]=spicok[2]
for i in spicok[3:11]:
  ocenki.append(int(i))
a = sum(ocenki)/len(ocenki)
student["Сред_оценки"]=a
print(student)