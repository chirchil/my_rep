# Написать функцию, которая принимает два аргумента: лямбда функция для фильтрации массива, массив строк.
# Сделать вызов данной функции для следующих функций фильтрации:
# Исключить строки с пробелами
# Исключить строки, начинающиеся с буквы “a”
# Исключить строки, длина которых меньше 5

from typing import Callable, List
import sys


def custom_filter(func: Callable, list_str: List[str]) -> List[str]:
    custom_list = list(filter(func, list_str))
    print(f"The new list of strings is: {custom_list}")
    return custom_list


if __name__ == "__main__":
    list_of_str = ['first item', 'another', 'something else', 'hello world', 'another important string', 'end']
    # list_of_str = sys.argv[1]
    custom_filter(lambda x: " " not in x, list_of_str)  # Исключить строки с пробелами
    custom_filter(lambda x: x[0] != 'a', list_of_str)  # Исключить строки, начинающиеся с буквы “a”
    custom_filter(lambda x: len(x) >= 5, list_of_str)  # Исключить строки, длина которых меньше 5
