# Составить список, в которой будут включены только согласные буквы и привести их к верхнему регистру.
# Список ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
spicok = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
sogl = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩбвгджзйклмнпрстфхцчшщ"
spicok_sogl = [[t.upper() for t in i if t in sogl] for i in spicok]
print("Список букв верхнего регистра:",spicok_sogl)