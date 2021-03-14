#include <stdlib.h>
#include <stdio.h>

#define ERR_FOPEN -1
#define ERR_DATA  -2

double* read_data(FILE *f, int *rows, int *cols)
{
    int n, m;
    if (fscanf(f, "%d%d", &n, &m) != 2 || n <= 0 || m <= 0)
        return NULL;
    double *arr = malloc(sizeof(double) * n * m);
    if (!arr)
        return NULL;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (fscanf(f, "%lf", &(arr[i * n + j])) != 1)
            {
                free(arr);
                return NULL;
            }
    *rows = n;
    *cols = m;
    return arr;
}

void print_data(double *arr, int rows, int cols)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
            printf("%.2lf ", arr[i * rows + j]);
        printf("\n");
    } 
}

int main()
{
    setbuf(stdout, NULL);
    int x = 1.5, y = 1.5, n_x, n_y;
    int rows, cols;
    FILE *f = fopen("data.txt", "r");
    if (!f)
    {
        printf("\nОшибка во время считывания данных из файла.\n");
        return ERR_FOPEN;
    }
    double *arr = read_data(f, &rows, &cols);
    if (!arr)
    {
        printf("\nФайл содержит некорректные данные.\n");
        return ERR_DATA;
    }
    print_data(arr, rows, cols);
    free(arr);
    return EXIT_SUCCESS;
}