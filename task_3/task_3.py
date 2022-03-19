# Класс фигуры
class Figure:
    # Сравнить площади
    def compare_area(self, obj: object):
        self.get_area()
        obj.get_area()
        if self.area > obj.area:
            print(f"Фигура '{self.name}' имеет большую площадь, чем фигура '{obj.name}'")
        elif self.area < obj.area:
            print(f"Фигура '{self.name}' имеет меньшую площадь, чем фигура '{obj.name}'")
        else:
            print("Площади фигур равны")

    # Сравнить периметры
    def compare_perimeter(self, obj: object):
        self.get_perimeter()
        obj.get_perimeter()
        if self.perimeter > obj.perimeter:
            print(f"Фигура '{self.name}' имеет больший периметр, чем фигура '{obj.name}'")
        elif self.perimeter < obj.perimeter:
            print(f"Фигура '{self.name}' имеет меньший периметр, чем фигура '{obj.name}'")
        else:
            print("Периметры фигур равны")


# Класс прямоугольника
class Rectangle(Figure):
    # Инициализация
    def __init__(self, a: float, b: float, name: str = "Rectangle"):
        self.a = a
        self.b = b
        self.name = name

    # Получить площадь
    def get_area(self):
        self.area = self.a * self.b
        print(f"Площадь фигуры с именем '{self.name}' равна {self.area}")

    # Получить периметр
    def get_perimeter(self):
        self.perimeter = 2 * (self.a + self.b)
        print(f"Периметр фигуры с именем '{self.name}' равен {self.perimeter}")


# Класс Квадрата, наследуемый от прямоугольника
class Square(Rectangle):
    # Инициализация
    def __init__(self, a: float, name: str = "Square"):
        self.a = a
        self.b = a
        self.name = name


# Класс треугольника, наследуемый от фигуры
class Triangle(Figure):
    # Инициализация
    def __init__(self, a: float, b: float, c: float, name: str = "Triangle"):
        self.a = a
        self.b = b
        self.c = c
        self.name = name

    # Получить периметр
    def get_perimeter(self):
        self.perimeter = self.a + self.b + self.c
        print(f"Периметр фигуры с именем '{self.name}' равен {self.perimeter}")

    # Получить площадь
    def get_area(self):
        p = (self.a + self.b + self.c)/2
        self.area = (p * (p - self.a) * (p - self.b) * (p - self.c))**1/2
        print(f"Площадь фигуры с именем '{self.name}' равна {self.area}")


obj1 = Triangle(3, 2, 2)
obj2 = Rectangle(1, 2)
obj1.compare_area(obj2)
