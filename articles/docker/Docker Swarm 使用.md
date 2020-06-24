# Docker Swarm 使用

June 24, 2020 by Meepo, Docker

---

## 1.CentOS 7

### 1.1 安装虚拟机

使用WMware新建虚拟机

### 1.2 更新yum

完成后先更新yum

```bash

sudo yum update

```

## 2 安装Docker

### 2.1 安装 DOCKER ENGINE

安装方法参照[Docker官方手册](https://docs.docker.com/engine/install/centos/)即可

安装yum-utils，为了使用yum-config-manager

```bash

sudo yum install -y yum-utils

sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo

```

### 2.2 安装 DOCKER Compose

安装方法参照[Docker官方手册](https://docs.docker.com/compose/install/)即可

下载Docker Compose

```bash

sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

```
