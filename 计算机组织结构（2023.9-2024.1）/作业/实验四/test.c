#include <stdio.h>

int main() {
    // (1) unsigned int 型数据
    unsigned int result1 = 1 + 4294967295;
    unsigned int result2 = 1 - 4294967295;

    printf("(1) unsigned int 型数据:\n");
    printf("1 + 4294967295 = %u (十进制), 0x%08X (十六进制)\n", result1, result1);
    printf("1 - 4294967295 = %u (十进制), 0x%08X (十六进制)\n", result2, result2);

    // (2) int 型数据
    int result3 = 2147483647 + 1;
    int result4 = -2147483648 - 1;

    printf("\n(2) int 型数据:\n");
    printf("2147483647 + 1 = %d (十进制), 0x%08X (十六进制)\n", result3, result3);
    printf("-2147483648 - 1 = %d (十进制), 0x%08X (十六进制)\n", result4, result4);

    // (3) float 型数据
    float result5 = (1.0 + 123456.789e30) + (-123456.789e30);
    float result6 = 1.0 + (123456.789e30 + (-123456.789e30));

    printf("\n(3) float 型数据:\n");
    printf("(1.0 + 123456.789e30) + (-123456.789e30) = %f (十进制)\n", result5);
    printf("1.0 + (123456.789e30 + (-123456.789e30)) = %f (十进制)\n", result6);

    return 0;
}
