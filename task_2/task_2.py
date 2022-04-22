from typing import Callable, List
import sys


# Кастомный фильтр
def custom_filter(filter_func: Callable, list_of_str : List[str]) -> List[str]:
    custom_list = list(filter(filter_func, list_of_str ))
    print(f"The new list of strings is: {custom_list}")
    return custom_list


if __name__ == "__main__":
    list_of_str = ['first item', 'another', 'something else', 'hello world', 'another important string', 'end']
    custom_filter(lambda x: " " not in x, list_of_str)  # Исключить строки с пробелами
    custom_filter(lambda x: x[0] != 'a', list_of_str)  # Исключить строки, начинающиеся с буквы “a”
    custom_filter(lambda x: len(x) >= 5, list_of_str)  # Исключить строки, длина которых меньше 5
