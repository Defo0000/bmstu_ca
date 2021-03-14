#ifndef IO_H
#define IO_H

#define ERR_READ  1
#define ERR_LEN   2
#define ERR_FOPEN 3
#define ERR_EMPTY 4
#define ERR_DATA  5

#define MAX_NAME_LEN      30
#define MAX_INPUT_LEN    100
#define MAX_POINTS_COUNT 100

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct 
{
    double x;
    double y;
    double d_y;
} point_t;

int read_filename(char name[], FILE **f);
int read_data(FILE *f, point_t points[], int *n);
void print(point_t points[], int n);
int get_x(double *x);

#endif