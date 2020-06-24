# C#装箱与拆箱

February 1, 2020 by Meepo, C#

---

## 值类型和引用类型

值类型：数据存储在栈上

- 有符号整数sbyte, short, int, long
- 无符号整数byte, ushort, uint, ulong
- 实数float, double, decimal
- char
- bool
- 自定义的struct
- 自定义的enum

引用类型：引用存储在栈上，数据存储在堆上

- string
- object
- 类（class）
- 接口（interface）
- 数组（Array）

所有对象的基类都是object，object是引用类型，为何int却是值类型？
确切的说值类型是继承自System.ValueType。

## 装箱与拆箱

装箱：值类型转换为引用类型
拆箱：引用类型转换为值类型

拆箱和装箱的过程会带来一些开销，所以要尽量避免。

开销从何而来？
装箱开销：值类型的数据存储在栈上，转换为引用类型时，需要在堆上分配一块数据空间，并且在栈上分配一块引用空间。
拆箱开销：引用类型类型转换为值类型时，需要在栈上分配一块数据空间。

代码示例：

```C#

int a = 1;
object obj = (object) a; //装箱
int b = (int) obj; //拆箱

```

那么问题来了，int类型继承自object，int对象可以调用object的方法，那在调用时是否会引发装箱？

## 值类型调用方法时的装箱问题

在C#中，如果调用的方法时值类型自己的，则不会发生装箱，如果调用的方法是父类的，则会装箱。

代码示例：

```C#

int a = 1;
string s = a.ToString(); //对象a在执行过程中不会装箱

```

ToString是object的方法，为何a在调用ToString时没有装箱？

看object对ToString的定义，发现这是一个虚方法（virtual）

```C#

//object 中的方法定义
public virtual string? ToString();

```

再看int的定义

```C#
//int 中的方法定义，重写了ToString
public override string ToString();

```

int对ToString进行了重写，所以不需要向下找父类object的ToString，不需要装箱。

再仔细看一下int的定义，重写了ToString, GetHashCode, Equals; 却没有对GetType进行重写。
所以int对象调用GetType时会先装箱找到object对象，再调用GetType方法。

## struct调用接口成员

如果一个struct继承自一个接口，那调用接口成员是否会引发装箱？

```C#

interface IIterface
{
    void Undo();
}
struct S : IIterface
{
    public void Undo() { }
}

class Program
{
    static void Main(string[] args)
    {
        S s = new S();
        s.Undo(); //不会装箱
        var i = (IIterface) s; //装箱
        i.Undo();
    }
}

```

结构体对象在调用接口成员时不会装箱，因为在自身中可以找到这个成员。
若使用接口对象引用该结构体实例，会进行装箱，因为接口是引用类型。

## 泛型避免拆装箱

最常见的情况是，一个方法的参数可能是多种类型，而代码逻辑是大致相同的，显然对方法进行重载是不友好的。
这时我们会想到使用所有类型的父类object作为参数类型。

```C#

public void Method(object obj)
{
    ...
}

```

问题来了，如果实参是int类型，那传进来的时候会先装箱成object类型，若需要在方法中使用该int，则需要再拆箱成int类型。

如何避免？

使用泛型，泛型在编译时就能确定类型，所以不需要到运行时再去做类型转换，避免了拆装箱问题。

```C#

public void Method<T>(T t)
{
    ...
}

```
