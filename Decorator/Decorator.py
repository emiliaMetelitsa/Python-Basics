import time

def time_decorator(func):
    """
    Декоратор, измеряющий время выполнения функции.

    :param func: функция, время выполнения которой нужно измерить
    :return: обёртка, выводящая время работы функции
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения функции {func.__name__}: {end - start:.10f} сек.")
        return result
    return wrapper


def sum_numbers(a, b):
    """
    Вычисляет сумму двух чисел и выводит результат в консоль.

    :param a: первое число
    :param b: второе число
    :return: сумма чисел
    """
    result = a + b
    print(f"Сумма {a} + {b} = {result}")
    return result


def sum_from_file():
    """
    Считывает два числа из файла input.txt,
    вычисляет их сумму и записывает результат в файл output.txt.

    :return: сумма считанных чисел
    """
    with open("input.txt", "r", encoding="utf-8") as f:
        a = float(f.readline().strip())
        b = float(f.readline().strip())

    result = a + b
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(f"Сумма {a} + {b} = {result}\n")

    print(f"Результат записан в output.txt")
    return result

"""Пример использования"""
decorated_sum = time_decorator(sum_numbers)
decorated_sum(5,7)
decorated_sum_from_file = time_decorator(sum_from_file)
decorated_sum_from_file()
