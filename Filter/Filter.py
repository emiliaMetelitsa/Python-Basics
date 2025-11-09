def Filtration(lambda_f, arr):
    """
    Фильтрует список строк с использованием переданной лямбда-функции.

    :param lambda_f: лямбда-функция для фильтрации
    :param arr: список строк для фильтрации
    :return: новый список строк, удовлетворяющих условию фильтрации
    """
    return list(filter(lambda_f, arr))

"""Проверяет, что строка не содержит пробелов."""
has_no_spaces = lambda s: " " not in s 
"""Проверяет, что строка не начинается с буквы 'a'."""
not_start_with_a = lambda s: not s[0]=="a"
"""Проверяет, что длина строки не меньше 5 символов."""
min_length_5 = lambda s: len(s) >= 5

#Пример использования
words = [" sihci", "hdjj kdjkd", "jhdi", "iwhjij", "jodjko "]
print(Filtration(has_no_spaces, words))
print(Filtration(not_start_with_a, words))
print(Filtration(min_length_5, words))
