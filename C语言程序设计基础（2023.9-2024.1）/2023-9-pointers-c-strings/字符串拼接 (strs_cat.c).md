# 字符串拼接 (strs_cat.c)

## 题目描述

给定两个字符串
$s_1,s_2(∣s_1∣,∣s_2∣≤1000)$，删除 $s_2$ 中开头最长的能和 $s_1$ 结尾匹配上的部分，再把两个字符串连接成一个字符串。

建议实现一个函数 void mystrcat(char*, char*)，从而把 $s_2$ 直接拼接在 $s_1$ 后边。

### 输入格式

第一行一个整数 $T (T≤500)$，表示一共有 T 组数据。

之后一共 T 行，每行两个字符串 $s_1$，$s_2$ 以空格间隔，字符串中不会出现空白符。

### 输出格式

一共 T 行，每行都是拼接后的字符串。

### 测试样例

##### Input

------

```
3
aabcd bcdee
ababa babac
{}}}_} }_{{{}}}
```

##### Output

------

```
aabcdee
ababac
{}}}_}_{{{}}}
```



## Code

```c
#include <stdio.h>
#include <string.h>

void mystrcat(char *s1, char *s2)
{
    int len1 = strlen(s1);
    int len2 = strlen(s2);
    int i, j;

    // 找到s1的结尾和s2的开头之间最长的匹配部分
    for (i = 0; i < len1; i++)
    {
        for (j = 0; j < len2 && i + j < len1 && s1[i + j] == s2[j]; j++)
            ;
        if (i + j == len1)
            break;
    }

    // 将s2的剩余部分拼接到s1的后面
    strcat(s1, s2 + j);
}

int main()
{
    int T;
    scanf("%d", &T);

    while (T--)
    {
        char s1[10001], s2[10001];
        scanf("%s %s", s1, s2);
        mystrcat(s1, s2);
        printf("%s\n", s1);
    }

    return 0;
}
```

