#Создайте класс "Человек", который содержит информацию о имени, возрасте и поле.
#Создайте классы "Мужчина" и "Женщина", которые наследуются от класса "Человек". Каждый класс должен иметь метод, который выводит информацию о поле объекта.
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Man(Human):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def mans(self):
        print("Мужчина " + self.name + " " + self.age + " " + self.gender)


class Woman(Human):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def women(self):
        print("Женщина " + self.name + " " + self.age + " " + self.gender)


man1 = Man("Jon", "20", "male")
man1.mans()
woman1 = Woman("Alla", "21", "female")
woman1.women()