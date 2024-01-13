# Time

## 题目描述

为了节约存储大小，需要把输入的日期改为目标格式输出 ~~都什么年代了还在用传统时间表示法？~~

举例:

- 输入: November 17 1968 Sunday 6 6 6
- 输出: Sun Nov 17 06:06:06 1968

## 输入格式

```
month day year weekday hour minute second
```

**其中 $0⩽ year ⩽9999$**

保证是公元后的合法日期

## 输出格式

```
Www Mmm dd hh:mm:ss yyyy
```

- `Www`: 3-letter abbreviated day of the week
- `Mmm`: 3-letter abbreviated month name
- `dd`: 2-digit day of the month
- `hh`: 2-digit hour
- `mm`: 2-digit minute
- `ss`: 2-digit second
- `yyyy`: 4-digit year

位数不足的，在前面补0.

## 测试样例

##### Input

------

```
November 17 1968 Sunday 6 6 6
```

##### Output

------

```
Sun Nov 17 06:06:06 1968
```

##### Input

------

```
September 29 22 Friday 12 0 0
```

##### Output

------

```
Fri Sep 29 12:00:00 0022
```

### 题目注解

**小心数据范围**



## 题解

### 思路

这个问题要求将输入的日期和时间格式转换为目标格式输出。我们可以使用格式化字符串来进行转换，并保证各个字段的位数正确。

### 解题方法

1. 从输入中读取月份、日期、年份、星期、小时、分钟和秒的值。
2. 使用格式化字符串来输出转换后的日期和时间格式，保证各个字段的位数正确。
3. 输出结果。

### 复杂度

  - 时间复杂度：$O(1)$，因为只进行了一些基本的输入和输出操作。

- 空间复杂度：$O(1)$，因为只使用了几个额外的变量来存储结果。

### Code

```c
#include <stdio.h>

int main()
{
    int dd, yyyy, hh, ss, mm;
    char mmm[10];
    char www[10];
    scanf("%s %d %d %s %d %d %d", mmm, &dd, &yyyy, www, &hh, &mm, &ss);
    printf("%.3s %.3s %.2d %.2d:%.2d:%.2d %.4d", www, mmm, dd, hh, mm, ss, yyyy);
    return 0;
}
```

