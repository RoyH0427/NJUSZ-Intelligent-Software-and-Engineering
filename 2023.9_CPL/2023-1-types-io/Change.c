#include <stdio.h>

int main()
{
    int n;
    char C, c;

    // 读取输入整数 n
    scanf("%d", &n);

    // 计算字符 C 和对应的小写字母 c 的 ASCII 码值
    C = (char)n;
    c = (C >= 'A' && C <= 'Z') ? (char)(C + 32) : C; // 转换为小写字母
    int m = (int)c;
    // 输出结果
    printf("%d %c\n", n, C);
    printf("%d %c\n", m, c);

    return 0;
}
