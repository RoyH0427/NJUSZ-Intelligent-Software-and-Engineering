# 说的道理 (reverse.c)

## 题目描述

请将给定的字符串**倒序输出**，并将字符串中的小写字母与大写字母**互转**，如 5AKiYARy -> YrayIka5

### 输入格式
共两行，

第一行为一个数字 len，表示字符串的长度，保证所有数据的 $len≤10^5$；
第二行为一个长度为 len 的字符串，仅含有 26 个英文字母的大小写与 10 个数字，无任何空白符。
### 输出格式
共一行，为倒序的，互转了大小写的字符串。

### 测试样例

##### Input

------

```
13
A0Miyu1SdDL24
```

##### Output

------

```
42ldDs1UYIm0a
```



## Code

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h> // 用于检测字符是否为大小写字母，并进行转换

int main() {
    int len;
    scanf("%d", &len); // 读取字符串的长度

    char str[len + 1]; // 创建足够长的字符串数组，加1是为了存储字符串的结束符'\0'
    scanf("%s", str); // 读取字符串

    for (int i = 0; i < len / 2; i++) {
        // 交换对称位置的字符
        char temp = str[i];
        str[i] = str[len - i - 1];
        str[len - i - 1] = temp;
    }

    for (int i = 0; i < len; i++) {
        // 将小写字母转为大写，大写字母转为小写
        if (islower(str[i])) {
            str[i] = toupper(str[i]);
        } else if (isupper(str[i])) {
            str[i] = tolower(str[i]);
        }
    }

    printf("%s\n", str); // 输出结果

    return 0;
}
```

