# 聪明的保罗 (fifa.c)

## 题目描述

经过仔细的分析和 STFW ，Corax 收集到了 n 支球队的信息，包括球队名，11 位首发球员名单（不是真的）以及他们的攻、防、战术组织的实力评分，Corax 希望分别对他们的平均攻、防、战术组织实力评分进行排序，以此来玄学地预估本届世界杯最终可能夺冠的球队，由于 Corax 对网上的信息甄别不佳，有一些根本没有资格进入小组赛甚至根本不存在的球队也鱼目混珠了，同学们可不能像他一样。

### 输入格式

输入共 $12⋅n+1$ 行，第一行一个整数 n 表示 Corax 搜集到信息的球队支数（$n≤1000$）。

接下来是 n 支球队的信息，每支球队信息的第一行是一个长度不超过 20 的字符串，表示球队名，数据保证球队名各不相同，接下来 11 行是 11 位首发球员的姓名、进攻评分、防守评分和战术组织评分，姓名同样是一个长度不超过 20 的字符串，三个评分均为 $0≤x≤100$ 的整数，中间用空格隔开。

保证球队名和姓名中只会出现英文字母，保证按现有排序规则结果唯一。

### 输出格式

输出共 3 行，分别表示所有球队按照平均进攻评分，平均防守评分和平均战术组织评分降序排序的结果，用球队名来标识整支球队

### 测试样例

##### Input

------

```
2
China
Fanzhiyi 77 55 22
Zhaopeng 33 44 22
Zhangsan 20 19 11
Lisi 21 15 9
Wangwu 15 11 7
Haishen 10 9 8
Tuiqian 10 22 33
Lanjingling 10 22 33
Tang 10 22 33
Yao 10 22 33
Geneva 0 30 0
Netherlands
Gakpo 75 40 26
Depay 86 51 18
Bergwijn 74 51 28
Weghorst 80 56 27
Dejong 58 61 54
Koopmeiners 57 66 63
vanDijk 43 83 79
Deligt 42 70 71
Ake 42 74 78
Blind 44 59 61
Pasveer 0 61 0
```

##### Output

------

```
Netherlands China 
Netherlands China
Netherlands China
```

##### Input

------

```
3
Brazil
Neymar 94 70 27
Vinicius 76 43 24
Rodrygo 65 51 37
Jesus 84 71 37
Santos 59 44 29
Casemiro 59 78 66
Bruno 59 67 51
Marcos 47 82 84
Silva 38 84 87
Bremer 45 76 82
Alisson 0 84 0
Argentina
Messi 99 77 25
Dimaria 81 55 38
Dybala 88 73 26
Lautaro 82 56 19
Depaul 76 68 32
Fernandez 79 44 51
Macallister 66 49 44
Romero 42 78 80
Acuna 57 58 55
Tagliafico 45 61 73
Martinez 0 79 0
France
Mbappe 94 66 28
Dembele 82 46 23
Griezmann 84 67 35
Giroud 79 54 30
Tchouameni 51 46 60
Fofana 52 51 46
Rabiot 55 64 60
Kounde 38 62 69
Upamecano 40 78 77
Pavard 43 80 75
Lloris 0 65 0
```

##### Output

------

```
Argentina Brazil France 
Brazil Argentina France
Brazil France Argentina
```



## 思路

这个编程问题的主要任务是对收集到的足球队信息进行分析和排序。我们需要读取每个球队的数据，包括球队名称和每名球员的进攻、防守和战术组织评分。然后，我们要计算每支球队的平均进攻评分、平均防守评分和平均战术组织评分。最后，我们需要根据这些平均分数对球队进行排序，并输出排序结果。下面是解决这个问题的详细步骤：

### 1. 定义数据结构

首先，定义一个结构体 `Team` 来存储每支球队的信息。这个结构体应包含球队名称和三个评分（进攻、防守、战术组织）的平均值。

### 2. 读取输入

- 读取球队的数量 \( n \)。
- 对于每支球队：
  - 读取球队名称。
  - 对于球队中的每位球员：
    - 读取球员的姓名和三个评分（进攻、防守、战术组织）。
    - 将这些评分累加到相应的球队总评分中。

### 3. 计算平均分

对于每支球队，将其总进攻评分、总防守评分和总战术组织评分各自除以 11（球队中球员的数量），得到每支球队的平均分数。

### 4. 排序

- 使用 `qsort` 函数对球队数组进行排序。由于需要根据三个不同的标准进行排序（平均进攻评分、平均防守评分、平均战术组织评分），我们需要为每个标准编写一个比较函数。
- 每个比较函数应该根据相应的评分标准对两支球队进行比较，并返回排序所需的结果。

### 5. 输出结果

- 分别按照平均进攻评分、平均防守评分和平均战术组织评分的排序结果，输出所有球队的名称。
- 每个排序标准的结果应该输出在单独的一行上。

### 注意事项

- 输入数据的格式和有效性：需要确保正确地解析输入数据，并处理可能的格式错误。
- 排序的唯一性：根据题目要求，如果两支球队的某个平均评分相同，则按照球队名称的字典序进行排序，以保证排序结果的唯一性。
- 内存和性能考虑：由于球队数量可能达到 1000，因此在处理大量数据时需要注意内存使用和算法效率。



## Code

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
    char name[21];
    double attack;
    double defense;
    double tactic;
} Team;

int compareAttack(const void *a, const void *b)
{
    Team *teamA = (Team *)a;
    Team *teamB = (Team *)b;
    if (teamB->attack != teamA->attack)
    {
        return (teamB->attack > teamA->attack) ? 1 : -1;
    }
    return strcmp(teamA->name, teamB->name);
}

int compareDefense(const void *a, const void *b)
{
    Team *teamA = (Team *)a;
    Team *teamB = (Team *)b;
    if (teamB->defense != teamA->defense)
    {
        return (teamB->defense > teamA->defense) ? 1 : -1;
    }
    return strcmp(teamA->name, teamB->name);
}

int compareTactic(const void *a, const void *b)
{
    Team *teamA = (Team *)a;
    Team *teamB = (Team *)b;
    if (teamB->tactic != teamA->tactic)
    {
        return (teamB->tactic > teamA->tactic) ? 1 : -1;
    }
    return strcmp(teamA->name, teamB->name);
}

void sortAndPrint(Team teams[], int n, int (*cmp)(const void *, const void *))
{
    qsort(teams, n, sizeof(Team), cmp);
    for (int i = 0; i < n; i++)
    {
        if (i > 0)
        {
            printf(" ");
        }
        printf("%s", teams[i].name);
    }
    printf("\n");
}

int main()
{
    int n;
    scanf("%d", &n);
    Team teams[n];

    for (int i = 0; i < n; i++)
    {
        scanf("%s", teams[i].name);
        teams[i].attack = teams[i].defense = teams[i].tactic = 0;
        for (int j = 0; j < 11; j++)
        {
            char playerName[21];
            int attack, defense, tactic;
            scanf("%s %d %d %d", playerName, &attack, &defense, &tactic);
            teams[i].attack += attack;
            teams[i].defense += defense;
            teams[i].tactic += tactic;
        }
        teams[i].attack /= 11;
        teams[i].defense /= 11;
        teams[i].tactic /= 11;
    }

    sortAndPrint(teams, n, compareAttack);
    sortAndPrint(teams, n, compareDefense);
    sortAndPrint(teams, n, compareTactic);

    return 0;
}
```

