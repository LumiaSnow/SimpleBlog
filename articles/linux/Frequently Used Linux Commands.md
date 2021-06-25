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

删除文件夹,-f表示无需确认直接删除，慎用

```bash
rm -rf somefolder1
```

## 7 查看内存占用

```bash
free –m
```

## 8 查看磁盘占用

```bash
# 查看整体
df –h

# 查看目录
du -h --max-depth=1


```

## 9 服务systemctl

```bash
# 列出所有service
systemctl list-units --type=service --all
# 列出所有的系统服务
systemctl
# 列出所有启动unit
systemctl list-units
# 列出所有启动文件
systemctl list-unit-files
# 列出所有service类型的unit
systemctl list-units –type=service –all
# 列出 cpu电源管理机制的服务
systemctl list-units –type=service –all grep cpu
# 列出所有target
systemctl list-units –type=target –all
# 查看当前运行级别target(mult-user)启动了哪些服务
systemctl list-dependencies
```

## 10 修改密码

```bash
# 修改当前用户密码
passwd

# 修改指定用户密码
passwd www
```

## 11 查找文件

```bash
find / -name rabbitmq-defaults
```

## 12 tail

```bash
# 查看某个文件的最后300行
tail xxxx.log -n 300
```

## 13 路由追踪 traceroute

```bash
yum install traceroute
traceroute libprint.sdyu.edu.cn

# on windows
tracert libprint.sdyu.edu.cn
```

## 14 解压文件

```bash
# tgz
tar -zxvf harbor-offline-installer-v2.3.0.tgz

```

