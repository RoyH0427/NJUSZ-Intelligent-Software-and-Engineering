#include <stdio.h>
#include <math.h>

int main()
{
    // 原数据
    double originalData = 1.123456789012345678901234567890;

    // 转换为float类型
    float floatData = (float)originalData;

    // 检查"-4.0/0"的运算结果
    float result1 = -4.0 / 0;

    // 检查"sqrt(-9.0)"的运算结果
    double result2 = sqrt(-9.0);

    // 输出originalData的值
    printf("Original: 1.123456789012345678901234567890\n");

    // 输出float类型的值
    printf("Float: %.20f\n", floatData);

    // 输出double类型的值
    printf("Double: %.20lf\n", originalData);

    // 输出"-4.0/0"的运算结果
    printf("-4.0/0 = %f\n", result1);

    // 输出"sqrt(-9.0)"的运算结果
    printf("sqrt(-9.0) = %f\n", result2);

    return 0;
}
