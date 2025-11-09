def is_palindrome(text: str) -> bool:
    """
    Проверяет, является ли строка палиндромом.

    :param text: Входная строка
    :return: True, если палиндром, иначе False
    """
    for i in range(len(text)):
        if text[i] != text[-(i + 1)]:
            return False
    return True

"""Пример использования"""
user_input = input("Введите строку: ")
print(is_palindrome(user_input))
