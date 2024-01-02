#include <stdio.h>

int main() {
    // 给定一个 int 型数据 2147483647
    int intValue = 2147483647;
    
    // 转换为 short 类型的数据
    short shortValue = (short)intValue;
    
    // 转换为 unsigned short 类型的数据
    unsigned short ushortValue = (unsigned short)intValue;
    
    // 转换为 unsigned int 类型的数据
    unsigned int uintValue = (unsigned int)intValue;
    
    // 转换为 float 类型的数据
    float floatValue = (float)intValue;
    
    // 打印输出各种操作的结果（十进制和十六进制形式）
    printf("int 转换为 short\n 十进制: %d, 十六进制: %X\n", shortValue, shortValue);
    printf("int 转换为 unsigned short\n 十进制: %u, 十六进制: %X\n", ushortValue, ushortValue);
    printf("int 转换为 unsigned int\n 十进制: %u, 十六进制: %X\n", uintValue, uintValue);
    printf("int 转换为 float\n 十进制: %f, 十六进制表示不适用\n", floatValue);
    
    return 0;
}
