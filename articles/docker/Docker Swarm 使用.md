# Docker Swarm 使用

June 24, 2020 by Meepo, Docker

---

## 1.创建集群

### 1.1 Manager初始化

```bash

docker swarm init --listen-addr 192.168.62.42:2377 --advertise-addr 192.168.62.42

结果：
Swarm initialized: current node (mwtgv9m8skb3p6cwk5k4vkac8) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-0ck7yg4ehl64ca30bjgcc0juy86qdrwfg02yq73i28jwdhrgdk-bwuqhdwe7nk4n4lsosli5as3k 192.168.62.42:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.

```

### 1.2 Worker加入

```bash
docker swarm join --token SWMTKN-1-0ck7yg4ehl64ca30bjgcc0juy86qdrwfg02yq73i28jwdhrgdk-bwuqhdwe7nk4n4lsosli5as3k 192.168.62.42:2377
```

1）若提示该错误，需要开启Manager服务器的2377端口

```bash
Error response from daemon: rpc error: code = Unavailable desc = all SubConns are in TransientFailure, latest connection error: connection error: desc = "transport: Error while dialing dial tcp 192.168.62.42:2377: connect: no route to host"
```

开启Manager服务器的2377端口

```bash
firewall-cmd --zone=public --add-port=2377/tcp --permanent
firewall-cmd --reload
```

2）若提示该错误

```bash
Error response from daemon: error while validating Root CA Certificate: x509: certificate has expired or is not yet valid
```

查看证书时间

```bash
docker swarm ca | openssl x509 -noout -text
```

更新系统时间

```bash
yum install ntpdate
sudo ntpdate time.nist.gov
```

解散集群，再重新创建，再重新加入

```bash
docker swarm leave --force
```

### 1.3 管理节点查看节点信息

```bash
docker info
docker node ls
```

## 2 共享文件存储配置

### 2.1 安装插件vieux/sshfs

```bash
docker plugin install --grant-all-permissions vieux/sshfs
```

### 2.2 创建卷

```bash
docker volume create --driver vieux/sshfs \
  -o sshcmd=root@192.168.62.42:/root/logs \
  -o password=AAAaaa111 \
  sshvolume
```

查看

```bash
docker volume ls
```
