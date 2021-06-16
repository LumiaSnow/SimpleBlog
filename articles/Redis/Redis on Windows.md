# Redis on Windows

## 1 常用命令

```powershell
# 进入redis目录
# 安装
redis-server --service-install --service-name redis
# 卸载
redis-server --service-uninstall --service-name redis
# 连接测试
redis-cli.exe -h localhost -p 6379
```

