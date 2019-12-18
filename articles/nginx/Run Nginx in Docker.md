# Run Nginx in Docker

December 17, 2019 by Meepo, Nginx

---

## 1.拉取Nginx镜像

```bash
docker pull nginx
```

## 2.启动Nginx容器

nginx镜像的默认端口是80，外部端口可自己设定。

两个目录需要挂载本地目录

+ /etc/nginx/conf.d目录，该目录下的conf文件会被nginx加载，默认有default.conf文件。
+ /usr/share/nginx/html目录，nginx的默认资源文件路径。

```bash
docker run --name nginx1 -d -p 80:80 -v /root/nginx/conf:/etc/nginx/conf.d -v /root/nginx/html:/usr/share/nginx/html nginx
```
