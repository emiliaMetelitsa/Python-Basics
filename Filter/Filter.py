from typing import Callable


def filtration(lambda_f: Callable[[str], bool], arr: list[str]) -> list[str]:
    """
    Фильтрует список строк с использованием переданной лямбда-функции.

    :param lambda_f: лямбда-функция для фильтрации
    :param arr: список строк для фильтрации
    :return: новый список строк, удовлетворяющих условию фильтрации
    """
    return list(filter(lambda_f, arr))


# Лямбда-фильтры
has_no_spaces = lambda x: " " not in x
not_start_with_a = lambda x: not x.startswith("a")
min_length_5 = lambda x: len(x) >= 5


if __name__ == "__main__":
    # Пример использования
    words = [" sihci", "hdjj kdjkd", "jhdi", "iwhjij", "jodjko "]

    print(filtration(has_no_spaces, words))
    print(filtration(not_start_with_a, words))
    print(filtration(min_length_5, words))
