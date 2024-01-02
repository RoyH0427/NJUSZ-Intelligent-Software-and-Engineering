#include <stdio.h>
#include <stdbool.h>
#include <limits.h>
int main()
{
    // test 1
    if (0 == (unsigned)0)
    {
        printf("0 == 0U is true\n");
    }
    else
    {
        printf("0 == 0U is false\n");
    }

    // test 2
    if (-1 < 0)
    {
        printf("-1 < 0 is true\n");
    }
    else
    {
        printf("-1 < 0 is false\n");
    }

    // test 3
    if (-1 < (unsigned)0)
    {
        printf("-1 < 0U is true\n");
    }
    else
    {
        printf("-1 < 0U is false\n");
    }

    // test 4
    int x = 2147483647;
    if (x > -x - 1)
    {
        printf("2147483647 > -2147483648 -1  is true\n");
    }
    else
    {
        printf("2147483647 > -2147483648 -1  is false\n");
    }

    // test 5
    if ((unsigned)x > -x - 1)
    {
        printf("2147483647U > -2147483648 -1  is true\n");
    }
    else
    {
        printf("2147483647U > -2147483648 -1  is false\n");
    }

    // test 6
    unsigned int y = 2147483648;
    if (x > (int)y)
    {
        printf("2147483647 > (int))147483648U is true\n");
    }
    else
    {
        printf("2147483647 > (int)2147483648U is false\n");
    }

    // test 7
    if (-1 > -2)
    {
        printf("-1 > -2 is true\n");
    }
    else
    {
        printf("-1 > -2 is false\n");
    }

    // test 8
    if ((unsigned)-1 > -2)
    {
        printf("-1U > -2 is true\n");
    }
    else
    {
        printf("-1U > -2 is false\n");
    }

    return 0;
}
