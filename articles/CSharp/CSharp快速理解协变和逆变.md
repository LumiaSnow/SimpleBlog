# C#快速理解协变和逆变

February 2, 2020 by Meepo, C#

---

## 定义

前提：如果A能隐式转换为B(A是B的子类)。
协变：X<A\>可以隐式转换成X<B\>，则称之为协变。
逆变：X<B\>可以隐式转换成X<A\>，则称之为逆变。

泛型out修饰符：该类型只能用作输出，如方法的返回值。
泛型in修饰符：该类型只能用作输入，如方法的参数。

## 代码示例

协变示例

```C#

//接口定义，含有一个只用于输出的类型T
interface IInterface<out T>
{
    T Undo();
}
class ClassInterface<T> : IInterface<T>
{
    public T Undo() => throw new NotImplementedException();
}

//类定义
class BaseClass {}
class SubClass : BaseClass {}

//执行
IInterface<SubClass> si = new ClassInterface<SubClass>();
IInterface<BaseClass> bi= si; //协变
BaseClass baseClass = bi.Undo();
```

逆变示例

```C#

//接口定义，含有一个只用于输入的类型T
interface IInterface<in T>
{
    void Undo(T t);
}
class ClassInterface<T> : IInterface<T>
{
    public void Undo(T t) => throw new NotImplementedException();
}

//类定义
class BaseClass {}
class SubClass : BaseClass {}

//执行
IInterface<BaseClass> bi = new ClassInterface<BaseClass>();
IInterface<SubClass> si= bi; //逆变
var subClass = new SubClass();
si.Undo(subClass);

```

## 为什么需要协变和逆变

协变和逆变存在的意义和引用转换差不多，也就是父类的引用可以指向子类实例。
好处就是可以节省大量的重复代码，像我们期待的一样去工作。

举个例子，如果我们写一个栈Stack，其中需要有Push方法和Pop方法。
如果我们需要往栈中放入多种类型，如何做？
1.可以定义栈中的元素都是object类型，但是Pop出来的元素需要我们自己转换成需要的类型去使用，而且可能存在拆箱问题。
2.使用泛型Stack<T\>

"Stack<T\>的协变、逆变"与"T的引用转换"是一个道理。
有时候我们需要父类引用承接子类实例，同样也会需要Stack<父类>引用承接Stack<子类>实例，这就是协变。

其实本质是一样的，只不过类型作为一个类型的泛型去使用时稍微复杂一点而已。

## 理解

### 理解协变

先看引用转换

```C#
//类定义
class BaseClass {}
class SubClass : BaseClass {}

//假设有一个方法
SubClass GetSubClassInstance()
{
    return new SubClass();
}

BaseClass baseClass = GetSubClassInstance(); //引用转换，父类引用子类实例
```

这个很好理解，而反过来用SubClass去引用BaseClass实例是非法的。
再看协变。

协变是对接口的out修饰的泛型说的，out指的是该类型只能用作输出（方法返回值）。
看上面实例中的代码:

```C#
IInterface<SubClass> si = new ClassInterface<SubClass>();
IInterface<BaseClass> bi= si; //协变
BaseClass baseClass = bi.Undo();
```

实例是ClassInterface<SubClass\>类型，引用是IInterface<BaseClass\>
所以bi.Undo()返回的对象是BaseClass的引用类型，而实例类型则是SubClass，这是符合引用转换的。

### 理解逆变

先看引用转换

```C#
//类定义
class BaseClass {}
class SubClass : BaseClass {}

//假设有一个方法
void PostBaseClassInstance(BaseClass bassClass)
{
}

var subClass = new SubClass();
PostBaseClassInstance(subClass); //引用转换
```

这个很好理解，而反过来用BaseClass实参传入SubClass形参是非法的。
再看逆变。

逆变是对接口的in修饰的泛型说的，in指的是该类型只能用作输入（方法参数）。
看上面实例中的代码:

```C#
IInterface<BaseClass> bi = new ClassInterface<BaseClass>();
IInterface<SubClass> si= bi; //逆变
var subClass = new SubClass();
si.Undo(subClass);
```

实例是ClassInterface<BaseClass\>类型，引用是IInterface<SubClass\>
所以si.Undo()的形参类型是BaseClass，而实参类型则是SubClass，这是符合引用转换的。

## 结论

协变和逆变不是凭空来的，是为了让泛型符合引用转换的规则，才规定了out和in修饰符，以及协变、逆变规则。

如果没有out和in做修饰，泛型T既可以作为输入又可以作为输出，但输入和输出只能满足一个合法变化。

想彻底理解协变和逆变，需要看书中的详解和示例。

## 历史问题

数组的协变

```C#
//类定义
class BaseClass {}
class SubClass : BaseClass {}
class SubClass2 : BaseClass {}

//执行
SubClass[] subClasses = new SubClass[3];
BaseClass[] baseClasses = subClasses; //合法，协变
var b1 = baseClasses[1]; //合法，输出BaseClass引用的SubClass类型（忽略空引用异常，仅是示例）
baseClasses[2] = new SubClass2(); //Runtime Error, 因为实际是SubClass类型的数组

```

可以从这个例子中理解一下为什么逆变协变需要规定out和in。
