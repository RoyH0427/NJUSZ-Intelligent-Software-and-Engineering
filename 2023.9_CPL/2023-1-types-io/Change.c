#include <stdio.h>

int main() {
    int n;

    // 读取输入的软妹币数额
    scanf("%d", &n);

    // 计算各面额纸币的数量
    int num50 = n / 50;
    n %= 50;

    int num20 = n / 20;
    n %= 20;

    int num10 = n / 10;
    n %= 10;

    int num5 = n / 5;
    n %= 5;

    int num1 = n;

    // 输出结果
    printf("%d\n%d\n%d\n%d\n%d\n", num50, num20, num10, num5, num1);

    return 0;
}
