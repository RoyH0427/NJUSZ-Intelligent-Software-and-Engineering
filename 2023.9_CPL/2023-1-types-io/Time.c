#include <stdio.h>

int main()
{
    int dd, yyyy, hh, ss, mm;
    char mmm[10];
    char www[10];
    scanf("%s %d %d %s %d %d %d", mmm, &dd, &yyyy, www, &hh, &mm, &ss);
    printf("%.3s %.3s %.2d %.2d:%.2d:%.2d %.4d", www, mmm, dd, hh, mm, ss, yyyy);
    return 0;
}