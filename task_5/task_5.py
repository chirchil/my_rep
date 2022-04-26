import time

# Декоратор для вычисления времени выполнения функции
def runtime(func):
    def wrapper(*args):
        start_time = time.perf_counter()
        func(*args)
        stop_time = time.perf_counter()
        print(f"Время выполнения функции равно {round((stop_time-start_time)*1000, 7)} миллисекунд")
    return wrapper


# Функция вычисляет сумму двух чисел a и b, выводит результат в консоль
@runtime
def sum_and_print(a: float, b: float):
    result = a + b
    print(f"Сумма чисел {a} и {b} равна {result}")

# Функция читает из файла input.txt значение двух чисел a и b,
# записывает результат вычисления в файл output.txt (файлы приложить к репозиторию)
@runtime
def file_read_plus_write():
    with open('input.txt') as rfile:
        a = int(rfile.readline())
        b = int(rfile.readline())
        result = a + b
    with open("output.txt", "w") as ofile:
        ofile.write(str(result))


sum_and_print(2, 5)
file_read_plus_write()



