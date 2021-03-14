#include "io.h"
#include "calc.h"

int main(void)
{
    FILE *f;
    char name[MAX_NAME_LEN];
    int rc = read_filename(name, &f);
    point_t points[MAX_POINTS_COUNT];
    int n = 0;
    double x;
    if (!rc)
    {
        rc = read_data(f, points, &n);
        if (!rc)
        {
            print(points, n);
            rc = get_x(&x);
            if (!rc)
            {
                newton(points, n, x);
                hermite(points, n, x);
                root(points, n);
                fclose(f);
            }
        }
    }
    return rc;
}