# JS

## 1 保留两位小数

```javascript
var num =2.446242342;
num = num.toFixed(2); 

// 2.45
```

## 2 路径返回上一级

如：/root/test 返回 /root，再返回 /

```javascript
function backFolder(path) {
    if (!path || path == "/")
        return "/";
    var index = files.path.lastIndexOf("/");
    var backPath = files.path.substring(0, index);
    if (!backPath)
        backPath = "/";
    return backPath;
}
```

