# Frequently Used Docker Commands

December 18, 2019 by Meepo, Docker

---

用最简单的命令，做最有价值的事情。

## 1.镜像

### 1.1 查看已有镜像

```bash
docker images
```

![avatar](http://meeposoft.cn/static/img/docker/dockerimages.png)

### 1.2 删除已有镜像

使用镜像的部分id，如：

```bash
docker rmi b7150
```

### 1.3 拉取镜像

```bash
docker pull python
```

### 1.4 创建镜像

需要事先写好dockerfile，dockerfile不再赘述。

```bash
docker build -t testimage .
```

## 2.容器

### 2.1 跑一个容器

冒号：表示映射，<操作系统>:<容器内部>

-v 表示挂在本地路径

```bash
docker run --name nginx80 -d -p 80:80 -v /root/nginx/conf:/etc/nginx/conf.d -v /root/nginx/html:/usr/share/nginx/html nginx
```

### 2.2 查看容器

```bash
docker ps -a
```

### 2.3 启动、停止、重启容器

使用容器的部分id，如：

```bash
docker start u3i27
docker stop u3i27
docker restart u3i27
```

### 2.4 删除容器

```bash
docker rm u3i27
```
