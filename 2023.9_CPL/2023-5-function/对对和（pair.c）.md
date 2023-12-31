# 对对和（pair.c）

## 题目描述

小 z 有一个长度为 n $(1≤n≤10^6)$，的整数数组 $a = a_0,a_1,…,a_{n-1}$ 和一个长度为 m $(1≤m≤10^6)$ 的整数数组 $b = b_0,b_1,…,b_{m-1}$

小 z 在心里偷偷想了一个整数 t，现在他想要知道，从数组 a 和 b 中分别选取一个整数 $a_i$ 和 $b_j$，在满足 $t≥a_i+b_j$ 的情况下，$t -a_i-b_j$ 的值最小为多少。

这个问题对小 z 来说太难了，于是善良的老师给数组 a 施加了一些魔法，现在数组 a 中的数单调不减（请注意，数组 b 并不一定满足这个性质）。

现在，请你来帮助小 z 解决这个问题。

### 输入格式

输入包含三行。

第一行为三个整数，分别为 n,m,t ；

第二行包含 n 个整数，依次表示 $a_0,a_1,…,a_{n-1}$

第三行包含 m 个整数，依次表示 $b_0,b_1,…,b_{m-1}$

### 输出格式

输出一行一个整数，表示在满足 $t≥a_i+b_j$ 的情况下 $t -a_i-b_j$ 的最小值，如果找不到这样的 $a_i$ 和 $b_j$，输出 `-1` 。

### 测试样例

##### Input

------

```
4 3 9
1 2 3 4
9 6 2
```

##### Output

------

```
0
```

##### Input

------

```
1 1 1
1
1
```

##### Output

------

```
-1
```

##### Input

------

```
7 3 1000000000
0 0 0 0 0 0 1
9 111 22
```

##### Output

------

```
999999888
```

### 题目注解
保证所有出现的整数都在 int 范围内，$0≤a_i,b_j≤10^9 ,0≤t≤2×10^9$。



## 思路

### 1 双指针

1. **排序**
   - 由于数组 $a$ 已经是单调不减的，我们需要对数组 $b$ 进行排序。排序后，我们可以用双指针法有效地找到使 $t - (a_i + b_j)$ 最小的 $a_i$ 和 $b_j$。

2. **双指针**

   - **初始化两个指针**：一个指针 $i$ 遍历数组 $a$，另一个指针 $j$ 从数组 $b$ 的末尾开始。

   - **遍历数组**：当 $i$ 没有遍历完数组 $a$ 并且 $j$ 没有到数组 $b$ 的开头时，进行以下操作：
     - 计算 $sum = a_i + b_j$。
     - 如果 $sum$ 小于或等于 $t$，我们尝试更新答案并将 $i$ 加一。
     - 如果 $sum$ 大于 $t$，那么我们需要减小 $sum$ 的值，所以将 $j$ 减一。


3. **更新答案**
   - 在 $sum \leq t$ 的条件下，我们想让 $t - sum$ 尽可能小。因此，每次 $sum$ 符合条件时，我们都会尝试更新答案。
     

4. **输出答案**
   - 如果我们找到了符合条件的 $a_i$ 和 $b_j$，输出使 $t - (a_i + b_j)$ 最小的值。
   - 如果没有找到符合条件的 $a_i$ 和 $b_j$，输出 $-1$。

#### 解题思路示例：

考虑数组 $a = [1, 2, 3, 4]$ 和 $b = [9, 6, 2]$，且 $t = 9$。

- 排序数组 $b$ 后得到 $b = [2, 6, 9]$。

- 初始化 $i = 0$ 和 $j = 2$。

进行如下迭代：

- $i = 0$, $j = 2$：$a_i = 1$, $b_j = 9$，$sum = 10$（大于 9），$j$ 减一。
- $i = 0$, $j = 1$：$a_i = 1$, $b_j = 6$，$sum = 7$（小于等于 9），尝试更新答案并增加 $i$。
- $i = 1$, $j = 1$：$a_i = 2$, $b_j = 6$，$sum = 8$（小于等于 9），尝试更新答案并增加 $i$。
- $i = 2$, $j = 1$：$a_i = 3$, $b_j = 6$，$sum = 9$（小于等于 9），尝试更新答案并增加 $i$。

在这个例子中，我们找到了 $a_2 = 3$ 和 $b_1 = 6$ 使得 $t - (a_i + b_j) = 0$ 是最小的，所以输出 0。

### 2 二分查找

1. **对数组 $b$ 遍历**
   - 我们不需要对数组 $b$ 进行排序，而是直接遍历数组 $b$ 中的每一个元素 $b_j$。

2. **二分查找**

   - 我们已知数组 $a$ 是有序的（单调不减），我们可以利用这一特性进行二分查找。

   - 对于数组 $b$ 中的每一个元素 $b_j$，我们在数组 $a$ 中寻找一个元素 $a_i$，使得 $a_i+b_j \leq t$ 并且 $t-(a_i+b_j)$ 的值尽可能小。

   - 为实现这一目的，我们可以进行二分查找，寻找不超过 $t-b_j$ 的数组 $a$ 中的最大值。

	二分查找的步骤：

	- 初始化两个指针，`left` 和 `right`，分别指向数组 $a$ 的开始和结束：`left = 0` 和 `right = n-1`。
	- 当 `left` 不大于 `right` 时，进行以下操作：
		- 计算中间索引 `mid`：$ \text{mid} = \text{left} + \frac{\text{right} - \text{left}}{2} $
		- 如果 $a[\text{mid}] + b_j$ 小于等于 $t$，则将 `left` 更新为 `mid+1`。
		- 如果 $a[\text{mid}] + b_j$ 大于 $t$，则将 `right` 更新为 `mid-1`。

3. **更新答案**
   - 二分查找完成后，如果找到了满足条件的 $a_i$（即 `right` 指针指向的元素），我们可以计算 $t - (a_i + b_j)$。
   - 我们将这个差值与当前最小差值进行比较，如果这个新计算出的差值更小，我们就用它更新当前最小差值。
   - 如果在数组 $a$ 中没有找到满足条件的 $a_i$（即没有元素与 $b_j$ 的和不超过 $t$），则不更新当前最小差值。
   
   - 如果 `right` 指针指向一个有效索引（即 `right >= 0`），则：
     - 计算差值：$ \text{diff} = t - (a[\text{right}] + b_j) $
     - 如果这个差值小于当前最小差值，则更新当前最小差值：$ \text{minDiff} = \text{diff} $
   
   重复上述步骤，直到数组 $b$ 中的每个元素都被考虑过。最后，输出找到的最小差值，如果没有找到符合条件的元素对，输出 -1。
   
4. **输出答案**
   - 遍历完数组 $b$ 中的所有元素后，如果找到了符合条件的 $a_i$ 和 $b_j$，则输出使得 $t - (a_i + b_j)$ 最小的值；否则，输出 $-1$。

#### 解题思路示意：

假设 $a = [1, 2, 3, 4]$，$b = [9, 6, 2]$，且 $t = 9$。

- 遍历数组 $b$：
  - 当 $b_j = 9$ 时，在 $a$ 中二分查找：找到 $a_i = 1$，$a_i + b_j = 10$ 太大，所以 $i$ 减少；找到 $a_i = 1$，$a_i + b_j = 10$ 是当前最小值。
  - 当 $b_j = 6$ 时，在 $a$ 中二分查找：找到 $a_i = 3$，$a_i + b_j = 9$，这是一个更好的值，所以更新答案。
  - 当 $b_j = 2$ 时，在 $a$ 中二分查找：找到 $a_i = 4$，$a_i + b_j = 6$，没有改进，所以保持当前答案不变。

因此，答案是 $t - (a_i + b_j) = 9 - 9 = 0$。

