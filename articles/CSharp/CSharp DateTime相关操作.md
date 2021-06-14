# CSharp DateTime相关操作

## 1 获取当天0点

```c#
DateTime dt = DateTime.Now;
var day = DateTime.Now.Date;
Console.WriteLine(day.ToString());

// 2021/6/14 0:00:00
```

## 2 获取当前周

```c#
CultureInfo ci = new CultureInfo("zh-CN");
DateTime dt = DateTime.Now;
var weekIndex = ci.Calendar.GetWeekOfYear(dt, ci.DateTimeFormat.CalendarWeekRule, ci.DateTimeFormat.FirstDayOfWeek);
Console.WriteLine(weekIndex);

// 25
// 注：结果范围1-53
```

## 3 取某月第一天0点

```C#
DateTime dt = DateTime.Now;
dt.AddDays(1 - datetime.Day);
```

## 4 取某月最后一天0点

```C#
DateTime dt = DateTime.Now;
dt.AddDays(1 - datetime.Day).AddMonths(1).AddDays(-1);
```

## 5 AddMonths机制

1月31号，加1个月是2月28号（平年），加2个月是3月31号

```C#
DateTime m1 = new DateTime(2021, 1, 31);
Console.WriteLine(m1.ToString());
Console.WriteLine(m1.AddMonths(1).ToString());
Console.WriteLine(m1.AddMonths(2).ToString());

// 2021/1/31 0:00:00
// 2021/2/28 0:00:00
// 2021/3/31 0:00:00
```

2月28号，加1个月是3月28号

```C#
DateTime m2 = new DateTime(2021, 2, 28);
Console.WriteLine(m2.ToString());
Console.WriteLine(m2.AddMonths(1).ToString());

// 2021/2/28 0:00:00
// 2021/3/28 0:00:00
```





