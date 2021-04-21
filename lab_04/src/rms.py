from math import *

def get_coeff(p, a, b, degree_a, degree_b):
    coeff = 0

    for i in range(len(p)):
        coeff += p[i] * (a[i] ** degree_a) * (b[i] ** degree_b)

    return coeff


def make_slae(p, x, y, degree):
    n = degree

    slae = [0] * (n + 1)
    for i in range(n + 1):
        slae[i] = [0] * (n + 2)

    for i in range(n + 1):
        for j in range(n + 1):
            slae[i][j] = get_coeff(p, x, x, i, j)
        slae[i][n + 1] = get_coeff(p, y, x, 1, i)

    return slae


def solve_slae(p, x, y, degree):

    slae = make_slae(p, x, y, degree)

    n = degree + 1

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            mul = slae[j][i] / slae[i][i]
            for k in range(n + 1):
                slae[j][k] -= mul * slae[i][k]

    for i in range(n):
        div = slae[i][i]
        for j in range(n + 1):
            slae[i][j] /= div

    return [slae[i][-1] for i in range(len(slae))]
