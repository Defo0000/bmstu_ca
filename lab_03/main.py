def make_table_of_squares(t_range, step):
    return [[i, i * i] for i in range(0, t_range + 1, step)]

def print_table(table):
    print("\nf(x):\n")
    for i in range(len(table)):
        print("f(", table[i][0], ") = ", table[i][1], sep="")
    print("\n")

def newton_interpolation(table, x, polynom_degree):
    diffs = [[0 for i in range(polynom_degree)] for i in range(polynom_degree)]

    start_pos = find_range(table, x, polynom_degree)

    for i in range(start_pos, start_pos + polynom_degree):
        diffs[i][0] = (table[i][1] - table[i + 1][1]) / (table[i][0] - table[i + 1][0])

    for col in range(1, polynom_degree):
        for row in range(0, polynom_degree - col):
            diffs[row][col] = (diffs[row][col - 1] - diffs[row + 1][col - 1]) \
                              / (table[row][0] - table[row + col + 1][0])

    res = table[start_pos][1]
    temp = (x - table[start_pos][0])

    for i in range(polynom_degree):
        res += temp * diffs[0][i]
        temp *= (x - table[start_pos + i + 1][0])

    return res


def find_range(table, x, polynom_degree):
    pos, side = get_the_nearest_dot(table, x)

    right_indent = (polynom_degree + 1) // 2
    if side == "right":
        right_indent += (polynom_degree + 1) % 2

    left_indent = polynom_degree + 1 - right_indent

    if (pos - left_indent) < 0:
        return 0
    else:
        if (pos + right_indent) < len(table):
            return pos - left_indent
        else:
            return len(table) - polynom_degree - 1

def get_the_nearest_dot(table, x):
    i = 0
    n = len(table)
    while i < n and table[i][0] < x:
        i += 1
    if i == n:
        i -= 1
    if i > 0 and (x - table[i - 1][0]) < (table[i][0] - x):
        return i - 1, "left"
    else:
        return i, "right"

def spline_interpolation(table, x):
    pass

table = make_table_of_squares(10, 1)
print_table(table)

x1 = 0.5 # Значение аргумента х в 1-ом интервале для проведения интерполяции
x2 = 5.5 # Значение аргумента х в 6-ом интервале для проведения интерполяции

newton_interpolation(table, x1, 3)


