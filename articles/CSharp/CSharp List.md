# CSharp List

## 1 List<父类>添加子类对象，JSON序列化表现

### 1.1 类定义及对象构建

```c#
public class BaseClass
{
    public string Name { get; set; }
}
public class Child1Class : BaseClass
{
    public string Child1Remark { get; set; }
}
public class Child2Class : BaseClass
{
    public string Child2Remark { get; set; }
}

var list = new List<BaseClass>();
list.Add(new BaseClass { Name = "BaseClass" });
list.Add(new Child1Class { Name = "Child1Class", Child1Remark = "111" });
list.Add(new Child2Class { Name = "Child2Class", Child2Remark = "222" });
```

### 1.2 使用System.Text序列化JSON

```C#
Console.WriteLine(JsonSerializer.Serialize(list));

// [{"Name":"BaseClass"},{"Name":"Child1Class"},{"Name":"Child2Class"}]
```

### 1.3 使用.net framework web api 返回序列化JSON

```C#
return Json(list);

//[
//  {
//    "Id": "parent"
//  },
//  {
//    "Name": "eeee",
//    "Id": "parent"
//  },
//  {
//    "Age": "dddd",
//    "Id": "parent"
//  }
//]
```

### 1.4 使用newtonsoft序列化JSON

```C#
Console.WriteLine(JsonConvert.SerializeObject(list));
// [{"Name":"BaseClass"},{"Child1Remark":"111","Name":"Child1Class"},{"Child2Remark":"222","Name":"Child2Class"}]
```

