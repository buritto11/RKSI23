#Туристические агенства предлагают следующие туры. Вояж-Мексика,Канада,Израиль,Италия.
#РейнаТур-Англия,Япония,Канада,ЮАР. Определить:
#1. какие туры из Вояж, отсутствуют в РейнаТур
#2. какие товары из РейнаТур, отсутствуют в Вояж
#3. перечень одинаковых туров
#4. равны ли перечни туров
Вояж = {"Мексика","Канада","Израиль","Италия"}
РейнаТур = {"Англия","Япония","Канада","ЮАР"}
print(Вояж - РейнаТур)
print(РейнаТур - Вояж)
print(Вояж & РейнаТур)
print(Вояж == РейнаТур)