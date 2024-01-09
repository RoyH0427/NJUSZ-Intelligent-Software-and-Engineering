# 不简单的词法分析器 (tokenizer.c)

## 题目描述

为了编译程序，我们第一步是要分析程序的每一个单词，把字符串序列转换为单词序列。

设定一种 y 语言，以英文分号 `;` 作为语句的分界，以空格作为单词的分界。其单词具有如下几种形式：

1、保留字 (**reserved**)。设定有16种，分别是 const, int, float, double, long, static, void, char, extern, return, break, enum, struct, typedef, union, goto

2、整数 (**integer**)。负号不属于整数的一部分，负号应为运算符，且负号不应与整数直接相连。

3、浮点数 (**float**)。负号不属于浮点数的一部分，同上。形如 1. 和 .1 的也算是浮点数

4、运算符 (**operator**)。设定11种，分别是 +, -, *, /, =, ==, !=, >=, <=, >, <

5、变量 (**variable**)。由字母、数字、下划线组成，但不能以数字开头

要求：每条语句输出一行，给出语句的分析结果；

一条语句的分析结果中，各成分以空格隔开。

如果存在不符合约定的成分，则输出 `Compile Error`。

不符合约定的成分例子比较多，比如：

```cpp
1..1   // 浮点数不能有两个小数点
-1   // 约定中整数不含负号
2a   // 变量开头不是数字
a || b   // 约定中没有 || 运算符
```

### 输入格式

不定长的字符串，小于 4096 字节，表示一段程序。

**句子成分的长度均只受总长度限制。想想整数！想想浮点数！**

### 输出格式

多行，每行分析一条语句。

如果整个程序中有不符合约定的地方，**仅**输出 `Compile Error`。

### 测试样例

##### Input

------

```
const int a = 1;float b = a + 1.1;
int a ; float b;
```

##### Output

------

```
reserved reserved variable operator integer
reserved variable operator variable operator float
reserved variable
reserved variable
```

##### Input

------

```
int a = true || false;
b = 2a + b;
1..0;
-1;
-0.1;
```

##### Output

------

```
Compile Error
```

##### Input

------

```
1 2 3 4 5;
double d = 34.324823748923642234234823764827346234239472398709825729386752439085610198236740584635092843;
```

##### Output

------

```
integer integer integer integer integer
reserved variable operator float
```

##### Input

------

```
char ch; return true; return 0;
```

##### Output

------

```
reserved variable
reserved variable
reserved integer
```

##### Input

------

```
1 + 1 - 1 * 1 / 1 = 1 == 1 != 1 >= 1 <= 1 > 1 < 1;
```

##### Output

------

```
integer operator integer operator integer operator integer operator integer operator integer operator integer operator integer operator integer operator integer operator integer operator integer
```

##### Input

------

```
const int float double long static void char extern return break enum struct typedef union goto;
```

##### Output

------

```
reserved reserved reserved reserved reserved reserved reserved reserved reserved reserved reserved reserved reserved reserved reserved reserved
```

### 题目注解

建议将样例 2 每一行单独输入进行测试，理应每一行都 `Compile Error`。

**本题推荐的思路是，用 scanf("%s", ) 来逐词读入->读入->处理->用一个字符串保存输出。但是空格与分号可能出现在任何位置。**

以下是一种可以拿到 9090 分的处理分号的方法：

```c
while (scanf("%s", s) != EOF) {
  char *position = strchr(s, ';');   // if there's no ';' in s, it returns NULL.
  if (position == NULL) process(s);
  else {
    process(s 中分号前的部分);
    在输出末尾加个换行;
    process(s 中分号后的部分);
  }
}
```

用 `scanf` 的好处之二是，你根本就不用考虑输入中的任何空格或换行，但满分的处理分号的方法需要你自己去探索，可以从上述方法进化而来。

你可以使用**字符串数组** `const char *reserved[LEN] = { "const", "int", ..., "goto" };` 存储保留字，作为通常的数组使用。这里的类型同时涉及 `*` 与 `[]`。

