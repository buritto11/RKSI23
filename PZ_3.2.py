vklad = input("Введите сумму вносимого вклада")
procent = 3
y = 0
try:
    vklad = int(vklad)
    if vklad <= 50000:
        y = procent + 1
        print("Процент вносимого вклада равен",y,"%")
    elif vklad >= 50000 and vklad <= 1000000 :
        y = procent + 2
        print("Процент вносимого вклада равен",y,"%")
    elif vklad >= 100000 and vklad <= 1500000 :
        y = procent + 3
        print("Процент вносимого вклада равен",y,"%")
    elif vklad >= 150000 and vklad <= 2000000  :
        y = procent + 4
        print("Процент вносимого вклада равен" ,y,"%")
    else:
        print("Максимальный вклад равен 200000")
except:
    print("Что-то пошло не так")
finally:
    print("Программа закончена")