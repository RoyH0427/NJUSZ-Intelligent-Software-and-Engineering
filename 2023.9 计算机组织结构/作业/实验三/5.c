#include <stdio.h>

int main() {
    // 给定一个 short 型数据 -12345
    short shortValue = -12345;
    
    // 按 short 类型左移 2 位
    short leftShiftShort = shortValue << 2;
    
    // 按 short 类型右移 2 位
    short rightShiftShort = shortValue >> 2;
    
    // 按 unsigned short 类型左移 2 位
    unsigned short leftShiftUShort = (unsigned short)shortValue << 2;
    
    // 按 unsigned short 类型右移 2 位
    unsigned short rightShiftUShort = (unsigned short)shortValue >> 2;
    
    // 打印输出各种操作的结果（十进制和十六进制形式）
    printf("short 左移 2 位\n 十进制: %d, 十六进制: %X\n", leftShiftShort, leftShiftShort);
    printf("short 右移 2 位\n 十进制: %d, 十六进制: %X\n", rightShiftShort, rightShiftShort);
    printf("unsigned short 左移 2 位\n 十进制: %u, 十六进制: %X\n", leftShiftUShort, leftShiftUShort);
    printf("unsigned short 右移 2 位\n 十进制: %u, 十六进制: %X\n", rightShiftUShort, rightShiftUShort);
    
    return 0;
}