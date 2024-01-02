#include <stdio.h>

int main() {
    // 给定一个 float 型数据 123456.789e5
    float floatValue = 123456.789e5;
    
    // 转换为 double 类型的数据
    double doubleValue = floatValue;
    
    // 打印输出转换结果（十进制和十六进制形式）
    printf("float 转换为 double\n 十进制: %lf, 十六进制表示不适用\n", doubleValue);
    
    return 0;
}
