# 参数传递 (parse.c)

## 题目描述

命令行中，程序的参数传递是一个很现实的问题。

比如在 steam 中打开 CS:GO 国服时，steam 实际上做了这样的调用：

```
csgo64.exe -perfectworld -threads 4
```

其中第一项是实际运行的程序。被空格隔开的每一项都叫做“参数”。

在函数的一讲里，我们讲了函数的参数传递。计算机中的程序，其本质也都是函数，我们自然可以给它们传递参数。对于 C 程序而言，我们可以向 main 函数来传递参数：

```c
int main(int argc, char * argv[]);
```

其中 `argc` 表示参数的数量。`argv[]` 是一个数组，每一项是一个 `char *`，即字符串。命令行在进行上述例子中的调用的时候， 最终它以如下的参数调用了 csgo.exe 中的 `main()` 函数：

```c
argc = 4;  // 程序名也是参数之一
argv[0] = "csgo64.exe";
argv[1] = "-perfectworld";
argv[2] = "-threads";
argv[3] = "4";
argv[4] = NULL;  // 约定最后一个参数之后是空指针
```

本题中，要求你从命令的字符串中解析出指定的参数。需要你解出的参数有如下三种类型：

- 程序名（就是命令中的第一项）
- '-'后跟一个英文字母。
- '-'后跟一个英文字母，紧接着一个空格，再跟一个字符串表示这个参数的值。

比如，`gcc a.c -o a.out` （在 OJ 上，你的 C 语言程序也是这么编译出来的）

其中，`gcc` 是程序名。`a.c` 指 C 语言文件名（不构成上述类型中的任一种，因此不要求解析）

`-o` 的意思是指定输出的文件名。自然我们需要后跟一个文件名来给它一个值。

### 输入格式

第一行为解析规则，长度小于 128 字符，由`英文字母`、`英文字母+':'`两种格式组成。

独立的英文字母表示存在一个以该字母为名的参数。后跟':'的英文字母表示存在一个以该字母为名的参数且它需要后跟一个参数。

例如 `abABc:d:e`

其含义为，命令中可能会出现的参数有 `-a` `-b` `-A` `-B` `-c something` `-d something` `-e`

命令从前往后解析。假如出现 `-c -A` 这样的情况，你需要优先解析出 `-c`，并且把 `-A` 当作 `-c` 参数的值。

第二行为一行命令。长度在 1024 字符以内。可能重复出现需要解析的参数。

### 输出格式

若整条命令解析成功，则输出多行，第一行为程序名，接下来按照在命令里的先后顺序，输出参数列表（以及参数-值列表）。具体样式参考样例。

若某个参数需要值但是缺少了，则只输出一行：

> 程序名: option requires an argument -- 'x'

x 为解析过程中发现的缺少值的参数。

若出现了某个规则中未出现的参数，则只输出一行：

> 程序名: invalid option -- 'x'

只需要报告命令中的第一处错误即可。

### 测试样例

##### Input

------

```
cgo:Sv
gcc a.c -c -o a.o
```

##### Output

------

```
gcc
c
o=a.o
```

##### Input

------

```
fiIrdv
rm -r -f /
```

##### Output

------

```
rm
r
f
```

##### Input

------

```
hvVlfnrt:o:
mount -t
```

##### Output

------

```
mount: option requires an argument -- 't'
```

##### Input

------

```
aAbBc:d:e
this -c -d -e some useless arguments -c -A 
```

##### Output

------

```
this
c=-d
e
c=-A
```

##### Input

------

```
hvVlfnrt:o:
mount -k -t
```

##### Output

------

```
mount: invalid option -- 'k'
```

### 题目注解

被空格所分割的多个字符串，可以用连续的 `scanf("%s", s);` 进行读入。

使用 `fgets()`, `gets()`, `scanf("%c")` 这些就是给你自己增加难度并且挖大坑。

解析参数存在现成的库函数 `getopt()`。但是你几乎没办法用它来做这次 OJ。如果不想受尽折磨，请不要尝试。

~~最大的坑在于 getopt 的错误信息并不是输出到标准输出流。。~~

原版：

~~这个函数在 Linux 上，其行为和我们的答案是一致的。而我们的评测机是 Linux。也就是说你只要调库调对了，就可以很快解决。~~

~~在 Windows 上，其行为和答案的略有出入。但你依然可以使用 OJ 的 “自定测试” 功能，来看到你的程序在评测机上会跑出什么样的结果。~~

所以老实地选择自己实现，那上面这些你都不用担心。