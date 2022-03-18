# Класс студента
class Student():
    # Инициализация
    def __init__(self, name: str, surname: str, otch: str, age: int, group_num: str, gpa: float):
        self.name = name
        self.surname = surname
        self.otch = otch
        self.age = age
        self.group_num = group_num
        self.gpa = gpa

    # Получить информацию
    def get_info(self):
        print(f"ФИО: {self.surname} {self.name} {self.otch} Возраст: {self.age}")

    # Получить значение стипендии
    def get_grant(self):
        if self.gpa == 5:
            self.grant = 6000
        elif 4 <= self.gpa < 5:
            self.grant = 4000
        else:
            self.grant = 0
        print(f"Стипендия студента с именем {self.surname} {self.name} {self.otch} равна {self.grant} рублей")

    # Сравнить стипендии
    def compare_grant(self, obj: object):
        self.get_grant()
        obj.get_grant()
        if self.grant < obj.grant:
            print(f"Стипендия у {self.name} меньше, чем стипендия у {obj.name}")
        elif self.grant > obj.grant:
            print(f"Стипендия у {self.name} больше, чем стипендия у {obj.name}")
        else:
            print(f"Стипендии равны")


# Класс магистра
class Graduate(Student):
    # Инициализация
    def __init__(self, name: str, surname: str, otch: str, age: int, group_num: str, gpa: float, work: str):
        self.name = name
        self.surname = surname
        self.otch = otch
        self.age = age
        self.group_num = group_num
        self.gpa = gpa
        self.work = work

    # Получить значение стипендии
    def get_grant(self):
        if self.gpa == 5:
            self.grant = 8000
        elif 4 <= self.gpa < 5:
            self.grant = 6000
        else:
            self.grant = 0
        print(f"Стипендия студента с именем {self.surname} {self.name} {self.otch} равна {self.grant} рублей")


stud1 = Student('anton', 'shibalov', 'igorevich', 22, '21/421', 5)
stud2 = Graduate('igor', 'shibalov', 'antonovich', 32, '21/422', 4, 'CNN')
stud1.compare_grant(stud2)
