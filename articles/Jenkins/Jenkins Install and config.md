# CentOS7安装JENKINS

## 1 安装JDK

```bash
yum install -y java
```

## 2 安装jenkins

添加Jenkins库到yum库，Jenkins将从这里下载安装。

```bash
wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo
# 导入key，否则无法安装
rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key
# 安装
yum install -y jenkins
# 安装（不检测key）
yum install jenkins -y --nogpgcheck

# 注：正常安装时可能会报错
# warning: /var/cache/yum/x86_64/7/jenkins/packages/jenkins-2.297-1.1.noarch.rpm: Header V4 RSA/SHA512 Signature, key ID 45f2c3d5: NOKEY
# 使用不检测key安装即可
```

## 3 相关设置

```bash
vi /etc/sysconfig/jenkins
# 设置端口项
JENKINS_PORT="8080"
# 设置运行用户(若需要高权限，可以设置root)
JENKINS_USER="root"
JENKINS_GROUP="root"
# jenkins用户加入root组
gpasswd -a root jenkins
```

## 4 启动JENKINS

```bash
service jenkins start 
service jenkins stop
service jenkins restart  
#或者  
systemctl start jenkins

# 查看jenkiins是否启动
ps aux|grep jenkins
```

## 5 开启防火墙端口

```bash
firewall-cmd --zone=public --add-port=8080/tcp --permanent
firewall-cmd --reload
```

