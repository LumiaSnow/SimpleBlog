# MYSQL查询

## 1 日期查询

```sql
# 今天 2021-06-25
SELECT CURDATE();

# 查询日期部分
SELECT date(create_time) from tb;

# 30天前
SELECT DATE_SUB(CURDATE(), INTERVAL 30 DAY);

# 条件查询
DATE_SUB(CURDATE(), INTERVAL 30 DAY) <= date(时间字段名);

# 当前周
SELECT WEEK(now(),5) as now_week

# 当前年
SELECT YEAR(create_time) as year
```

## 2 快速生成数据库字典

```sql
SELECT
	t.TABLE_SCHEMA AS 库名,
	t.TABLE_NAME AS 表名,
	t.COLUMN_NAME AS 字段名,
	t.COLUMN_TYPE AS 数据类型,
	CASE IFNULL(t.COLUMN_DEFAULT,'Null') 
		WHEN '' THEN '空字符串' 
		WHEN 'Null' THEN 'NULL' 
		ELSE t.COLUMN_DEFAULT END  AS 默认值,
	CASE t.IS_NULLABLE WHEN 'YES' THEN '是' ELSE '否' END AS 是否允许为空,
	t.COLUMN_COMMENT AS 字段说明
FROM information_schema.COLUMNS t 
WHERE t.TABLE_SCHEMA='db_name' AND t.TABLE_NAME='tb_name';
```

