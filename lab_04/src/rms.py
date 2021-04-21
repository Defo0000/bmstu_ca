from math import *

def get_coeff(p, a, b, degree_a, degree_b):
    coeff = 0

    for i in range(len(p)):
        coeff += p[i] * (a[i] ** degree_a) * (b[i] ** degree_b)

    return coeff


def make_slae(p, x, y):
    n = len(p)

    slae = [[0] * (n + 2)] * (n + 1)

    for i in range(n + 1):
        for j in range(n + 1):
            slae[i][j] = get_coeff(p, x, x, i, j)
        slae[i][n + 1] = get_coeff(p, y, x, 1, i)

    return slae


def solve_slae(slae):
    return slae

