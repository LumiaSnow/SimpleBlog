# 算法-入门篇（CSharp）

## 1 数字反转

基本思路：对10的n次方求余，求得对应位上的数字，反转输出

题目1：反转后保留最前面的0，如：340反转成043

思路：反转后拼成字符串

题目2：反转后省略最前面的0，如：340反转成43

思路：反转后形成数值类型，如：int

## 2 变量交换

传统思路：通过第三个变量

```C#
var a = 3;
var b = 4;
Console.WriteLine($"a {a}, b {b}");
var t = a;
a = b;
b = t;
Console.WriteLine($"a {a}, b {b}");

// a 3, b 4
// a 4, b 3
```

通过元组

```C#
var a = 3;
var b = 4;
Console.WriteLine($"a {a}, b {b}");
(a, b) = (b, a);
Console.WriteLine($"a {a}, b {b}");

// a 3, b 4
// a 4, b 3
```

## 3 输出所有形如AABB的四位完全平方数（A可以等于B）

方一：目标四位数的平方根与整数比较

```C#
for (var a = 1; a < 10; a++)
    for (var b = 0; b < 10; b++)
    {
        var aabb = a * 1000 + a * 100 + b * 10 + b;
        var aabbSqrt = Math.Sqrt(aabb);
        var aabbSqrtFloor = Math.Floor(aabbSqrt);
        if (aabbSqrtFloor == aabbSqrt)
            Console.Write($" {aabb},");
    }
```

方二：整数的平方是否符合AABB四位完全平方数规则

```C#
// 1100 = 33.几的平方
// 10000 = 100的平方
// 所以只需判断34 至 99即可
for (var n = 34; n < 100; n++)
{
    var n2 = n * n;
    if (n2 / 1000 == n2 % 1000 / 100 && n2 % 100 / 10 == n2 % 10)
        Console.Write($" {n2},");
}
```

## 4 阶乘之和的后6位

S = 1! + 2! + 3! + ... + n! ，给n，求S的后6位。

思路：关键点在于n过大时会造成数值溢出，这里可以应用一个数学知识，计算只包含加法、减法、乘法的整数表达式时，表达式结果对正整数m求余，等同于在每步计算之后对正整数m求余。

```C#
var n = 22;
var sum = 0;
for (var i = 1; i <= n; i++)
{
    var factorial = 1;
    for (var j = 1; j <= i; j++)
    {
        factorial = j * factorial % 1000000;
    }
    sum = (sum + factorial) % 1000000;
}
return sum;
```

优化：从22开始，后六位永远是940313，所以可以对n>=22开始的数直接返回

```c#
var n = 22;
if(n>=22)
    return 940313;
var sum = 0;
for (var i = 1; i <= n; i++)
{
    var factorial = 1;
    for (var j = 1; j <= i; j++)
    {
        factorial = j * factorial % 1000000;
    }
    sum = (sum + factorial) % 1000000;
}
return sum;
```



## 5 输出n的所有正因数。（n <= 10^12）

思路：如果i是n的因数，则n / i也是n的因数，所以只需要检测i从1到根号n即可。

``` C#

```

## 6 输入一个不超过10^9的正整数，输出它的位数。

如：17626，5位

``` C#
```

## 7 输出100-999中所有的水仙花数

若三位数ABC满足 ABC = A^k + B^k + C^k （k为正整数），则称之为水仙花数。

如：153 = 1^3 + 5^3 + 3^3

```C#
```

## 8 韩信点兵

韩信点兵时，让士兵站成3人一排，记录多出来的人数，再站成5人一排、7人一排，分别记录多出来的人数，便可知有多少人。若总人数在10-100之间，输入a,b,c (a<3,b<5,c<7)，输出可能的总人数。

```c#
```



