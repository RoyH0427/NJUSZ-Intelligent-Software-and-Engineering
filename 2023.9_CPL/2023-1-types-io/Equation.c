#include <stdio.h>
#include <math.h>

int main()
{
    float p, q;
    double x;
    scanf("%f %f", &p, &q);

    double a = -q / 2;
    double b = q / 2;
    double c = p / 3;

    double discriminant = b * b + c * c * c;

    if (discriminant < 0)
    {
        printf("No real solution\n");
    }
    else
    {
        x = cbrt(a + sqrt(discriminant)) + cbrt(a - sqrt(discriminant));
        printf("%.3lf\n", x);
    }

    return 0;
}