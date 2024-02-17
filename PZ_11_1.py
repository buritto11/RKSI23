# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Максимальный элемент:
# Произведение элементов меньших 0 в первой половине:
spicok = [12,-4,-6,-23,-55,87]
spicok_print=[]
proiz = 1
f = open('pr11.txt', 'w')
for i in spicok:
  spicok_print.append(str(i))
print(spicok_print)
stroka="Исходные данные: " + ','.join(spicok_print) + '\n'
f.write(stroka)
elements="Количество элементов: " + str(len(spicok)) + "\n"
f.write(elements)
maks_element="Максимальный элемент: " + str(max(spicok)) + "\n"
f.write(maks_element)
for i in spicok[0:len(spicok)//2]:
  if i < 0:
    proiz = proiz * i
    print(proiz)
proiz_pol="Произведение элементов ниже 0 в первой половине: " + str(proiz)
f.write(proiz_pol)
f.close()