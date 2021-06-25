# Jenkins install by Docker

## 1 镜像

```bash
docker pull jenkinsci/blueocean
```

## 2 启动容器

```bash
docker run -u root --rm -d -p 8080:8080 -p 50000:50000 -v /var/jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkinsci/blueocean 

# Meepo在用
docker run -u root --rm -d -p 8090:8080 -p 50000:50000 -v /data/jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkinsci/blueocean 
```

## 3 防火墙开启端口

```bash
firewall-cmd --zone=public --add-port=8080/tcp --permanent
firewall-cmd --reload
```

