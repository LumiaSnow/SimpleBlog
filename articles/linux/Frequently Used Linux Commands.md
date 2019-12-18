# Frequently Used Linux Commands

December 17, 2019 by Meepo, Linux

---

用最简单的命令，做最有价值的事情。

## 1.远程连接服务器

```bash
ssh root@47.100.117.190
```

## 2.复制文件/文件夹到远程服务器

复制文件

```bash
scp test.txt root@47.100.117.190:/root/somefolder/
```

复制文件夹

```bash
scp -r somefolder1 root@47.100.117.190:/root/somefolder/
```

## 3.创建文件夹

```bash
mkdir foldername
```

## 4.移动文件/文件夹

移动文件

```bash
mv test.txt /root/somefolder/
```

移动文件夹

```bash
mv -r somefolder1 /root/somefolder/
```

## 5.复制文件/文件夹

复制文件

```bash
cp test.txt /root/somefolder/
```

复制文件夹

```bash
cp -r somefolder1 /root/somefolder/
```

## 6.删除文件/文件夹

删除文件

```bash
rm test.txt
```

删除文件夹

```bash
rm -r somefolder1
```
