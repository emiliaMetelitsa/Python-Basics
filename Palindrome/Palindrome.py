def is_palindrome(string: str) -> bool:
    """
    Проверяет, является ли строка палиндромом.
    :param string: проверяемая строка
    :return: True, если строка палиндром, иначе False
    """
    for i in range(len(string)):
        if string[i] != string[-(i + 1)]:
            return False
    return True


if __name__ == "__main__":
    # Пример использования
    user_input = input("Введите строку: ")
    print(is_palindrome(user_input))
