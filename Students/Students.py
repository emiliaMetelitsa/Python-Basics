class Student:
    """Класс студент"""
    def __init__(self, name, age, group, score):
        self.name = name
        self.age = age
        self.group = group
        self.score = score

        """ Расчёт стипендии """
        if self.score == 5:
            self.grant = 6000
        elif self.score < 5:
            self.grant = 4000
        else:
            self.grant = 0
    
    """Выводит ФИО и группу"""
    def print_info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Группа: {self.group}")

    """Выводит стипендию"""
    def print_grant(self):
        print(f"Стипендия: {self.grant} руб.")

    """Сравнивает стипендии"""
    def compare_grant(self, other):
        if self.grant > other.grant:
            print("Стипендия больше")
        elif self.grant < other.grant:
            print("Стипендия меньше")
        else:
            print("Стипендии равные")


class PostGraduate(Student):
    def __init__(self, name, age, group, score, study):
        """Вызываем конструктор родителя"""
        super().__init__(name, age, group, score)
        self.study = study

        """Изменяем логику стипендии"""
        if self.score == 5:
            self.grant = 8000
        elif self.score < 5:
            self.grant = 6000
        else:
            self.grant = 0


"""Пример использования"""
student = Student("Гасанова Эмилия Алиевна", 19, "5132704/30801", 5.0)
post_graduate = PostGraduate("Флинс Кирилл Чудомирович", 25, "66666666/66666", 5.0, "Исследование")

student.print_info()
student.print_grant()
student.compare_grant(post_graduate)

print()

post_graduate.print_info()
post_graduate.print_grant()
