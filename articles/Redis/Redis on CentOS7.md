

## 安装

```bash
wget https://download.redis.io/releases/redis-6.2.4.tar.gz?_ga=2.237662150.712314985.1624432291-1615205430.1577429097

mv redis-6.2.4.tar.gz?_ga=2.237662150.712314985.1624432291-1615205430.1577429097 redis-6.2.4.tar.gz

tar -xzvf redis-6.2.4.tar.gz
cd redis-6.2.4
cd deps
make jemalloc
make hiredis
make linenoise
make lua
cd ..
make
make install


cd /root/redis-5.0.2
vi redis.conf

bind 127.0.0.1
修改为
#bind 127.0.0.1

# requirepass foobared
修改为
requirepass password(需要设置的密码)

daemonize no
修改为
daemonize yes

logfile ""
修改为指定的日志文件
logfile "/var/log/redis/6379.log"

cp /root/redis-6.2.4/redis.conf /etc/redis/redis.conf



vi /usr/lib/systemd/system/redis.service

[Unit]
Description=Redis 6379
After=syslog.target network.target
[Service]
Type=forking
PrivateTmp=yes
Restart=always
ExecStart=/usr/local/bin/redis-server /etc/redis/redis.conf
ExecStop=/usr/local/bin/redis-cli -h 127.0.0.1 -p 6379 -a jcon shutdown
User=root
Group=root
LimitCORE=infinity
LimitNOFILE=100000
LimitNPROC=100000
[Install]
WantedBy=multi-user.target


# 使服务自动运行
systemctl daemon-reload
systemctl enable redis
# 启动服务
systemctl restart redis
systemctl status redis
```

