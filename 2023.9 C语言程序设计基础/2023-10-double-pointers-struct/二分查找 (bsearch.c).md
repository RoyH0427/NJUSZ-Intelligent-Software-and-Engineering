# 二分查找 (bsearch.c)

## 题目描述

**这是一道要你自学 stdlib.h 库中的二分查找函数 bsearch() 的题目。**

给定一个包含 n 个整数的数组 A，这 n 个整数各不相同且按升序排列（即，$A[0]<A[1]<…<A[n−1]$）。

现对该数组进行 q 次询问，每次询问输入一个数，需返回该数在数组 A 中的下标。

若该数不存在，则输出 −1。

### 输入格式

第一行两个 int 型整数 n, q ($1⩽n,q⩽1e6$)，分别表示数组大小和询问的次数。

第二行 n 个 int 型整数。保证升序排序，且互不相同。

接下来 q 行，每行一个 int 型整数，代表被查询的数。

### 输出格式

每行一个整数，为待查询整数在数组中的下标。

若待查询整数不存在，则输出 −1。

### 测试样例

##### Input

```
4 3
-1 2 3 4
-1
2
3
```

##### Output

```
0
1
2
```

### 题目注解

**数据规模与约定**

对于 60% 的数据，$1⩽n,q⩽10,000$

对于剩余 40% 的数据，$1⩽n,q⩽1,000,000$



## Code

```c
#include <stdio.h>
#include <stdlib.h>

// 二分查找函数
int binarySearch(int arr[], int n, int target)
{
    int left = 0, right = n - 1;

    while (left <= right)
    {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target)
        {
            return mid; // 找到了目标元素，返回下标
        }
        else if (arr[mid] < target)
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }

    return -1; // 目标元素不存在，返回-1
}

int main()
{
    int n, q;
    scanf("%d %d", &n, &q);

    int arr[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    for (int i = 0; i < q; i++)
    {
        int query;
        scanf("%d", &query);

        int result = binarySearch(arr, n, query);
        printf("%d\n", result);
    }

    return 0;
}
```

