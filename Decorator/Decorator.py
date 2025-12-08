import time
from typing import Callable

# Константы для путей
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def time_decorator(func: Callable) -> Callable:
    """
    Декоратор, измеряющий время выполнения функции.

    :param func: функция, которую нужно задекорировать
    :return: обёртка функции
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения функции {func.__name__}: {end - start:.10f} сек.")
        return result
    return wrapper


def sum_numbers(a: float, b: float) -> float:
    """
    Вычисляет сумму двух чисел и выводит результат в консоль.

    :param a: первое число
    :param b: второе число
    :return: сумма чисел
    """
    result = a + b
    print(f"Сумма {a} + {b} = {result}")
    return result


def sum_from_file(input_path: str = INPUT_FILE, output_path: str = OUTPUT_FILE) -> float:
    """
    Считывает два числа из файла input_path,
    вычисляет их сумму и записывает результат в файл output_path.

    :param input_path: путь к входному файлу
    :param output_path: путь к выходному файлу
    :return: сумма прочитанных чисел
    """
    with open(input_path, "r", encoding="utf-8") as f:
        a = float(f.readline().strip())
        b = float(f.readline().strip())

    result = a + b

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"Сумма {a} + {b} = {result}\n")

    print(f"Результат записан в {output_path}")
    return result


if __name__ == "__main__":
    # Пример использования
    decorated_sum = time_decorator(sum_numbers)
    decorated_sum(5, 7)

    decorated_sum_from_file = time_decorator(sum_from_file)
    decorated_sum_from_file()
