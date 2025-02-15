# 疑犯追踪 (poi.c)

## 题目描述

现在有一个游戏，同学们扮演嫌犯，老师需要扮演的剧本是抓捕所有嫌犯，然后从各个嫌犯口中获知他“上头”那个是谁，最终揪出幕后主谋。

假设同学们编号为 1~n，每位同学会告诉老师自己上级的编号，如果一位同学没有上级，他报出的将会是自己的编号。

### 输入格式

第一行一个数 n（n≤100000），表示同学数(编号1~n)

第二行 n 个数，第 i 个数  $a_i$ 表示第 i 号同学的上级是编号为 $a_i$  的同学

数据保证不会出现“上级”闭环，保证数据随机

### 输出格式

一行 n 个数，表示每个同学的幕后主使的编号

### 测试样例

##### Input

------

```
7
2 3 3 4 5 5 6
```

##### Output

------

```
3 3 3 4 5 5 5
```

### 题目注解

**幕后主使的定义**: 报出的编号就是自己的同学

**某位同学的幕后主使**：如果1号的上级是2号，2号的上级是3号，3号没有上级，那么3号同学就是1号同学和2号同学犯罪的幕后主使



## 思路

这个问题可以通过图论的概念来解决，其中每个同学可以被视为一个节点，他们的“上级”关系则构成了一个有向图。关键在于理解并实现查找每个节点的“根节点”（即幕后主使），这里的根节点指的是在有向图中不再指向其他节点的节点。

### 解题思路

1. **理解问题结构**：
   - 同学们和他们的上级关系构成了一个有向图，其中节点是同学，边是上级关系。
   - 一个同学可能直接或间接地指向另一个同学作为上级，形成一系列的链条。
   - 幕后主使被定义为一个链条中的根节点（即该节点指向自身）。

2. **数据结构的选择**：
   - 使用一个数组 `superiors` 存储每个同学的上级。
   - 使用另一个数组 `masterminds` 存储每个同学的幕后主使（初始设为自己）。

3. **寻找幕后主使的算法**：
   - 对于每个同学，我们需要遍历他们的上级链条直到找到根节点。
   - 这可以通过递归实现：如果某个同学的上级是他自己，那他就是幕后主使；否则，递归地查询这个上级的幕后主使。

4. **优化**：
   - 在递归查找过程中，一旦找到某个同学的幕后主使，可以将这个信息存储起来。
   - 这样，当再次查询同一链条上的其他同学时，可以直接从 `masterminds` 数组中获取幕后主使，而无需重新遍历链条。

5. **实现输出**：
   - 最后，对于每个同学，输出他们的幕后主使。

### 代码实现

1. **读入数据**：输入同学数量和他们各自的上级编号。
2. **初始化**：每个同学的幕后主使初始设为自己。
3. **查找和存储幕后主使**：
   - 使用递归函数 `findMastermind` 遍历每个同学的上级链条，直到找到幕后主使。
   - 在找到幕后主使后，更新 `masterminds` 数组。
4. **输出结果**：对于每个同学，输出他们的幕后主使。

这种方法的优势在于它可以高效地处理大量的数据，因为它通过存储已经计算过的幕后主使来避免重复工作。