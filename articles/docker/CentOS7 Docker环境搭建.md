# CentOS7 Docker环境搭建

June 24, 2020 by Meepo, Docker

---

## 1.CentOS 7

### 1.1 安装虚拟机

使用WMware新建虚拟机

磁盘大小40G，内存2G，网络桥接（根据自己需要）

开启虚拟机

进入安装向导后，语言选择English（默认），Continue

SYSTEM - 点击 INSTALLATION DESTINATION - 点击磁盘 - 点击Done

SYSTEM - 点击 NETWORK & HOST NAME - 点击OFF变为ON - 点击Configure设置静态IP - 点击Done

Begin Installation

设置ROOT PASSWORD

可以不添加其他USER，看个人需要

等待安装完成

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

安装 DOCKER ENGINE

```bash

sudo yum install docker-ce docker-ce-cli containerd.io

```

启动 DOCKER

```bash

sudo systemctl start docker

```

设置 DOCKER 开机自启动

```bash

sudo systemctl enable docker

```

### 2.2 安装 DOCKER Compose

安装方法参照[Docker官方手册](https://docs.docker.com/compose/install/)即可

下载Docker Compose

```bash

sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

```

Apply executable permissions to the binary

```bash

sudo chmod +x /usr/local/bin/docker-compose

```

安装完成，试一下

```bash

docker-compose --version

```

如果找不到该执行文件，创建一个link

```bash

sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

```

### 2.3 安装 Docker Machine

安装方法参照[Docker官方手册](https://docs.docker.com/machine/install-machine/)即可

```bash

curl -L https://github.com/docker/machine/releases/download/v0.16.2/docker-machine-`uname -s`-`uname -m` >/tmp/docker-machine &&
    chmod +x /tmp/docker-machine &&
    sudo cp /tmp/docker-machine /usr/local/bin/docker-machine

sudo ln -s /usr/local/bin/docker-machine /usr/bin/docker-machine

sudo chmod -R 777 /usr/local/bin/docker-machine

```

### 2.4 安装 Docker Plugin vieux/sshfs

用于swarm模式下使用共享文件存储

```bash
docker plugin install --grant-all-permissions vieux/sshfs
```
