#Блок 1
# Создайте класс "Студент", который имеет атрибуты имя, фамилия, и оценки.
# Добавьте методы для вычисления среднего балла и определения, является ли студент отличником.
#Блок 3
#Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяет сохранять информацию из экземпляров класса (3 шт.)
#в файл и загружать ее обратно. Использовать модуль pickle для сериализации и десерриализации объектов Python в бинарном формате
import pickle


class Student:
    def __init__(self, name, surname, grade):
        self.name = name
        self.surname = surname
        self.grade = grade

    def grades(self):
        print(self.grade)
        ocenki = sum(self.grade) / len(self.grade)
        print(ocenki)
        if ocenki == 5.0:
            print("Отличник")
        else:
            print("Не отличник")

    def save_def(self):
        with open('student.txt', 'wb') as f:
            pickle.dump(self, f)
            print("Ycpex")

    def load_def(self):
        with open('student.txt', 'rb') as f:
            st = pickle.load(f)
        print(st, st.name, st.surname, st.grade)


student1 = Student('John', 'Smith', [5, 5, 5, 4, 5, 5])
student1.grades()
student1.save_def()
student1.load_def()
