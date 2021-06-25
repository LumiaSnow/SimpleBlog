# Harbor搭建

官网手册

## 1 下载

可在 https://github.com/goharbor/harbor/releases 选择自己需要版本

```bash
wget https://github.com/goharbor/harbor/releases/download/v2.3.0/harbor-offline-installer-v2.3.0.tgz
```

## 2 创建SSL证书

```bash
# 创建证书目录，并赋予权限
mkdir -p /data/cert && chmod -R 777 /data/cert && cd /data/cert

# 生成私钥，需要设置密码
openssl genrsa -des3 -out harbor.key 2048

# 生成CA证书，需要输入密码
openssl req -sha512 -new \
    -subj "/C=CN/ST=JS/L=WX/O=zwx/OU=jhmy/CN=solution.toshiba-tec.com.cn" \
    -key harbor.key \
    -out harbor.csr

# 备份证书
cp harbor.key harbor.key.org

# 退掉私钥密码，以便docker访问（也可以参考官方进行双向认证）
openssl rsa -in harbor.key.org -out harbor.key

# 使用证书进行签名
openssl x509 -req -days 365 -in harbor.csr -signkey harbor.key -out harbor.crt
```

## 3 解压安装

```bash
# 解压
tar -zxvf harbor-offline-installer-v2.3.0.tgz

# Into harbor folder
cd harbor

# 修改harbor.yml.tmpl文件（测试环境版本）
# hostname: reg.mydomain.com 改为实际域名/内网IP，不能使用localhost / 127.0.0.1
hostname: 192.168.62.42
http:
  port: 80 # 改为自己需要的port
harbor_admin_password: Harbor12345 # 改为自己的密码
# https #测试环境中不开启https
#  port: 443

# 从tmpl文件创建harbor.yml
cp harbor.yml.tmpl harbor.yml

# 安装
./install.sh # http测试环境
./install.sh --with-notary # --with-notary限定必须https，用于生产环境
```

## 4 相关配置



## 5 使用

尝试访问harbor(测试环境)

http://192.168.62.42:8081

