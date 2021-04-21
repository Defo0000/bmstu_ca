from utils import *
from rms import *


print("Введите количество узлов: ", end="")
n = get_n()
while n == -1:
    print("Введите количество узлов: ", end="")
    n = get_n()

x = []
y = []
p = []
p_true = [1 for i in range(n)]

action = get_action()
while action != 8:
    if action == -1:
        action = get_action()
    elif action == 1:
        x, y = generate_table("sin(radians(x[i])) ** 2 + cos(radians(x[i]))", 0, 1000, n)
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
    elif action == 7:
        print_table(x, y, p)
    action = get_action()