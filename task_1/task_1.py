# Функция, проверяющая палиндром
def palindrome(string: str) -> str:
    """
    Функция проверяет, является ли строка палиндромом
    """
    if string == string[::-1]:
        print(f"The string '{string}' is a palindrome")
    else:
        print(f"The string '{string}' is not a palindrome")
