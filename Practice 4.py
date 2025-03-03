class Student:  # основной класс Студент
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def display_info(self):
        return f'Имя: {self.name}, Фамилия: {self.surname}, Возраст: {self.age}'

    def fits_conditions(self, conditions):
        return True  # Метод может быть переопределен в дочерних классах


class Bachelor(Student):  # класс БАКАЛАВР
    def __init__(self, name, surname, age, course):
        super().__init__(name, surname, age)
        self.course = course

    def display_info(self):
        return f'{super().display_info()}, Курс: {self.course}'

    def fits_conditions(self, conditions):
        return self.course == conditions.get('course', self.course)


class Master(Student):  # класс МАГИСТР
    def __init__(self, name, surname, age, specialization):
        super().__init__(name, surname, age)
        self.specialization = specialization

    def display_info(self):
        return f'{super().display_info()}, Специализация: {self.specialization}'

    def fits_conditions(self, conditions):
        return self.specialization == conditions.get('specialization', self.specialization)


class Aspirant(Student):  # класс АСПИРАНТ
    def __init__(self, name, surname, age, thesis_topic):
        super().__init__(name, surname, age)
        self.thesis_topic = thesis_topic

    def display_info(self):
        return f'{super().display_info()}, Тема диссертации: {self.thesis_topic}'

    def fits_conditions(self, conditions):
        return self.thesis_topic == conditions.get('thesis_topic', self.thesis_topic)


# Создание списка студентов
students = [
    Bachelor("Иван", "Иванов", 20, 3),
    Master("Петр", "Петров", 25, "Компьютерные науки"),
    Aspirant("Светлана", "Сидорова", 28, "Искусственный интеллект"),
]

# Вывод информации о студентах
for student in students:
    print(student.display_info())

# Поиск студентов по имени или курсу
def search_students(criteria):
    for student in students:
        if student.name == criteria or (isinstance(student, Bachelor) and student.course == criteria):
            print(student.display_info())

search = input("Введите имя или курс для поиска: ")
search_students(search)
