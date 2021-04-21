from random import *
import matplotlib.pyplot as plt
from rms import *

def get_n():
    n = input()
    try:
        n = int(n)
        if n <= 0:
            print("Ошибка: количество должно выражаться положительным числом.")
            return -1
    except:
        print("Ошибка: количество должно выражаться целым числом.")
        return -1
    return n


def get_weight():
    n = input()
    try:
        n = float(n)
        if n < 0 or n > 1:
            print("Ошибка ввода: должно быть введено вещественное число в диапазоне от 0 до 1.")
            return -1
    except:
        print("Ошибка: должно быть введено корректное вещественное число.")
        return -1
    return n


def get_index(n):
    i = input()
    try:
        i = int(i)
        if i < 1 or i > n:
            print("Ошибка ввода: должно быть введено целое число в диапазоне от 1 до N(", n, ").", sep="")
            return -1
    except:
        print("Ошибка: должно быть введено корректное целое число.")
        return -1
    return i


def get_weights(n):
    p = []
    print("Введите веса: ")
    for i in range(n):
        print("P[", i + 1, "] = ", end="", sep="")
        value = get_weight()
        while value == -1:
            print("P[", i + 1, "] = ", end="", sep="")
            value = get_weight()
        p.append(value)
    return p


def edit_weight(p, n):
    print("Введите номер узла, для которого необходимо изменить вес: ")
    i = get_index(n)
    while i == -1:
        print("Введите номер узла, для которого необходимо изменить вес: ")
        i = get_index(n)

    print("Введите P[", i, "]: ", sep="", end="")
    value = get_weight()
    while value == -1:
        print("Введите P[", i, "]: ", sep="", end="")
        value = get_weight()

    p[i - 1] = value
    return p


def edit_degree():
    print("Введите новую степень полинома: ", end="")
    n = get_n()
    while n == -1:
        print("Введите новую степень полинома: ", end="")
        n = get_n()
    return n

def get_action():
    print("\nДоступные действия:")
    print("1) Сгенерировать таблицу (х, у)")
    print("2) Сгенерировать веса")
    print("3) Задать веса для точек вручную")
    print("4) Изменить значение веса заданной точки")
    print("5) Изменить степень полинома")
    print("6) Найти решение")
    print("7) Вывести результат на экран в виде графика")
    print("8) Вывести таблицу на экран")
    print("9) Завершить программу")
    n = input("\nВаш выбор: ")
    try:
        n = int(n)
        if n < 1 or n > 9:
            print("Ошибка ввода команды: должна быть введена цифра от 1 до 9 включительно.")
            return -1
    except:
        print("Ошибка: количество должно выражаться целым числом.")
        return -1
    return n

def generate_table(func, left, right, n):
    y = [0] * n

    x = [i for i in range(left, right)]
    shuffle(x)
    x = x[:n]
    x = sorted(x)

    for i in range(n):
        y[i] = eval(func)

    return x, y


def generate_weight(n):
    return [random() for i in range(n)]


def print_table(x, y, p):
    print("┏━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━┓")
    print("┃   № узла  ┃     X     ┃     Y     ┃    Вес    ┃")
    for i in range(len(x)):
        print("┣━━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━━┫")
        print("┃", "%9d" % (i + 1), "┃", "%9.2f" % x[i], "┃", "%9.2f" % y[i], "┃", "%9.2f" % p[i], "┃")
    print("┗━━━━━━━━━━━┻━━━━━━━━━━━┻━━━━━━━━━━━┻━━━━━━━━━━━┛")


def get_polynom_value(coeffs, x):

    res = coeffs[0]
    mul = x

    for i in range(1, len(coeffs)):
        res += mul * coeffs[i]
        mul *= x

    return res

def draw_data(coeffs, x, y, degree, name_func):

    plt.title("Аппроксимация для функции " + name_func)

    apr_func = []
    for i in range(len(x)):
        apr_func.append(get_polynom_value(coeffs, x[i]))

    plt.scatter(x, y)
    plt.plot(x, apr_func)

    plt.show()