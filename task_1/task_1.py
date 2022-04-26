# Функция, проверяющая палиндром
def is_palindrome(string: str) -> str:
    """
    Функция проверяет, является ли строка палиндромом
    """
    return string == string[::-1]

print(is_palindrome('tenet'))