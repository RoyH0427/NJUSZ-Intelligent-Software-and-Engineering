# Prime Number Count

## 题目描述

输入`n`，输出`[1,n]`闭区间的素数个数。

### 输入格式

一行一个整数 n 。

对于30%的数据，保证 n ≤ 1000；

对于60%的数据，保证 n ≤ 10000；

对于90%的数据，保证 n ≤ 1000000；

对于100%的数据，保证 n ≤ 50000000。

### 输出格式

一行一个整数 m，表示所求素数个数。

### 测试样例

##### Input

------

```
2
```

##### Output

------

```
1
```

##### Input

------

```
17
```

##### Output

------

```
7
```

### 题目注解

对于较大的数据，尝试不用数组解决问题。

如何降低程序运行时间？



## 题解

### 思路 

要解决这个问题，我们可以使用埃拉托斯特尼筛法（Sieve of Eratosthenes）来找到素数，并计数它们的个数。

筛选法是一种非常有效的方法，可以在较短的时间内找出所有小于给定数的素数。

### 解题方法 

1. 创建一个长度为 `n+1` 的布尔数组，用于标记每个数是否是素数，初始都标记为 `true`。
2. 从2开始，遍历到 `n` 的平方根，对于每个数 `i`，如果它被标记为素数（即 `true`），则将其倍数标记为非素数（即 `false`）。
3. 最后，遍历整个数组，计算标记为素数的个数。

这种方法可以高效地找出素数，因为它避免了多次检查相同的数。

### 复杂度 

- 时间复杂度: $O(n \log \log n)$，这是筛选法的时间复杂度。
- 空间复杂度: $O(n)$，需要一个布尔数组来存储素数信息。

### Code

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int countPrimes(int n) {
    if (n <= 1) {
        return 0;
    }

    bool *isPrime = (bool *)malloc((n + 1) * sizeof(bool));
    if (isPrime == NULL) {
        return 0;
    }

    // Initialize the array, assuming all numbers are prime
    for (int i = 2; i <= n; i++) {
        isPrime[i] = true;
    }

    int count = 0;

    // Sieve of Eratosthenes
    for (int i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            // Mark multiples of i as not prime
            for (int j = i * i; j <= n; j += i) {
                isPrime[j] = false;
            }
        }
    }

    // Count prime numbers
    for (int i = 2; i <= n; i++) {
        if (isPrime[i]) {
            count++;
        }
    }

    free(isPrime);
    return count;
}

int main() {
    int n;
    scanf("%d", &n);

    int result = countPrimes(n);
    printf("%d\n", result);

    return 0;
}
```

