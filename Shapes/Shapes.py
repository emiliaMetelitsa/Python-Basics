from __future__ import annotations
import math


class Shape:
    """
    Базовый класс фигуры.
    Определяет интерфейс для вычисления площади и периметра.
    """

    def area(self) -> float:
        """Вычисляет площадь фигуры."""
        raise NotImplementedError

    def perimeter(self) -> float:
        """Вычисляет периметр фигуры."""
        raise NotImplementedError

    def compare_area(self, other: "Shape") -> None:
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

    def compare_perimeter(self, other: "Shape") -> None:
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
    """Класс квадрат."""

    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side ** 2

    def perimeter(self) -> float:
        return 4 * self.side


class Rectangle(Shape):
    """Класс прямоугольник."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Класс круг."""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Triangle(Shape):
    """Класс треугольник по трём сторонам."""

    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        # Формула Герона
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self) -> float:
        return self.a + self.b + self.c


if __name__ == "__main__":
    """Пример использования"""
    fig1 = Square(4)
    fig2 = Rectangle(3, 5)
    fig3 = Triangle(3, 4, 5)
    fig4 = Circle(3)

    fig1.compare_area(fig2)
    fig3.compare_perimeter(fig4)
