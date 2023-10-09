#include <stdio.h>
#include <math.h>
int main(void)
{
    int n = 0, a = 0;
    double x, y = 0.0, res = 0.0;
    scanf("%lf %d", &x, &n);
    for (int i = 0; i <= n; i++)
    {
        if ((i % 2) < 1)
        {
            a = 1;
        }
        else
        {
            a = -1;
        }

        if (x > 0)
        {
            res = pow(x, (2 * i + 1));
        }
        else if (x < 0)
        {
            res = pow((-x), (2 * i + 1));
            if (((2 * i + 1) % 2) > 0)
            {
                res = -res;
            }
        }
        y = y + ((a * res) / (2 * i + 1));
    }
    y = y * 4;
    printf("%.10lf\n", y);
    return 0;
}
