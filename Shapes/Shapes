import math

class Shape:
    """
    Базовый класс для всех фигур.
    Определяет интерфейс для вычисления площади и периметра.
    """

    def area(self):
        """Вычисляет площадь фигуры."""
        raise NotImplementedError

    def perimeter(self) -> float:
        """Вычисляет периметр фигуры."""
        raise NotImplementedError

    def compare_area(self, other):
        """
        Сравнивает площадь текущей фигуры с другой фигурой.

        :param other: другая фигура
        """
        if self.area() > other.area():
            print("Площадь больше")
        elif self.area() < other.area():
            print("Площадь меньше")
        else:
            print("Площади равны")

    def compare_perimeter(self, other):
        """
        Сравнивает периметр текущей фигуры с другой фигурой.

        :param other: другая фигура
        """
        if self.perimeter() > other.perimeter():
            print("Периметр больше")
        elif self.perimeter() < other.perimeter():
            print("Периметр меньше")
        else:
            print("Периметры равны")


class Square(Shape):
    """Класс, представляющий квадрат."""

    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side ** 2

    def perimeter(self) -> float:
        return self.side * 4


class Rectangle(Shape):
    """Класс, представляющий прямоугольник."""

    def __init__(self, width: float, length: float):
        self.width = width
        self.length = length

    def area(self) -> float:
        return self.width * self.length

    def perimeter(self) -> float:
        return 2 * (self.width + self.length)


class Triangle(Shape):
    """Класс, представляющий треугольник."""

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self) -> float:
        return self.a + self.b + self.c


class Circle(Shape):
    """Класс, представляющий круг."""

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


"""Пример использования"""
fig1 = Square(4)
fig2 = Rectangle(3, 5)
fig3 = Triangle(3, 4, 5)
fig4 = Circle(3)

fig1.compare_area(fig2)
fig3.compare_perimeter(fig4)
