# Класс фигуры
class Figure:
    # Сравнить площади
    def compare_area(self, obj: object):
        return True if self.area > obj.area else False

    # Сравнить периметры
    def compare_perimeter(self, obj: object):
        return True if self.perimeter > obj.perimeter else False


# Класс прямоугольника
class Rectangle(Figure):
    # Инициализация
    def __init__(self, a: float, b: float, name: str = "Rectangle"):
        self.a = a
        self.b = b
        self.name = name
        self.area = self.a * self.b
        self.perimeter = 2 * (self.a + self.b)


# Класс Квадрата, наследуемый от прямоугольника
class Square(Rectangle):
    # Инициализация
    def __init__(self, a: float, name: str = "Square"):
        self.a = a
        self.b = a
        self.name = name
        self.area = self.a * self.b
        self.perimeter = 2 * (self.a + self.b)


# Класс треугольника, наследуемый от фигуры
class Triangle(Figure):
    # Инициализация
    def __init__(self, a: float, b: float, c: float, name: str = "Triangle"):
        self.a = a
        self.b = b
        self.c = c
        self.name = name
        p = (self.a + self.b + self.c)/2
        self.area = (p * (p - self.a) * (p - self.b) * (p - self.c))**1/2
        self.perimeter = self.a + self.b + self.c

    # Получить периметр
    def print_perimeter(self):
        print(f"Периметр фигуры с именем '{self.name}' равен {self.perimeter}")

    # Получить площадь
    def print_area(self):
        print(f"Площадь фигуры с именем '{self.name}' равна {self.area}")


obj1 = Triangle(3, 2, 2)
obj1.print_area()
obj2 = Rectangle(1, 2)
obj2.print_area()
print(obj1.compare_area(obj2))

