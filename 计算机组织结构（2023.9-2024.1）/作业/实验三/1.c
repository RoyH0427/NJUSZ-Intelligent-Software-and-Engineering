#include <stdio.h>

int main() {
    // 给定一个 short 型数据 -12345
    short shortValue = -12345;
    
    // 转换为 int 类型的数据
    int intValue = (int)shortValue;
    
    // 转换为 unsigned short 类型的数据
    unsigned short ushortValue = (unsigned short)shortValue;
    
    // 转换为 unsigned int 类型的数据
    unsigned int uintValue = (unsigned int)shortValue;
    
    // 转换为 float 类型的数据
    float floatValue = (float)shortValue;
    
    // 打印输出各种操作的结果（十进制和十六进制形式）
    printf("short 转换为 int: \n 十进制: %d, 十六进制: %X\n", intValue, intValue);
    printf("short 转换为 unsigned short: \n 十进制: %u, 十六进制: %X\n", ushortValue, ushortValue);
    printf("short 转换为 unsigned int: \n 十进制: %u, 十六进制: %X\n", uintValue, uintValue);
    printf("short 转换为 float: \n 十进制: %f, 十六进制表示不适用\n", floatValue);
    
    return 0;
}
