#include "io.h"

int read_filename(char name[], FILE **f)
{
    printf("\nВведите имя файла для чтения данных: ");
    if (!fgets(name, MAX_NAME_LEN, stdin))
    {
        printf("Ошибка во время считывания названия: превышена максимальная длина названия.\n");
        return ERR_READ;
    }
    name[strlen(name) - 1] = '\0';
    if (!strlen(name))
    {
        printf("Ошибка во время считывания названия: введена пустая строка.\n");
        return ERR_LEN;
    }
    *f = fopen(name, "r");
    if (!(*f))
    {
        printf("\nОшибка: файла с таким именем не существует.\n");
        return ERR_FOPEN;
    }
    printf("\nИмя файла успешно считано.\n");
    return EXIT_SUCCESS;
}

int read_data(FILE *f, point_t points[], int *n)
{
    printf("\nЧтение данных из файла...\n");
    rewind(f);
    char buf[MAX_INPUT_LEN];
    int i = 0;
    *n = 0;
    while (fgets(buf, sizeof(buf), f))
    {
        if (sscanf(buf, "%lf%lf%lf", &(points[i].x), &(points[i].y), &(points[i].d_y)) != 3)
        {
            printf("\nОшибка: файл содержит некорректные данные в %d-ой строке.\n", i + 1);
            return ERR_DATA;
        }
        i++;
    }
    if (!feof(f))
    {
        printf("\nОшибка: файл содержит некорректные данные.\n");
        return ERR_DATA;
    }
    if (!i)
    {
        printf("\nОшибка: пустой файл.\n");
        return ERR_EMPTY;
    }
    *n = i;
    printf("\nДанные успешно считаны из файла.\n");
    return EXIT_SUCCESS;
}

void print(point_t points[], int n)
{
    printf("\nПечать данных...\n\n┏━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┓\n");
    printf("┃     x    ┃     y    ┃    dy    ┃\n");
    for (int i = 0; i < n; i++)
    {
        printf("┣━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━┫\n");
        printf("┃%-10lf┃%-10lf┃%-10lf┃\n", points[i].x, points[i].y, points[i].d_y);
    }
    printf("┗━━━━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━━┛\n");
}

int get_x(double *x)
{
    printf("\nВведите точку для аппроксимизации: ");
    if (scanf("%lf", x) != 1)
    {
        printf("\nОшибка: введено некорректное число.\n");
        return ERR_DATA;
    }
    printf("\nТочка успешно введена.\n");
    return EXIT_SUCCESS;
}