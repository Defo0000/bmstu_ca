from utils import *
from rms import *


print("Введите количество узлов для формирования таблицы: ", end="")
n = get_n()
while n == -1:
    print("Введите количество узлов для формирования таблицы: ", end="")
    n = get_n()
print("Количество узлов введено.")


print("Введите степень полинома: ", end="")
degree = get_n()
while n == -1:
    print("Введите степень полинома: ", end="")
    degree = get_n()
print("Степень полинома введена.")

x = []
y = []
p = []
coeffs = []
p_true = [1 for i in range(n)]

action = get_action()
while action != 9:
    if action == -1:
        action = get_action()
    elif action == 1:
        x, y = generate_table("sin(x[i]) * x[i] ** 2 - 50 * x[i]", 0, 100, n)
        p = p_true
        print("\nТаблица успешно сгенерирована.")
    elif action == 2:
        p = generate_weight(n)
        print("\nВеса успешно сгенерированы.")
    elif action == 3:
        p = get_weights(n)
        print("\nВеса успешно введены.")
    elif action == 4:
        p = edit_weight(p, n)
        print("Значение успешно изменено.")
    elif action == 5:
        degree = edit_degree()
        print("Значение степени полинома успешно изменено.")
    elif action == 6:
        if not x:
            print("Таблица не создана. Воспользуйтесь пунктом 1.")
        else:
            coeffs = solve_slae(p, x, y, degree)
            print("\nАппроксимирующая функция найдена.")
    elif action == 7:
        if not coeffs:
            coeffs = solve_slae(p, x, y, degree)
        draw_data(coeffs, x, y, degree, "sin(x) * x^2 - 50 * x")
    elif action == 8:
        print_table(x, y, p)
    action = get_action()