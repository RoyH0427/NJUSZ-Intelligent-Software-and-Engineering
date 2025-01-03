# 积分 (integration.c)

## 题目描述

注意本题允许误差。

辛普森积分法是一种用抛物线近似函数曲线来求定积分数值解的方法。把积分区间等分成若干段，对被积函数在每一段上使用[辛普森公式](https://baike.baidu.com/item/辛普森公式/9255085)：
$$
S(a, b) =  \int_{a}^{b} f(x) \approx \frac{4f(\frac{a+b}{2}) + f(a) + f(b)}{4} (b-a)
$$
就相当于根据其在每一段的两端和中点处的值近似为抛物线，逐段积分后加起来，即得到原定积分的数值解。

本题要求采用 [Adaptive Simpson's Method](https://en.wikipedia.org/wiki/Adaptive_Simpson's_method) 自适应辛普森法 以保证精度。

（上述**两处链接**均为出题时的参考材料，不需要阅读。）

### 自适应辛普森法

- 考虑当前在 (l,r) 上对 f(x) 进行积分，因为是数值积分，使用一个精度 ϵ 表示当前可接受的误差。

- 记 $mid = \frac{l+r}{2}$，使用辛普森公式求出 (l,r) 的积分数值 S，(l,mid) 段的积分数值 SL ，(mid,r) 段的积分数值 SR 。

- 若当前段与抛物线足够相似，即满足 $∣SL+SR−S∣≤15ϵ$ 的精度要求，则直接使用 $SL+SR+\frac{SL+SR-S}{15}$ 作为当前段积分的答案。

- 若当前段不满足精度要求，则直接按照 mid 将区间从中拆分为 (l,mid) 和 (mid,r) 两个区间分别进行上述处理并将结果相加。因为减少了区间长度，所以在处理上述两个子区间时需要动态调整 ϵ ，为简单起见可取 $ϵ′=\frac{ϵ}{2} $。

给出一个多项式函数，$f(x) = (a_nx^n+a_{n-1}x^{n-1}+...+a_1x+a_0)^p$，其中 n⩽20, $a_i$ 是整数，p∈−2,−1,1,2。请应用辛普森积分法计算函数在区间 (a,b) 上的定积分数值。允许误差范围为 $±10^{−4}$。

### 输入格式

第一行两个整数 n, p。

第二行 n+1 个整数 $a_0,a_1,a_2,...,a_n$。

第三行两个实数 a，b 即待积区间。

保证50%的数据，p=1，这种情况下你可以用原函数计算积分。

保证函数在区间上连续。

保证计算不爆 double 的范围与精度。

### 输出格式

一个浮点数，表示积分结果。

### 测试样例

##### Input

------

```
2 1
0 1 1
-1 1
```

##### Output

------

```
0.666667
```

##### Input

------

```
1 -1
0 1
1 2
```

##### Output

------

```
0.693147
```

### 题目注解

样例1的函数为 $f(x)=x^2+x$

样例2为 $f(x)= \frac{1}{x}$



## 思路

这道题目要求使用自适应辛普森积分法来求多项式函数在给定区间上的定积分。解题的核心思路涉及以下几个步骤：

### 1. 理解辛普森积分法

辛普森积分法是一种数值积分方法，用于近似函数在某个区间上的积分。它通过将积分区间分成小段，然后在每段上近似函数为二次多项式（抛物线），计算每段的积分，并将这些积分相加得到整个区间的近似积分值。

### 2. 自适应辛普森法

这种方法的关键在于动态地调整积分区间的大小，以达到所需的精度。具体步骤包括：

- **初步积分**：计算整个区间（a, b）上的辛普森积分近似值。
- **区间分割**：将区间分为两个子区间（a, mid）和（mid, b），其中 mid 是区间的中点。
- **精度检验**：比较两个子区间的辛普森积分之和与整个区间积分的差异。如果差异小于某个预设的阈值（精度要求），则认为当前的近似是可接受的。
- **递归调用**：如果差异大于阈值，则对每个子区间递归地执行以上步骤，每次递归时将误差容忍度减半。

### 3. 多项式函数的计算

多项式函数的形式为 $ f(x) = (a_nx^n + a_{n-1}x^{n-1} + ... + a_1x + a_0)^p $，其中 $ n \leq 20 $，$ a_i $ 是系数，$ p $ 是给定的指数。实现一个函数来计算给定 x 值时多项式的值。

### 4. 编程实现

具体编程实现时，需要注意以下几点：

- **读取输入**：首先从输入中读取多项式的次数、指数、系数以及积分的区间。
- **辛普森积分函数**：实现一个函数，根据辛普森公式计算给定区间的积分近似值。
- **自适应积分函数**：实现递归函数，根据自适应辛普森方法计算积分。
- **精度控制**：在递归中动态调整误差容忍度，以满足题目对精度的要求。

### 5. 调试和测试

最后，确保代码能够正确处理不同的输入案例，并在允许的误差范围内返回准确的积分结果。
