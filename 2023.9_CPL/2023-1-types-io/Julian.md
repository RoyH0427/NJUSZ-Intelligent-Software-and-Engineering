# Julian

### 题目描述

儒略日 （ Julian Day ）是在儒略周期内以连续的日数计算时间的计时法，主要是天文学家在使用。

儒略日数（ Julian Day Number ，JDN ）的计算是从格林威治标准时间的中午开始，包含一个整天的时间，起点的时间（ 0 日）回溯至儒略历的西元前 4713 年 1 月 1 日中午 12 点。例如，2000 年 1 月 1 日的 12:00 是儒略日 2,451,545 。

给出公历中的年、月、日表示（year, month, day），儒略日数（JDN）可用如下公式计算：

$$
a=⌊ \frac{14−month}{12} ⌋ \\

y=year+4800−a \\

m = month+12a−3 \\

JDN = day + ⌊ \frac{153m+2}{5} ⌋ + 365y + ⌊ \frac{y}{4} ⌋ - ⌊ \frac{y}{100} ⌋ + ⌊ \frac{y}{400} ⌋ −32045
$$
给出公历中的一个年、月、日，请你写一个程序计算儒略日数。

### 输入格式

一行三个整数 year, month, day，用空格分隔。

### 输出格式

一行一个整数 JDN，即所求答案。

### 测试样例

##### Input

------

```
2000 1 1
```

##### Output

------

```
2451545
```

##### Input

------

```
2002 9 30
```

##### Output

------

```
2452548
```

### 题目注解

保证输入数据为公历 1900 年 1 月 1 日 到 2599 年 12 月 31 日之间的某一个合法日期。

⌊x⌋ 表示 对 x 向下取整，比如 ⌊3.2⌋=3, ⌊1.0⌋=1。



## 题解

### 思路

这个问题涉及到计算儒略日数（Julian Day Number，JDN），需要根据给定的公历日期计算。可以使用提供的公式来计算儒略日数。

### 解题方法

1. 从输入中读取年、月、日的整数值。
2. 使用提供的公式计算儒略日数：
   - 首先，计算变量 $a$，$a = \left\lfloor \frac{14 - \text{month}}{12} \right\rfloor$。
   - 然后，计算变量 $y$，$y = \text{year} + 4800 - a$。
   - 接着，计算变量 $m$，$m = \text{month} + 12a - 3$。
   - 最后，计算儒略日数 $JDN$，$JDN = \text{day} + \left\lfloor \frac{153m + 2}{5} \right\rfloor + 365y + \left\lfloor \frac{y}{4} \right\rfloor - \left\lfloor \frac{y}{100} \right\rfloor + \left\lfloor \frac{y}{400} \right\rfloor - 32045$。
3. 输出计算得到的儒略日数 $JDN$。

### 复杂度

  - 时间复杂度：$O(1)$，因为只进行了一些基本的数学运算和变量赋值。

- 空间复杂度：$O(1)$，因为只使用了几个额外的变量来存储结果。

### Code

```c
#include <stdio.h>

int main()
{
    int year, month, day;

    // 从输入中读取年、月、日
    scanf("%d %d %d", &year, &month, &day);

    // 计算儒略日数
    int a = (14 - month) / 12;
    int y = year + 4800 - a;
    int m = month + 12 * a - 3;
    int JDN = day + (153 * m + 2) / 5 + 365 * y + y / 4 - y / 100 + y / 400 - 32045;

    // 输出儒略日数
    printf("%d\n", JDN);

    return 0;
}
```