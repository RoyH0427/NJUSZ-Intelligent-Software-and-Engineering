# SQL 优化的其它问题

## Where 子句的比较运算符

### 比较运算符的自动转化

比较运算符用于 `WHERE` 子句中，对数据进行过滤和筛选。优化器会尝试将一些比较操作转化为更高效的等价形式。

```
a = 1000
a = 500 + 500
a - 500 = 500
```

对于 `a = 500 + 500`，优化器可以自动将其转化为 `a = 1000`。

但是对于 `a - 500 = 500`，优化器无法转化，因为这是一个减法操作，而非单纯的比较操作。

在全表扫描时，比较操作的优化可以显著提高性能，而复杂的数学运算（如减法）则可能降低优化器的效率。

### 不同形式的比较语句对性能的影响

```
CREATE TABLE t AS SELECT * FROM dba_objects;
INSERT INTO t SELECT * FROM t;
```

统计2019年4月20日这一天每个用户下的对象个数。以下是三种查询方式：

1. 直接使用范围比较条件，效率较高

   ```
   SELECT COUNT(*) 
   FROM t
   WHERE created >= TO_DATE('2019-04-20 00:00:00', 'yyyy-mm-dd hh24:mi:ss')
     AND created < TO_DATE('2019-04-21 00:00:00', 'yyyy-mm-dd hh24:mi:ss')
   GROUP BY owner;
   ```

2. 通过 `TO_CHAR` 转换日期后进行比较，性能较低，因为转换操作会对每一行数据执行

   ```
   SELECT COUNT(*) 
   FROM t
   WHERE TO_CHAR(created, 'yyyy-mm-dd') = '2019-04-20'
   GROUP BY owner;
   ```

3. 使用 `TO_CHAR` 转换后加范围比较，同样会降低性能

   ```
   SELECT COUNT(*) 
   FROM t
   WHERE TO_CHAR(created, 'yyyy-mm-dd hh24:mi:ss') >= '2019-04-20 00:00:00'
     AND TO_CHAR(created, 'yyyy-mm-dd hh24:mi:ss') <= '2019-04-20 23:59:59'
   GROUP BY owner;
   ```

### 比较运算符的转化规则

1. `ANY` 的转化：

   ```sql
   sales_qty > ANY (:in_qty1, :in_qty2)
   sales_qty > :in_qty1 OR sales_qty > :in_qty2
   ```

2. `ALL` 的转化：

   ```sql
   sales_qty > ALL (:in_qty1, :in_qty2)
   sales_qty > :in_qty1 AND sales_qty > :in_qty2
   ```

3. 范围比较的转化：

   ```sql
   sales_qty BETWEEN 100 AND 200
   sales_qty >= 100 AND sales_qty <= 200
   ```

4. NOT 的转化：

   ```sql
   NOT (sal < 30000 OR comm IS NULL)
   sal >= 30000 AND comm IS NOT NULL
   ```

5. 子查询的转化：

   ```sql
   NOT deptno = (SELECT deptno FROM emp WHERE empno = 9527)
   deptno <> (SELECT deptno FROM emp WHERE empno = 9527)
   ```



## 大数据量查询的优化

越快剔除不需要的数据，查询的后续阶段必须处理的数据量就越少，查询效率就越高。

早期过滤条件的应用可以有效减少数据的处理量，从而提高整体查询性能。

```
SELECT …
FROM A, B, C, D, E1
WHERE (condition on E1)
  AND (join and other conditions)
UNION
SELECT …
FROM A, B, C, D, E2
WHERE (condition on E2)
  AND (join and other conditions);
```

```
SELECT …
FROM A, B, C, D,
  (SELECT …
   FROM E1
   WHERE (condition on E1)
   UNION
   SELECT …
   FROM E2
   WHERE (condition on E2)
  ) E
WHERE (joins and other conditions);
```

第一种写法：如果主查询中表 `A` 到 `D` 的数据量较大，多个独立查询执行时会增加IO和计算负担。

第二种写法：子查询结果先被优化，减少了主查询中需要处理的数据量。更适合在大数据量场景中使用



## 将子查询转换为 JOIN

适用条件：

- 子查询不包含聚合函数。
- 子查询的条件选择是单一的，而非复杂的多条件组合。

```
SELECT payment 
FROM salary 
WHERE rank = (
  SELECT rank 
  FROM ranks 
  WHERE title = (
    SELECT title 
    FROM jobs 
    WHERE employee = '…'
  )
);
```

优化：

```
SELECT payment 
FROM salary, ranks, jobs
WHERE salary.rank = ranks.rank
  AND ranks.title = jobs.title
  AND jobs.employee = '…';
```

原查询包含两层嵌套子查询：第一层从 `jobs` 表查询 `title`。第二层基于第一层结果，从 `ranks` 表查询 `rank`。

通过 `JOIN` 将子查询重写为扁平化的连接查询：将 `salary`、`ranks` 和 `jobs` 表通过外键关系直接连接。数据库优化器可以选择最佳的连接路径，利用索引提升查询性能。



## 查询不存在的内容

使用 LEFT OUTER JOIN 与 NULL 检查



## 将聚合子查询转换为 JOIN 或内嵌视图







## 非关联子查询优化

将非关联子查询转换为内嵌视图