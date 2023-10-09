# Time

### 题目描述

为了节约存储大小，需要把输入的日期改为目标格式输出 ~~都什么年代了还在用传统时间表示法？~~

举例:

- 输入: November 17 1968 Sunday 6 6 6
- 输出: Sun Nov 17 06:06:06 1968

### 输入格式

```
month day year weekday hour minute second
```

**其中 $0⩽ year ⩽9999$**

保证是公元后的合法日期

### 输出格式

```
Www Mmm dd hh:mm:ss yyyy
```

- `Www`: 3-letter abbreviated day of the week
- `Mmm`: 3-letter abbreviated month name
- `dd`: 2-digit day of the month
- `hh`: 2-digit hour
- `mm`: 2-digit minute
- `ss`: 2-digit second
- `yyyy`: 4-digit year

位数不足的，在前面补0.

### 测试样例

##### Input

------

```
November 17 1968 Sunday 6 6 6
```

##### Output

------

```
Sun Nov 17 06:06:06 1968
```

##### Input

------

```
September 29 22 Friday 12 0 0
```

##### Output

------

```
Fri Sep 29 12:00:00 0022
```

### 题目注解

**小心数据范围**



## 题解

1. 读取输入，包括月份（month）、日期（day）、年份（year）、星期几（weekday）、小时（hour）、分钟（minute）、秒（second）。
2. 创建一个映射表，将输入的星期几和月份名称映射到它们的缩写形式。例如，星期几 "Sunday" 映射到 "Sun"，月份 "November" 映射到 "Nov"。
3. 对于年份，确保它始终有4位，可以使用格式化字符串来实现这一点，例如 `%04d`。
4. 对于日期、小时、分钟和秒，确保它们始终有2位，并在需要时在前面补零。可以使用格式化字符串 `%02d` 来实现这一点。
5. 使用格式化字符串将所有部分组合起来，按照目标格式输出结果。

注意事项：

- 输入日期的各个部分都需要进行适当的格式化，以满足输出要求。
- 当年份、日期、小时、分钟和秒的位数不足时，需要在前面补零。
- 星期几和月份的名称需要映射到它们的缩写形式。