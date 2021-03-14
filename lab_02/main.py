def check_int(str):
    try:
        int(str)
        return True
    except:
        return False

def check_float(str):
    try:
        float(str)
        return True
    except:
        return False

def read_data(name):
    f = open(name, 'r')
    dims = f.readline().split()
    if len(dims) != 2:
        return -1
    rows, cols = dims
    if check_int(rows) == False or check_int(cols) == False:
        return -1
    rows = int(rows)
    cols = int(cols)
    a = [[0 for i in range(rows)] for j in range(cols)]
    i = 0
    for line in f:
        line = line.split()
        if len(line) != cols:
            return -1
        a[i] = line
        for j in range(cols):
            if check_float(a[i][j]) == False:
                return -1
            a[i][j] = float(a[i][j])
        i += 1
    return a, rows, cols

def print_data(a, rows, cols):
    print()
    print("┏" + "━━━━━━━━━━━━┳" * cols + "━━━━━━━━━━━━┓")
    print("┃     Х/У    ┃", end="")
    for i in range(cols):
        print("%11d" % i, "┃", end="")
    print()
    for i in range(rows):
        print("┣" + "━━━━━━━━━━━━╋" * cols + "━━━━━━━━━━━━┫")
        print("┃", "%11d" % i, end="")
        for j in range(cols):
            print("┃", "%10.2f" % a[i][j], end=" ")
        print("┃")
    print("┗" + "━━━━━━━━━━━━┻" * cols + "━━━━━━━━━━━━┛")
    print()

def get_near_dots(a, value, n):
    n += 1
    pos = get_pos(a, value)
    if pos < (n // 2):
        start = 0
    elif (pos + n // 2) > len(a):
        start = len(a) - n
    else:
        start = pos - n // 2
    return a[start:start + n]

def get_pos(a, value):
    right = 0
    while right < len(a) and right < value:
        right += 1
    if right >= (len(a) - 1):
        return len(a) - 1
    elif right == 0:
        return 0
    else:
        left = right - 1
        if (right - value) <= (value - left):
            return right
        else:
            return left

def interpolation(f, x, n):

    nums = [i for i in range(len(f))]
    near = get_near_dots(nums, x, n)

    div_sums = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        div_sums[i][0] = (f[near[i]] - f[near[i + 1]]) / (near[i] - near[i + 1])

    for i in range(1, n):
        for j in range(0, n - i):
            div_sums[j][i] = (div_sums[j][i - 1] - div_sums[j + 1][i - 1]) / (near[j] - near[j + i + 1])

    ans = f[near[0]]
    temp = (x - near[0])
    for i in range(n):
        ans += temp * div_sums[0][i]
        temp *= (x - near[i + 1])
    return ans

def multi_interpolation(f, x, y, n_x, n_y):

    data = [i for i in range(len(f))]
    near_y = get_near_dots(data, y, n_y)

    ans = [0 for i in range(cols)]

    for k in range(len(near_y)):
        vals = [f[i][near_y[k]] for i in range(rows)]
        ans[near_y[k]] = (interpolation(vals, x, n_x))

    return interpolation(ans, y, n_y)

x = 1.5
y = 1.5

res = read_data("data.txt")
if res == -1:
    print("Ошибка чтения данных из файла.")
else:
    a, rows, cols = res
    print_data(a, rows, cols)
    print("X: ", x, ", Y: ", y)
    print("┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓")
    print("┃  N_X/N_Y   ┃      1     ┃      2     ┃      3     ┃")
    for n_x in range(1, 4):
        print("┣━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━┫")
        print("┃" + "%12d" % n_x, end="")
        for n_y in range(1, 4):

            print("┃" + "%11.2f" % multi_interpolation(a, x, y, n_x, n_y), end=" ")
        print("┃")
    print("┗━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━━━━━━━┛")