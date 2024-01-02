#include <stdio.h>

int main() {
    // 给定一个 double 型数据 123456.789e5
    double doubleValue = 123456.789e5;
    
    // 转换为 float 类型的数据
    float floatValue = (float)doubleValue;
    
    // 打印输出转换结果（十进制和十六进制形式）
    printf("double 转换为 float\n 十进制: %f, 十六进制表示不适用\n", floatValue);
    
    return 0;
}