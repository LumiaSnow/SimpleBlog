# MYSQL环境变量

## 1 SQL_SAFE_UPDATES（SQL安全更新）

执行delete语句时提示错误

delete from shareprinter.sp_zfiles where status_conversion=2	Error Code: 1175. You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column.  To disable safe mode, toggle the option in Preferences -> SQL Editor and reconnect.	0.047 sec

解决方法，临时关掉SQL_SAFE_UPDATES

``` sql
SET SQL_SAFE_UPDATES = 0;
delete from shareprinter.sp_zfiles where status_conversion=2;
SET SQL_SAFE_UPDATES = 1;
```



