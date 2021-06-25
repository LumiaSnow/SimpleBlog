# MY SQL 索引

##  展示索引

```sql
SHOW INDEX FROM t_s_user;
```

## 删除索引

```sql
DROP INDEX usertypeid ON t_s_user;
```

## 前缀索引

有些字符串字段长度较长，比如给游客自动分配GUEST登录账号code "g1610545426223" ，且会用该字段进行查询，该字段不重复，所以需要创建索引，以优化查询效率；

是否需要对整个字符串创建索引？不建议，因为：

+ 索引体积较大
+ 影响增删改语句效率

如果字符串的长度从几十增大到几百，那以上缺点将更明显

解决方法：截取字符串前若干位创建索引，往往前10位左右的重复率已 < 10%，索引体积，查询效率，增删改效率可以比较好的平衡。

创建之前，先查看不重复率，选取不重复率高，且位数少的长度

```sql
select count(distinct left(code, 3))/count(*) as sel3,
count(distinct left(code, 10))/count(*) as sel10,
count(distinct left(code, 11))/count(*) as sel11,
count(distinct left(code, 12))/count(*) as sel12,
count(distinct left(code, 13))/count(*) as sel13,
count(distinct left(code, 14))/count(*) as sel14
from testtb;
```

创建前缀索引，比如前13位

``` sql
# 添加前缀索引
ALTER TABLE testtb ADD INDEX(code(13));
```



