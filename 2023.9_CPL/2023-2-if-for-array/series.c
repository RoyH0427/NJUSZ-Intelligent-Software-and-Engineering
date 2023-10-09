#include <stdio.h>
#include <math.h>

int main()
{
    double x;
    int n;
    scanf("%lf %d", &x, &n);

    double result = 0.0;

    for (int i = 0; i <= n; i++)
    {
        double term = pow(-1, i) * pow(x, 2 * i + 1) / (2 * i + 1);
        result += term;
    }

    result *= 4;

    printf("%.10lf\n", result);

    return 0;
}
