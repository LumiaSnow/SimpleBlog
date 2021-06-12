# Linux 防火墙设置

June 24, 2020 by Meepo, Linux

---

## 1.重启防火墙（重启生效）

```bash
firewall-cmd --reload
```

## 2.开启端口

```bash
firewall-cmd --zone=public --add-port=2377/tcp --permanent
```

## 3.关闭端口

```bash
firewall-cmd --zone=public --remove-port=2377/tcp --permanent
```
