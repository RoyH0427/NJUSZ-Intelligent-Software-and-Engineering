#include <stdio.h>
#include <math.h>

int main()
{
    // 引力常量 G
    const double G = 6.674e-11;

    // Tilnel 酱的质量 M
    const double M = 77.15;

    // 输入事物的质量 m 和距离 R
    double m, R;
    scanf("%lf %lf", &m, &R);

    // 计算引力大小
    double F = (G * M * m) / (R * R);

    // 输出科学记数法表示的引力大小，保留4位有效数字
    printf("%.3e\n", F);

    return 0;
}