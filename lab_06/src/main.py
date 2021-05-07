def left_diff_derivative(y, step, i):
    if i > 0:
        return (y[i] - y[i - 1]) / step
    else:
        return None

def right_diff_derivative(y, step, i):
    if i + 1 < len(y):
        return (y[i + 1] - y[i]) / step
    else:
        return None

def center_diff_derivative(y, step, i):
    if 0 < i < (len(y) - 1):
        return (y[i + 1] - y[i - 1]) / (2 * step)
    else:
        return None

def second_diff_derivative(y, step, i):
    if 0 < i < (len(y) - 1):
        return (y[i - 1] - 2 * y[i] + y[i + 1]) / (step ** 2)
    else:
        return None

def runge_left_derivative(y, step, i):
    if i > 1:
        f = left_diff_derivative(y, step, i)
        w = (y[i] - y[i - 2]) / (2 * step)
        return 2 * f - w
    else:
        return None

def align_vars_derivative(x, y, i):
    if i > (len(y) - 2):
        return None
    else:
        align_vars_diff = (1 / y[i + 1] - 1 / y[i]) / (1 / x[i + 1] - 1 / x[i])
        return y[i] * y[i] / (x[i] * x[i]) * align_vars_diff

x = [1, 2, 3, 4, 5, 6]
y = [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]

def print_float(value):
    if value == None:
        print("┃" + " " * 3 + "----" + " " * 2, end=" ")
    else:
        print("┃" + str("%9.3f" % value), end=" ")
def print_char(value):
    print("┃" + " " * 4 + value + " " * 4, end=" ")
def print_header():
    print("┏" + ("━" * 10 + "┳") * 6 + "━" * 10 + "┓")
def print_end():
    print("\n┗" + ("━" * 10 + "┻") * 6 + "━" * 10 + "┛")
def print_between_line():
    print("\n┣" + ("━" * 10 + "╋") * 6 + "━" * 10 + "┫")
    

print_header()
print_char("x")
print_char("y")
for i in range(1, 6):
    print_char(str(i))
print("┃", end="")
print_between_line()

step = x[1] - x[0]

for i in range(len(x)):
    print_char(str(x[i]))
    print_float(y[i])
    print_float(left_diff_derivative(y, step, i))
    print_float(center_diff_derivative(y, step, i))
    print_float(runge_left_derivative(y, step, i))
    print_float(align_vars_derivative(x, y, i))
    print_float(second_diff_derivative(y, step, i))
    print("┃", end=" ")
    if i != (len(x) - 1):
        print_between_line()

print_end()