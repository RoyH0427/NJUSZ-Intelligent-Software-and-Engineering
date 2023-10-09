#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);

    int steps = 0;
    int max_value = n;

    while (n != 1)
    {
        if (n % 2 == 0)
        {
            n = n / 2;
        }
        else
        {
            n = 3 * n + 1;
        }

        steps++;

        if (n > max_value)
        {
            max_value = n;
        }
    }

    printf("%d %d\n", steps, max_value);

    return 0;
}
