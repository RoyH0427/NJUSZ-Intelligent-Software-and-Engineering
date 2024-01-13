# Pi

### 题目描述

调用 C 语言中的数学函数库，分别用以下两种近似方式计算圆周率:

- [Formula @ wiki](https://en.wikipedia.org/wiki/Approximations_of_π#Miscellaneous_approximations)
  - $\pi = \frac{ln(640320^3 + 744)}{\sqrt{163}}$
- [Machin Formula @ wiki](https://en.wikipedia.org/wiki/Approximations_of_π#Machin-like_formula)
  - $\frac{\pi}{4} = 4arctan(\frac{1}{5}) + arctan(\frac{1}{9})$

要求:

- 每个结果占一行
- 小数点后均保留 15 位
  - 精度要求为 `double`
- 必须通过调用数学函数计算结果
  - 指定使用 `log()`, `sqrt()`, `atan()`, `sqrt()` 函数， **不要使用 `atan2()`**
  - 写在注释里假装调用了是不行哒，嘎嘎嘎

### 输入格式

无输入

### 输出格式

两行，每行一个小数

注意由于本题输出的是定值，所以无需考虑样例

### 测试样例

##### Input

------

```
 
```

##### Output

------

```

```



## 题解

### 思路

这个问题要求使用C语言的数学函数库来计算两种不同的圆周率近似值。我们需要调用`log()`、`sqrt()`、`atan()`和`pow()`等函数来计算这些值。

### 解题方法

1. 使用`log()`函数和`pow()`函数来计算第一种近似方式的圆周率 $\pi_1$。
2. 使用`atan()`函数来计算第二种近似方式的圆周率 $\pi_2$。
3. 输出结果，利用`%.15lf`保留15位小数。

### 复杂度

  - 时间复杂度：$O(1)$，因为只进行了一些基本的数学运算和函数调用。

- 空间复杂度：$O(1)$，因为只使用了几个额外的变量来存储结果。

### Code

```c
#include <stdio.h>
#include <math.h>

int main()
{
    double pi1, pi2;

    // 计算圆周率近似值1
    pi1 = (log(pow(640320.0, 3) + 744.0) / sqrt(163.0));

    // 计算圆周率近似值2
    pi2 = (4.0 * atan(1.0 / 5.0) - atan(1.0 / 239.0)) * 4;

    // 输出结果，保留15位小数
    printf("%.15lf\n%.15lf\n", pi1, pi2);

    return 0;
}
```

