#ifndef CALC_H
#define CALC_H

#include "io.h"
#include <math.h>

#define EPS                1e-6

#define ERR_NOT_ENOUGH_DATA   6
#define ERR_ZERO_DIV          7

int newton(point_t points[], int n, double x);
int hermite(point_t points[], int n, double x);
int root(point_t points[], int n);
int get_nearest_pos(point_t points[], int n, double x);

#endif