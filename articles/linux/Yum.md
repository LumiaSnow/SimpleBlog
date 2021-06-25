# YUM常用命令

# 1.安装

```bash
yum install -y [package]
```

# 2 查询

```bash
# 使用 yum 查找软件包 
yum search [package]
# 列出所有可安装的软件包 
yum list [package]
# 列出所有可更新的软件包 
yum list updates 
yum list updates [package]
# 列出所有已安装的软件包 
yum list installed
yum list installed [package]
```

## 3 YUM被占用问题

执行yum命令，报错：

Existing lock /var/run/yum.pid: another copy is running as pid 2096.

解决：

```bash
rm -f /var/run/yum.pid
/sbin/service yum-updatesd restart
```

