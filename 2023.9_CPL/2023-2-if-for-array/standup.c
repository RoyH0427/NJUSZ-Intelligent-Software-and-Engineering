#include <stdio.h>

int minActorsToStandUp(int n, int shyLevels[])
{
    int actorsNeeded = 0;
    int standingCount = 0;

    for (int i = 0; i <= n; i++)
    {
        if (standingCount < i)
        {
            actorsNeeded += i - standingCount;
            standingCount = i;
        }
        standingCount += shyLevels[i];
    }

    return actorsNeeded;
}

int main()
{
    int n;
    scanf("%d", &n);
    int shyLevels[n + 1];

    for (int i = 0; i <= n; i++)
    {
        scanf("%d", &shyLevels[i]);
    }

    int result = minActorsToStandUp(n, shyLevels);

    printf("%d\n", result);

    return 0;
}
