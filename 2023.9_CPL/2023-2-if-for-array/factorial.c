#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);

    int result = 0;
    int factorial = 1;

    for (int i = 1; i <= n; i++)
    {
        factorial = (factorial * i) % 10007;
        result = (result + factorial) % 10007;
    }

    printf("%d\n", result);

    return 0;
}
