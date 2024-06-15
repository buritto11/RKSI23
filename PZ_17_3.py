#Задание предполагает, что у студента есть проект с практическими работами (№№ 2-13),
#оформленный согласно требованиям. Все задания выполняются c использованием модуля
#OS:
# перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
#вложенных подкаталогов выводить не нужно.
# перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
#test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
#Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
#файлов в папке test.
# перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
#консоль. Использовать функцию basename () (os.path.basename()).
# перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
#привязанной к нему программе. Использовать функцию os.startfile().
# удалить файл test.txt.
import os
import subprocess, sys

opener = "open" if sys.platform == "darwin" else "xdg-open"


# Определение базового пути к проекту
base = '/home/student/Документы/Архипов ИС-27/Prog_Архипов/'
basepath = base + 'PZ_11'
test = base + 'test'
test1 = base + 'test/test1'

# Переход в каталог PZ11 и вывод списка файлов
os.chdir(basepath)
print('Текущая директория:', os.getcwd())
print('Список файлов в PZ11:', os.listdir(basepath))

# Создание папок test и test1
os.makedirs(test, exist_ok=True)
os.makedirs(test1, exist_ok=True)

# Перемещение файлов из PZ6 и PZ7
# os.replace(base + 'PZ_6/PZ_6.1.py', test + '/PZ_6.1.py')
# os.replace(base + 'PZ_6/PZ_6.2.py', test + '/PZ_6.2.py')
# os.replace(base + 'PZ_7/PZ_7.1.py', test1 + '/test.txt')

# Вывод информации о размере файлов в папке test
list_dir = os.listdir(test)
print('Список файлов в test:', list_dir)
for i in list_dir:
    print(i)
    razmer = os.path.getsize(os.path.join(test, i))
    print(f'Размер {i}: {razmer} байт')

# Нахождение файла с самым коротким именем в PZ11
os.chdir(basepath)
print('Текущая директория:', os.getcwd())
pz_11_list = os.listdir(basepath)
shortest_file = min(pz_11_list, key=len)
print('Файл с самым коротким именем:', shortest_file)

# Запуск PDF-файла
os.chdir(basepath)
for filename in os.listdir(basepath):
    if filename.endswith(".pdf"):
        subprocess.call([opener, os.path.join(basepath, filename)])
        break

# Запуск PDF-файла
os.chdir(basepath)
for filename in os.listdir(basepath):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(basepath, filename)
        if os.path.exists(pdf_path):
            subprocess.call([opener, pdf_path])
            break

# Удаление файла test.txt
# os.remove(test1 + '\\test.txt')