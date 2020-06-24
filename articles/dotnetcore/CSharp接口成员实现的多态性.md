# C#接口成员实现的多态性 (Dotnet Core)

January 31, 2020 by Meepo, C#

---

## 结论

先说结论，否则后面几百行可能会比较懵。

1.接口和基类的引用均具有多态性：

- 基类virtual隐式实现接口成员，子类override该成员。

2.接口的引用具有多态性，基类的引用不具有多态性：

- 基类和子类均继承自接口，不论显示实现或隐式实现。

3.其他情况均不具有多态性。

实现方式叙述：

- 隐式实现和显示实现本质上是相同的，默认情况下均不具有多态性。
- 显示实现无法指定public和virtual，若想实现多态，在基类中同时进行virtual隐式实现。
- 显示实现主要是用来对两个接口有重名成员时进行区分，此处不做讨论。

## 接口成员实现的几种方式

### 1.隐式实现

隐式实现：直接通过方法名进行实现，最常用的实现方式。

代码示例：

```C#
//接口定义
interface IInterface
{
    void Undo();
}
//隐式实现
class BaseClass : IInterface
{
    public void Undo() => Console.WriteLine("BaseClass");
}
class SubClass : BaseClass
{
    public void Undo() => Console.WriteLine("SubClass");
}

class Program
{
    static void Main(string[] args)
    {
        //接口方法实现的多态性
        var subClass = new SubClass();
        subClass.Undo();
        var baseClass = (BaseClass)subClass;
        baseClass.Undo();
        var iInterface = (IInterface)subClass;
        iInterface.Undo();
    }
}

//结果：
//SubClass
//BaseClass
//BaseClass

//分析：接口和基类引用均无多态性
//1）接口引用时，将执行基类的实现
//2）基类引用时，将执行基类的实现
//3）子类引用时，将执行子类的实现

```

### 2.隐式实现 + virtual

virtual：虚方法以实现多态

代码示例：

```C#
//接口定义
interface IInterface
{
    void Undo();
}
//隐式实现 + virtual
class BaseClass : IInterface
{
    public virtual void Undo()=>Console.WriteLine("BaseClass");
}
class SubClass : BaseClass
{
    public override void Undo()=>Console.WriteLine("SubClass");
}

class Program
{
    static void Main(string[] args)
    {
        //接口方法实现的多态性
        var subClass = new SubClass();
        subClass.Undo();
        var baseClass = (BaseClass)subClass;
        baseClass.Undo();
        var iInterface = (IInterface)subClass;
        iInterface.Undo();
    }
}

//结果：
//SubClass
//SubClass
//SubClass

//分析：接口和基类引用均具有多态性
//1）接口引用时，将执行子类的实现
//2）基类引用时，将执行子类的实现
//3）子类引用时，将执行子类的实现

```

***说明virtual的多态性对普通类和接口是相同的。***

### 3.显式实现

显示实现：通过{接口名.方法名}进行实现。显示实现时不能指定public和virtual。且该类必须继承接口，不能仅继承自基类。

#### 1）基类显示实现，子类隐式实现

代码示例：

```C#
//接口定义
interface IInterface
{
    void Undo();
}
//显示实现
class BaseClass : IInterface
{
    void IInterface.Undo() => Console.WriteLine("BaseClass");
}
class SubClass : BaseClass
{
    public void Undo() => Console.WriteLine("SubClass");
}

class Program
{
    static void Main(string[] args)
    {
        //接口方法实现的多态性
        var subClass = new SubClass();
        subClass.Undo();
        var iInterface = (IInterface)subClass;
        iInterface.Undo();
        //显示实现不能指定public，所以基类无法调用Undo(),需要通过接口调用
        var baseClass = new BaseClass();
        var iInterface2 = (IInterface)baseClass;
        iInterface2.Undo();
    }
}

//结果：
//SubClass
//BaseClass
//BaseClass

//分析：接口引用均多态性
//1）接口引用时，将执行基类的实现
//2）子类引用时，将执行子类的实现

```

***说明显示实现和隐式实现相同，不具有多态性。***

但显示实现时无法指定为virtual，那该如何实现多态？

#### 2）基类显示实现，子类隐式实现，同时子类也继承自接口

代码示例：

```C#
//接口定义
interface IInterface
{
    void Undo();
}
//显示实现
class BaseClass : IInterface
{
    void IInterface.Undo() => Console.WriteLine("BaseClass");
}
class SubClass : BaseClass, IInterface //子类也继承接口
{
    public void Undo() => Console.WriteLine("SubClass");
}

class Program
{
    static void Main(string[] args)
    {
        //接口方法实现的多态性
        var subClass = new SubClass();
        subClass.Undo();
        var iInterface = (IInterface)subClass;
        iInterface.Undo();
        //显示不能指定public，所以基类无法调用Undo(),需要通过接口调用
        var baseClass = new BaseClass();
        var iInterface2 = (IInterface)baseClass;
        iInterface2.Undo();
    }
}

//结果：
//SubClass
//SubClass
//BaseClass

//分析：接口引用有多态性
//1）接口引用时，将执行子类的实现
//2）子类引用时，将执行子类的实现

```

***说明当接口被基类显示实现，并且子类隐式实现时，同时子类也继承自接口，接口引用将调用子类的实现。***

若基类隐式实现，子类显示实现，又将如何？

#### 3）基类隐式实现，子类显示实现

代码示例：

```C#
//接口定义
interface IInterface
{
    void Undo();
}
//显示实现
class BaseClass : IInterface
{
    public void Undo() => Console.WriteLine("BaseClass");
}
class SubClass : BaseClass, IInterface //子类也继承接口
{
    void IInterface.Undo() => Console.WriteLine("SubClass");
}

class Program
{
    static void Main(string[] args)
    {
        //接口方法实现的多态性
        var subClass = new SubClass();
        subClass.Undo();
        var baseClass = (BaseClass)subClass;
        baseClass.Undo();
        var iInterface = (IInterface)subClass;
        iInterface.Undo();
    }
}

//结果：
//BaseClass
//BaseClass
//SubClass

//分析：接口引用有多态性，基类引用没有多态性。
//1）接口引用时，将执行子类的实现
//2）基类引用时，将执行基类的实现
//3）子类引用时，将执行基类的实现，因为子类的显示实现访问不到

```

***说明当接口被基类隐示实现，并子类显式实现时，接口引用将调用子类的实现。***

***所以当基类和子类是显示实现和隐式实现的关系，接口引用都将调用子类的实现。***

若基类和子类同时显示实现将如何？

代码示例：

```C#
//接口定义
interface IInterface
{
    void Undo();
}
//显示实现
class BaseClass : IInterface
{
    void IInterface.Undo() => Console.WriteLine("BaseClass");
}
class SubClass : BaseClass, IInterface //子类也继承接口
{
    void IInterface.Undo() => Console.WriteLine("SubClass");
}

class Program
{
    static void Main(string[] args)
    {
        //子类实例，接口引用调用
        var subClass = new SubClass();
        var iInterface = (IInterface)subClass;
        iInterface.Undo();
        //基类实例，接口引用调用
        var baseClass = new BaseClass();
        var iInterface2 = (IInterface)baseClass;
        iInterface2.Undo();
    }
}

//结果：
//SubClass
//BaseClass

//分析：接口引用有多态性
//1）接口引用时，将执行子类的实现。

```

***当基类和子类都显示实现时，接口引用将调用子类的实现，具有多态性。***

结论：

***显示实现和隐式实现本质上都没有多态性，多态性来自子类对接口的继承***

以此推论，若基类和子类均隐式实现，子类也继承自接口时，接口引用具有多态性，基类引用不具有多态性。
验证：

### 4.隐式实现 + 子类继承接口

代码示例：

```C#
//接口定义
interface IInterface
{
    void Undo();
}
//隐式实现
class BaseClass : IInterface
{
    public void Undo() => Console.WriteLine("BaseClass");
}
class SubClass : BaseClass, IInterface
{
    public void Undo() => Console.WriteLine("SubClass");
}

class Program
{
    static void Main(string[] args)
    {
        //接口方法实现的多态性
        var subClass = new SubClass();
        subClass.Undo();
        var baseClass = (BaseClass)subClass;
        baseClass.Undo();
        var iInterface = (IInterface)subClass;
        iInterface.Undo();
    }
}

//结果：
//SubClass
//BaseClass
//SubClass

//分析：接口引用具有多态性，基类引用不具有多态性
//1）接口引用时，将执行子类的实现
//2）基类引用时，将执行基类的实现
//3）子类引用时，将执行子类的实现

```

***只要子类同时继承自接口，接口引用就具有多态性***

问题来了，基类显示实现接口成员，子类不想继承自接口，如何实现多态性？

### 5.基类显示实现接口成员，子类的多态性

推荐写法是同时实现一个virtual的隐式实现。

代码示例：

```C#
//接口定义
interface IInterface
{
    void Undo();
}
//基类显示实现 + virtual隐式实现
class BaseClass : IInterface
{
    void IInterface.Undo() => Undo();
    public virtual void Undo() => Console.WriteLine("BaseClass");
}
class SubClass : BaseClass
{
    public override void Undo() => Console.WriteLine("SubClass");
}
class Program
{
    static void Main(string[] args)
    {
        //接口方法实现的多态性
        var subClass = new SubClass();
        subClass.Undo();
        var baseClass = (BaseClass)subClass;
        baseClass.Undo();
        var iInterface = (IInterface)subClass;
        iInterface.Undo();
    }
}

//结果：
//SubClass
//SubClass
//SubClass

//分析：接口引用和基类引用均具有多态性
//1）接口引用时，将执行子类的实现
//2）基类引用时，将执行子类的实现
//3）子类引用时，将执行子类的实现

```

其实只看篇头的结论就够了，只是在看书时看到书中举的例子一时没能理解透彻，故想了多种情况进行测试。
