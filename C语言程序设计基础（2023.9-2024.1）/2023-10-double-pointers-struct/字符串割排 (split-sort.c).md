# 字符串割排 (split-sort.c)

## 题目描述

**这是一道要你自学 `stdlib.h` 库中的快速排序函数 `qsort()` 的题目。**

参考链接：[qsort, qsort_s (cpl.icu)](https://ref.cpl.icu/c/algorithm/qsort.html)

对于一个给定的字符串，利用一个特定字符对其做分割，如 `'a,b,c,dd'` 可以用 `','` 分割为 `['a', 'b', 'c', 'dd']`，而后对其字典排序并输出。

建议实现 `char ** strsplit(char *, char *)` 函数和 `strcmp(char *, char *)`函数。

可以使用 `string.h` 库函数（如果你会的话）。

新增提示是，学习函数 `char *strtok(char *str, const char *delim);`

### 输入格式

两行，第一行为需要分割的字符串，第二行为用来分割的字符。不会出现空格。

保证两个分隔符之间一定有长度非0的子串，分割后的字符串数量小于100，分割后每个字符串长度**小于等于**100。

### 输出格式

多行，每行是一个被分割的字符串，字典序排好。

### 测试样例

##### Input

------

```
c,b,aaaa,1,00,10,DA,AD
,
```

##### Output

------

```
00
1
10
AD
DA
aaaa
b
c
```

### 题目注解

C 标准库



## 思路

这道题目的主要目标是将给定的字符串根据指定的分隔符分割成子字符串，然后对这些子字符串按字典序进行排序，最后输出排序后的结果。

### 1. 分割字符串
- **目的**：将一个长字符串分割成多个子字符串。
- **方法**：使用 `strtok` 函数。这个函数能够在给定的字符串中查找由 `delim` 指定的分隔符，并将字符串拆分为一系列的子字符串（令牌）。每次调用 `strtok` 时，它会返回指向下一个令牌的指针，如果没有更多的令牌，则返回 NULL。

### 2. 存储子字符串
- **目的**：存储所有分割得到的子字符串，以便后续排序。
- **方法**：创建一个字符串数组，用于存储指向每个子字符串的指针。由于题目限制，数组大小可以预设为 100。

### 3. 字典序排序
- **目的**：对分割得到的子字符串数组进行排序。
- **方法**：使用 `qsort` 函数。这是 C 标准库中的一个通用排序函数，它可以对任何类型的数组进行排序。为了使用 `qsort`，你需要提供一个比较函数，该函数用于确定两个数组元素的排序顺序。在这个案例中，比较函数将基于字符串比较函数 `strcmp` 来比较字符串。

### 4. 输出结果
- **目的**：输出排序后的字符串数组。
- **方法**：遍历排序后的字符串数组，逐个打印每个字符串。

### 注意事项
- 分割字符串时，确保不会超出数组的界限。
- `strtok` 函数会修改原始字符串，因此如果原始字符串以后还需要使用，应该先对其进行复制。
- 由于使用了静态数组来存储子字符串指针，所以这个解决方案不是线程安全的。在多线程环境中应考虑其他方法。
- `qsort` 的比较函数必须正确实现，否则排序可能不正确。

## Code

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SUBSTRS 100
#define MAX_SUBSTR_LEN 101

int cmp(const void *a, const void *b)
{
    return strcmp(*(const char **)a, *(const char **)b);
}

char **strsplit(char *str, const char *delim)
{
    static char *tokens[MAX_SUBSTRS];
    int count = 0;

    char *token = strtok(str, delim);
    while (token != NULL)
    {
        tokens[count++] = token;
        token = strtok(NULL, delim);
    }
    return tokens;
}

int main()
{
    char str[MAX_SUBSTR_LEN * MAX_SUBSTRS];
    char delim[2]; // 分割字符 + 结尾的 '\0'

    scanf("%s", str);
    scanf("%s", delim);

    char **substrs = strsplit(str, delim);

    // 计算分割后的字符串数量
    int count = 0;
    while (substrs[count] != NULL)
    {
        count++;
    }

    // 使用 qsort 排序
    qsort(substrs, count, sizeof(char *), cmp);

    // 输出结果
    for (int i = 0; i < count; i++)
    {
        printf("%s\n", substrs[i]);
    }

    return 0;
}
```

