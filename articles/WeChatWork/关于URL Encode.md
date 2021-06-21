# 关于URL Encode

## 问题背景

做应用程序的企业微信扫码认证，构造了一个URL让用户通过企业微信进行扫码

https://xxxx/api/auth?state=MTAxLENOSko0MTM3NA%3d%3d,li yanan,null

期望：接口中获取到参数state=MTAxLENOSko0MTM3NA==,li yanan,null

问题：

+ 安卓扫描该URL，成功获取到MTAxLENOSko0MTM3NA==,li yanan,null
+ 苹果扫描该URL，获取到的值为MTAxLENOSko0MTM3NA%3d%3d,li yanan,null

## 问题分析

安卓企业微信扫码时，不会自动对URL进行Encode；

苹果企业微信扫码时，若参数中存在未转义的字符，会自动进行URL Encode。

（苹果、安卓表现不同，真是太坑了）

如：若将该url中的空格去掉，苹果企业微信将不会进行URL Encode

https://xxxx/api/auth?state=MTAxLENOSko0MTM3NA%3d%3d,liyanan,null

## 解决方案

### 1）去掉参数中的特殊字符

如li yanan是用户名，规定该应用程序中的用户名中不得出现特殊字符及空格。

### 2）对字符串进行Url Decode

```C#
var base64 = "MTAxLENOSko0MTM3NA%3d%3d";
Console.WriteLine(base64);
base64 = HttpUtility.UrlDecode(base64);
Console.WriteLine(base64);
base64 = HttpUtility.UrlDecode(base64);
Console.WriteLine(base64);

// MTAxLENOSko0MTM3NA%3d%3d
// MTAxLENOSko0MTM3NA==
// MTAxLENOSko0MTM3NA==
// 注：无法再次UrlDecode的字符串，HttpUtility.UrlDecode也不会报错。
```



