from __future__ import annotations
from typing import Optional


class Student:
    """
    Класс Student представляет обычного студента.

    Атрибуты:
        name: ФИО студента
        age: возраст студента (целое число)
        group: номер группы (строка)
        score: средний балл (0.0 - 5.0)
        grant: вычисляемая величина стипендии (руб.)
    """

    # Константы стипендий для студентов
    GRANT_EXCELLENT: int = 6000
    GRANT_GOOD: int = 4000
    GRANT_NONE: int = 0

    def __init__(self, name: str, age: int, group: str, score: float) -> None:
        """
        Инициализация студента и вычисление стипендии.

        :param name: ФИО
        :param age: возраст
        :param group: номер группы
        :param score: средний балл
        """
        self.name: str = name
        self.age: int = age
        self.group: str = group
        self.score: float = score
        self.grant: int = self._calculate_grant()

    def _calculate_grant(self) -> int:
        """
        Вычисляет размер стипендии на основании среднего балла.

        :return: размер стипендии в рублях
        """
        if self.score == 5:
            return self.GRANT_EXCELLENT
        if self.score < 5:
            return self.GRANT_GOOD
        return self.GRANT_NONE

    def print_info(self) -> None:
        """Выводит ФИО, возраст и группу."""
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Группа: {self.group}")

    def print_grant(self) -> None:
        """Печатает текущий размер стипендии."""
        print(f"Стипендия: {self.grant} руб.")

    def compare_grant(self, other: "Student") -> None:
        """
        Сравнивает размер стипендии с другим студентом/аспирантом.

        :param other: другой объект типа Student или его подкласс
        """
        if self.grant > other.grant:
            print("Стипендия больше")
        elif self.grant < other.grant:
            print("Стипендия меньше")
        else:
            print("Стипендии равные")


class PostGraduate(Student):
    """
    Класс PostGraduate (аспирант). Отличается наборами значений стипендий
    и дополнительным полем study (название научной работы).
    """

    # Константы стипендий для аспирантов
    GRANT_EXCELLENT: int = 8000
    GRANT_GOOD: int = 6000
    GRANT_NONE: int = 0

    def __init__(self, name: str, age: int, group: str, score: float, study: str) -> None:
        """
        Инициализация аспиранта.

        :param name: ФИО
        :param age: возраст
        :param group: группа/идентификатор
        :param score: средний балл
        :param study: название научной работы
        """
        super().__init__(name, age, group, score)
        self.study: str = study
        # Пересчитываем стипендию в случае, если константы в подклассе отличаются
        self.grant = self._calculate_grant()

    # Переопределение не требуется, т.к. базовый _calculate_grant использует
    # константы текущего класса (self.GRANT_...), поэтому поведение наследуется.


if __name__ == "__main__":
    # Пример использования (не будет выполняться при импорте модуля)
    student = Student("Гасанова Эмилия Алиевна", 19, "5132704/30801", 5.0)
    post_graduate = PostGraduate("Флинс Кирилл Чудомирович", 25, "66666666/66666", 5.0, "Исследование")

    student.print_info()
    student.print_grant()
    student.compare_grant(post_graduate)

    print()

    post_graduate.print_info()
    post_graduate.print_grant()
    post_graduate.compare_grant(student)
post_graduate.print_grant()
