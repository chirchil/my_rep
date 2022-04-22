# Класс студента
class Student():
    excelent_mark = 5
    good_mark = 4
    grant_for_excelent = 6000
    grant_for_good = 4000
    # Инициализация
    def __init__(self, name: str, surname: str, patronymic: str, age: int, group_num: str, gpa: float):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.age = age
        self.group_num = group_num
        self.gpa = gpa
        self.calculate_grant()

    # Вывести информацию
    def print_info(self):
        print(f"ФИО: {self.surname} {self.name} {self.patronymic} Возраст: {self.age}")

    # Посчитать значение стипендии
    def calculate_grant(self):
        if self.gpa == self.__class__.excelent_mark:
            self.grant = self.__class__.grant_for_excelent
        elif self.__class__.good_mark <= self.gpa < self.__class__.excelent_mark:
            self.grant = self.__class__.grant_for_good
        else:
            self.grant = 0
    
    # Вывести значение стипендии
    def print_grant(self):
        print(f"Стипендия студента с именем {self.surname} {self.name} {self.patronymic} равна {self.grant} рублей")

    # Сравнить стипендии
    def compare_grant(self, obj: object):
        if self.grant < obj.grant:
            print(f"Стипендия у {self.name} меньше, чем стипендия у {obj.name}")
        elif self.grant > obj.grant:
            print(f"Стипендия у {self.name} больше, чем стипендия у {obj.name}")
        else:
            print(f"Стипендии равны")


# Класс магистра
class Graduate(Student):
    grant_for_excelent = 8000
    grant_for_good = 6000
    # Инициализация
    def __init__(self, name: str, surname: str, patronymic: str, age: int, group_num: str, gpa: float, work: str):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.age = age
        self.group_num = group_num
        self.gpa = gpa
        self.work = work
        self.calculate_grant()

   
stud1 = Student('anton', 'shibalov', 'igorevich', 22, '21/421', 5)
stud2 = Graduate('igor', 'shibalov', 'antonovich', 32, '21/422', 5, 'CNN')
stud1.compare_grant(stud2)
stud1.print_grant()
stud2.print_grant()
