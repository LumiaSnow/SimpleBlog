# Run Flask web server in Docker

December 18, 2019 by Meepo, Python

---

## 1.拉取Python镜像

```bash
docker pull python
```

## 2.创建Web Server镜像

```bash
docker build -t SimpleBlog .
```

## 3.启动Web Server容器

```bash
docker run --name SimpleBlog7781 -d -p 7781:7781 -v /root/Blog/articles:/usr/src/app/articles SimpleBlog
```
