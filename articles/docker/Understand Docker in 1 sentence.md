# Understand Docker in 1 sentence

December 18, 2019 by Meepo, Docker

---

用直白的语言，理解晦涩的概念。

## 1.Docker是什么

Docker可以简单理解成一个沙箱，我们的app跑在这个沙箱中。

## 2.Docker的好处

+ 省事：Docker是个自带运行环境的小箱子，省的自己装环境，且随时可以开启新箱子。
+ 方便：Docker提供集群功能，很方便的把多个小箱子分发给多个服务器，实现负载均衡、高可用。

## 3.Docker怎么玩的

+ 容器：小箱子在docker中叫做容器；
+ 镜像：容器自带运行环境，python和java的运行环境不同，所以创建python容器时要指定是python运行环境；
+ 仓库：镜像从哪来呢？docker官方有一个镜像仓库，里面有各种各样的镜像，你想得到的都有。

从仓库中下载镜像，再用镜像创建容器，再把我们自己的代码放进去跑。

## 4.Docker集群是咋玩的

使用Docker自带的集群工具，可以创建一个服务器组，并且让容器自动分发到每一台服务器上去跑，这就是Swarm。

## 5.Docker和虚拟机有啥区别

+ 资源更小：虚拟机跑的是完整的操作系统，Docker只跑相关软件；

## 6.如何学好Docker

+ 多玩一玩就有了
+ 本文章只是粗浅的认识Docker，去看[Docker官方文档](https://www.docker.com/ "Docker官方文档")吧！
