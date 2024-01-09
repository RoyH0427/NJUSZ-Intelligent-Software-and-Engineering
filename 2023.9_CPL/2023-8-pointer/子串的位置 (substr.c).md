# 子串的位置 (substr.c)

## 题目描述

给定两个字符串 S 和 T，其中 $0<∣T∣⩽∣S∣<10^5$

求 T 每次在 S 中出现时，T 的首字符在 S 中的下标（数据保证 T 至少在 S 中出现一次）

不允许使用数组实现。

### 输入格式

两行，每行一个字符串，代表 S 和 T

### 输出格式

输出一行，为多个整数（空格隔开），代表 T 每次在 S 中出现时，T 的首字符在 S 中的下标

### 测试样例

##### Input

------

```
114514
14
```

##### Output

------

```
1 4
```

##### Input

------

```
mymymyqtddt
mymy
```

##### Output

------

```
0 2
```



## Code

```c
#include <stdio.h>
#include <stdlib.h>

void find_substring(const char *S, const char *T)
{
    const char *s_ptr, *t_ptr, *start;

    for (s_ptr = S; *s_ptr != '\0'; ++s_ptr)
    {
        if (*s_ptr == *T)
        {
            start = s_ptr;
            t_ptr = T;
            while (*t_ptr != '\0' && *s_ptr == *t_ptr)
            {
                ++s_ptr;
                ++t_ptr;
            }
            if (*t_ptr == '\0')
            {
                printf("%ld ", start - S);
            }
            s_ptr = start; // Reset s_ptr to start of the match
        }
    }
    printf("\n");
}

int main()
{
    char *S = (char *)malloc(100000 * sizeof(char));
    char *T = (char *)malloc(100000 * sizeof(char));

    if (S == NULL || T == NULL)
    {
        printf("Memory allocation failed.\n");
        return 1;
    }

    scanf("%s", S);
    scanf("%s", T);

    find_substring(S, T);

    free(S);
    free(T);

    return 0;
}
```



这段代码的实现思路、时间复杂度和空间复杂度如下：

### 实现思路

1. **内存分配**：使用 `malloc` 动态分配两块内存，分别用于存储字符串 `S` 和 `T`。这避免了静态数组的使用。

2. **读取输入**：使用 `scanf` 函数读取用户输入的两个字符串 `S` 和 `T`。

3. **查找子串**：
    - 遍历字符串 `S` 的每个字符，使用指针 `s_ptr` 进行遍历。
    - 当在 `S` 中找到一个字符与 `T` 的首字符相匹配时，记录下这个起始位置（指针 `start`）。
    - 从这个起始位置开始，继续遍历 `S` 和 `T`，比较后续的字符是否相同，使用 `t_ptr` 遍历 `T`。
    - 如果 `T` 被完全遍历（`*t_ptr` 为 `\0`），则意味着在 `S` 中找到了一个匹配的子串。此时，打印出 `start` 相对于 `S` 起始位置的偏移量。
    - 如果在中途字符不匹配，重置 `s_ptr` 回到起始位置 `start`，继续遍历 `S`。

4. **释放内存**：在查找操作完成后，使用 `free` 函数释放之前分配的内存。

### 时间复杂度

- 对于字符串 `S` 中的每个字符，都可能需要与字符串 `T` 中的每个字符进行比较。
- 因此，时间复杂度为 O(n * m)，其中 n 是字符串 `S` 的长度，m 是字符串 `T` 的长度。

### 空间复杂度

- 空间复杂度主要由动态分配的内存决定。
- 分配了两块大小为 100000 字符的内存区域，用于存储字符串 `S` 和 `T`。
- 因此，空间复杂度为 O(1)，因为内存的分配大小不依赖于输入大小，而是固定的。

### 注意点

- 代码中没有考虑 `malloc` 分配内存失败的情况。在实际应用中，应当检查 `malloc` 返回的指针是否为 `NULL`，以确保内存分配成功。
- 该实现对于非常长的字符串可能不够高效，特别是当 `T` 出现在 `S` 中的频率较高时。这是因为每次找到匹配的第一个字符后，都要重新遍历 `T` 的剩余部分。