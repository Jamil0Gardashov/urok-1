class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Класс: {self.grade}")

student1 = Student("Иван", 15, 9)
student2 = Student("Мария", 16, 10)

student1.display_info()
student2.display_info()
