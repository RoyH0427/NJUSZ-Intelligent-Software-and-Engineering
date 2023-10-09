#include <stdio.h>

int main()
{
    int year, month, day;

    // 从输入中读取年、月、日
    scanf("%d %d %d", &year, &month, &day);

    // 计算儒略日数
    int a = (14 - month) / 12;
    int y = year + 4800 - a;
    int m = month + 12 * a - 3;
    int JDN = day + (153 * m + 2) / 5 + 365 * y + y / 4 - y / 100 + y / 400 - 32045;

    // 输出儒略日数
    printf("%d\n", JDN);

    return 0;
}