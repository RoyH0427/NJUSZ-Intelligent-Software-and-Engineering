#include <stdio.h>
#include <math.h>

int main()
{
    double pi1, pi2;

    // 计算圆周率近似值1
    pi1 = (log(pow(640320.0, 3) + 744.0) / sqrt(163.0));

    // 计算圆周率近似值2
    pi2 = (4.0 * atan(1.0 / 5.0) - atan(1.0 / 239.0)) * 4;

    // 输出结果，保留15位小数
    printf("%.15lf\n%.15lf\n", pi1, pi2);

    return 0;
}