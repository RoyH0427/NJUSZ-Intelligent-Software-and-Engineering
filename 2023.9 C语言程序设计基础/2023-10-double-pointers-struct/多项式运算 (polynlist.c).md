# 多项式运算 (polynlist.c)

## 题目描述

蚂蚁老师在教小蚂蚁十以内的加减法，这时蝗虫走过来问，假设有两个多项式 $P_1$，$P_2$，请计算 $P_1 + P_2$，$P_1-P_2$，$P_1 \times P_2$

例如，若 $P_1 = 3n^2+1$ 和 $P_2=n-1$，则

- $P_1 + P_2 = 3n^2+n$
- $P_1-P_2=3n^2-n+2$
- $P_1 \times P_2=3n^3-3n^2+n-1$

### 输入格式

输入包含多行，第一行是两个空格隔开的正整数 $p_1$，$p_2$，分别代表多项式 $P_1$，$P_2$ 的阶（$0<p_1, p_2⩽10000$）

第二行是一个长度不超过 10 的字符串，代表多项式的变量名，例如上面的 n

第二行是 $p_1+1$ 个空格隔开的整数，代表多项式 $P_1$ 的系数（从高位开始输入，保证最高次项系数不为 0）

第三行是 $p_2+1$ 个空格隔开的整数，代表多项式 $P_2$ 的系数（从高位开始输入，保证最高次项系数不为 0）

### 输出格式

输出包含三行，分别为 $P_1 + P_2$，$P_1-P_2$，$P_1 \times P_2$

输出格式：对于一个多项式 $P=a_pn^p+a_{p-1}n^{p-1}+ \dots + a_1n^1+a_0n^0$

- 除最高次项外，若项的系数为负数，则不输出前面的 `+`
- 除常数项外，系数为零的项不输出，系数为 ±1±1 的项不输出 11
- 使用 `n^p` 表示 n 的 p 次方（$p>1$），p 为 1 时只输出 `n`，p 为 0 时只输出系数

例如：多项式 $P=(-4) \cdot n^4 + (-3) \cdot n^3 + 0 \cdot n^2 + 1 \cdot n^1 + 8 \cdot n^0$ 输出为：`-4n^4-3n^3+n+8`

### 测试样例

##### Input

------

```
2 1
nn
3 0 1
1 -1
```

##### Output

------

```
3nn^2+nn
3nn^2-nn+2
3nn^3-3nn^2+nn-1
```

### 题目注解

数据保证计算结果不爆 int



## 思路

### 1. 解析输入并存储多项式
- 输入包括两个多项式的阶数、变量名和每个多项式的系数。
- 使用两个数组（如 `polynomial1` 和 `polynomial2`）分别存储两个多项式的系数。数组的索引代表多项式的指数，而对应的数组值代表该指数项的系数。

### 2. 多项式的加法和减法
- 加法和减法可以通过遍历两个多项式的每一项来完成。对于加法，对于每个指数，将两个多项式中相应指数的项的系数相加。减法类似，只是将系数相减。
- 通过遍历最高阶数（两个多项式阶数的最大值），逐一处理每个指数的系数。

### 3. 多项式的乘法
- 对于乘法，创建一个结果数组（如 `polynomialResult`），其大小是两个输入多项式阶数之和的两倍，这是因为乘法结果的最高可能阶数是输入多项式阶数之和。
- 使用两层循环分别遍历两个多项式的每一项。对于每一对项的组合，将两项的系数相乘，并将结果添加到结果数组的相应位置（即两项的指数之和的位置）。

### 4. 输出格式化
- 对于每个运算结果（加法、减法、乘法），按照题目要求的格式输出多项式。
- 输出时需要考虑系数（是否为1或-1）、指数（是否为0或1）以及项之间的符号（正或负）。
- 特别是在乘法中，由于可能会有多个相同指数的项，需要事先合并这些同类项。

### 5. 辅助函数
- 实现一个辅助函数（如 `printPolynomialTerm`）来处理多项式每一项的格式化输出。这个函数根据系数和指数的不同情况输出不同的格式。

### 注意事项

- 在处理多项式系数和指数时要注意细节，例如系数为0时不输出，系数为1或-1时的特殊处理，以及输出时符号的正确显示。
- 为了防止数组越界，需要正确管理多项式的最大可能阶数。
- 乘法的结果可能需要合并同类项，这在编程实现时需要特别注意。



## Code

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int polynomialResult[20005] = {0};
char variableName[41]; // 变量名

void printPolynomialTerm(int degree);

int main()
{
    struct PolynomialTerm
    {
        int isFirstTerm; // 标记是否是首项
    };
    struct PolynomialTerm termsFlag[54275];

    int degreeP1 = 0, degreeP2 = 0;
    scanf("%d %d", &degreeP1, &degreeP2);
    scanf("%s", variableName);

    int polynomial1[20005] = {0}, polynomial2[20005] = {0};

    for (int i = degreeP1; i >= 0; i--)
    {
        scanf("%d", &polynomial1[i]);
    }
    for (int i = degreeP2; i >= 0; i--)
    {
        scanf("%d", &polynomial2[i]);
    }
    int maxDegree = fmax(degreeP1, degreeP2);
    for (int i = maxDegree; i >= 0; i--)
    {
        polynomialResult[i] = polynomial1[i] + polynomial2[i];
        if (polynomialResult[i] != 0)
        {
            termsFlag[i].isFirstTerm = 1;
            break;
        }
    }
    memset(polynomialResult, 0, sizeof(polynomialResult));

    /*****************************************************加法*****************************************************/
    for (int i = maxDegree; i >= 0; i--)
    {
        polynomialResult[i] = polynomial1[i] + polynomial2[i];
        if (termsFlag[i].isFirstTerm == 1) // 首位
        {
            if (i >= 2)
            {
                printf("%d%s^%d", polynomialResult[i], variableName, i); // 多次幂
            }
            if (i == 1)
            {
                printf("%d%s", polynomialResult[i], variableName); // 一次幂
            }
            if (i == 0)
            {
                printf("%d", polynomialResult[i]); // 常数项
            }
        }
        else if (termsFlag[i].isFirstTerm != 1)
        {
            printPolynomialTerm(i);
        }
    }
    printf("\n");
    memset(polynomialResult, 0, sizeof(polynomialResult));

    /*****************************************************减法*****************************************************/
    for (int i = maxDegree; i >= 0; i--)
    {
        polynomialResult[i] = polynomial1[i] - polynomial2[i];
        if (termsFlag[i].isFirstTerm == 1) // 首位
        {
            if (i >= 2)
            {
                printf("%d%s^%d", polynomialResult[i], variableName, i); // 多次幂
            }
            if (i == 1)
            {
                printf("%d%s", polynomialResult[i], variableName); // 一次幂
            }
            if (i == 0)
            {
                printf("%d", polynomialResult[i]); // 常数项
            }
        }
        else if (termsFlag[i].isFirstTerm != 1)
        {
            printPolynomialTerm(i);
        }
    }
    printf("\n");
    memset(polynomialResult, 0, sizeof(polynomialResult));

    /*****************************************************乘法*****************************************************/
    for (int i = degreeP2; i >= 0; i--)
    {
        for (int j = degreeP1; j >= 0; j--)
        {
            polynomialResult[i + j] += polynomial2[i] * polynomial1[j];
        }
    }
    int m = degreeP1 + degreeP2;
    for (int i = m; i >= 0; i--)
    {
        if (i == m)
        {
            if (i >= 2)
            {
                printf("%d%s^%d", polynomialResult[i], variableName, i); // 多次幂
            }
            if (i == 1)
            {
                printf("%d%s", polynomialResult[i], variableName); // 一次幂
            }
            if (i == 0)
            {
                printf("%d", polynomialResult[i]); // 常数项
            }
        }
        else if (i <= m)
        {
            printPolynomialTerm(i);
        }
    }
    return 0;
}

void printPolynomialTerm(int degree)
{
    if (polynomialResult[degree] > 0) // 系数为正数
    {
        if (polynomialResult[degree] != 1) // 系数不为1
        {
            if (degree >= 2)
                printf("+%d%s^%d", polynomialResult[degree], variableName, degree); // 多次幂
            if (degree == 1)
                printf("+%d%s", polynomialResult[degree], variableName); // 一次幂
            if (degree == 0)
                printf("+%d", polynomialResult[degree]); // 常数项
        }
        else if (polynomialResult[degree] == 1) // 系数为1
        {
            if (degree >= 2)
                printf("+%s^%d", variableName, degree); // 多次幂
            if (degree == 1)
                printf("+%s", variableName); // 一次幂
            if (degree == 0)
                printf("+%d", polynomialResult[degree]); // 常数项
        }
    }
    else if (polynomialResult[degree] < 0) // 系数为负数
    {
        if (polynomialResult[degree] != -1) // 系数不为-1
        {
            if (degree >= 2)
                printf("%d%s^%d", polynomialResult[degree], variableName, degree); // 多次幂
            if (degree == 1)
                printf("%d%s", polynomialResult[degree], variableName); // 一次幂
            if (degree == 0)
                printf("%d", polynomialResult[degree]); // 常数项
        }
        else if (polynomialResult[degree] == -1) // 系数为-1
        {
            if (degree >= 2)
                printf("-%s^%d", variableName, degree); // 多次幂
            if (degree == 1)
                printf("-%s", variableName); // 一次幂
            if (degree == 0)
                printf("%d", polynomialResult[degree]); // 常数项
        }
    }
}
```

