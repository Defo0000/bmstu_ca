#include "calc.h"

int newton(point_t points[], int n, double x)
{ 
    if (n < 4)
    {
        printf("\nНевозможно произвести анализ: необходимо минимум 4 точки.\n");
        return ERR_NOT_ENOUGH_DATA;
    }
    int res = get_nearest_pos(points, n, x);
    int start;
    if (res < 2)
        start = 0;
    else if (res + 2 > n)
        start = n - 5;
    else
        start = res - 2;

    double diff[4][4];

    for (int i = 0; i < 4; i++)
        diff[i][0] = (points[i + start].y - points[i + start + 1].y) / (points[i + start].x - points[i + start + 1].x);

    for (int i = 1; i < 4; i++)
        for (int j = 0; j < 4 - i; j++)
        {
            if (points[j].x == points[j + i + 1].x)
            {
                printf("\nОшибка: деление на ноль.\n");
                return ERR_ZERO_DIV;
            }
            diff[j][i] = (diff[j][i - 1] - diff[j + 1][i - 1]) / (points[j].x - points[j + i + 1].x);
        }
        
    printf("\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓");
    printf("\n┃                Полином Ньютона                ┃");
    printf("\n┣━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━┫");
    printf("\n┃   n = 1   ┃   n = 2   ┃   n = 3   ┃   n = 4   ┃");
    printf("\n┣━━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━━┫\n");
    double ans = points[start].y, temp = (x - points[start].x);
    for (int i = 0; i < 4; i++)
    {
        ans += temp * diff[0][i];
        printf("┃%11lf", ans);
        temp *= (x - points[start + i + 1].x);
    }
    printf("┃\n┗━━━━━━━━━━━┻━━━━━━━━━━━┻━━━━━━━━━━━┻━━━━━━━━━━━┛\n");
    return EXIT_SUCCESS;
}

int hermite(point_t points[], int n, double x)
{
    if (n < 4)
    {
        printf("\nНевозможно произвести анализ: необходимо минимум 4 точки.\n");
        return ERR_NOT_ENOUGH_DATA;
    }
    int res = get_nearest_pos(points, n, x);
    int start;
    if (res < 3)
        start = 0;
    else
        start = res - 1;

    double diff[4][4];

    diff[0][0] = points[start].d_y;
    diff[1][0] = (points[start].y - points[start + 1].y) / (points[start].x - points[start + 1].x);
    diff[2][0] = points[start + 1].d_y;
    diff[3][0] = (points[start + 1].y - points[start + 2].y) / (points[start + 1].x - points[start + 2].x);

    for (int i = 1; i < 4; i++)
        for (int j = 0; j < 4 - i; j++)
            if (points[j].x == points[j + i + 1].x)
                diff[i][j] = points[j].d_y;
            else
                diff[j][i] = (diff[j][i - 1] - diff[j + 1][i - 1]) / (points[j].x - points[j + i + 1].x);
    
    printf("\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓");
    printf("\n┃                Полином Эрмита                 ┃");
    printf("\n┣━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━┫");
    printf("\n┃   n = 1   ┃   n = 2   ┃   n = 3   ┃   n = 4   ┃");
    printf("\n┣━━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━━┫\n");
    double ans = points[start].y, temp = (x - points[start].x);
    for (int i = 0; i < 4; i++)
    {
        ans += temp * diff[0][i];
        printf("┃%11lf", ans);
        temp *= (x - points[start + i + 1].x);
    }
    printf("┃\n┗━━━━━━━━━━━┻━━━━━━━━━━━┻━━━━━━━━━━━┻━━━━━━━━━━━┛\n");
    return EXIT_SUCCESS;
}

int root(point_t points[], int n)
{
    if (n < 4)
    {
        printf("\nНевозможно произвести анализ: необходимо минимум 4 точки.\n");
        return ERR_NOT_ENOUGH_DATA;
    }
    double x = 0;
    int res = get_nearest_pos(points, n, x);
    int start;
    if (res < 2)
        start = 0;
    else if (res + 2 > n)
        start = n - 5;
    else
        start = res - 2;

    double diff[4][4];
    
    for (int i = 0; i < 4; i++)
        diff[i][0] = (points[i + start].x - points[i + start + 1].x) / (points[i + start].y - points[i + start + 1].y);

    for (int i = 1; i < 4; i++)
        for (int j = 0; j < 5 - i - 1; j++)
        {
            if (points[j].y == points[j + i + 1].y)
            {
                printf("\nОшибка: деление на ноль.\n");
                return ERR_ZERO_DIV;
            }
            diff[j][i] = (diff[j][i - 1] - diff[j + 1][i - 1]) / (points[j].y - points[j + i + 1].y);
        }

    printf("\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓");
    printf("\n┃  Нахождение корня с помощью полинома Ньютона  ┃");
    printf("\n┣━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━┫");
    printf("\n┃   n = 1   ┃   n = 2   ┃   n = 3   ┃   n = 4   ┃");
    printf("\n┣━━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━━┫\n");
    double ans = points[start].x, temp = (x - points[start].y);
    for (int i = 0; i < 4; i++)
    {
        ans += temp * diff[0][i];
        printf("┃%11lf", ans);
        temp *= (x - points[start + i + 1].y);
    }
    printf("┃\n┗━━━━━━━━━━━┻━━━━━━━━━━━┻━━━━━━━━━━━┻━━━━━━━━━━━┛\n");
    return EXIT_SUCCESS;
}

int get_nearest_pos(point_t points[], int n, double x)
{
    int res = 0;
    for (int i = 1; i < n; i++)
        if (fabs(points[i].x - x) < (fabs(points[res].x - x) - EPS))
            res = i;
    return res;
}