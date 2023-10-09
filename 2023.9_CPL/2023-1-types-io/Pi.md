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
