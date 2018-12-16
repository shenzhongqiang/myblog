Title: Docker初体验
url: docker-intro
save_as: docker-intro.html
Date: 2017-11-30
Category:
Authors: Zhongqiang Shen

最近的项目中用到了Docker，感觉超级好用。写下这篇文章作为自己学习的一个小结，也作为一篇Docker的入门介绍。

本文由以下内容组成：

+ 什么是Docker
+ Docker基本概念
+ 容器和传统VM的区别
+ 安装Docker
+ Docker命令简介
+ 创建Docker镜像
+ 多容器部署





#### 什么是Docker

Docker用Go语言开发实现，基于Linux内核的cgroup，namespace，和AUFS类的Union FS等技术，对进程进行封装隔离，属于操作系统层面的虚拟化技术。由于隔离的进程独立于宿主和其它的隔离的进程，因此也称其为容器。Docker 在容器的基础上，进行了进一步的封装，从文件系统、网络互联到进程隔离等等，极大的简化了容器的创建和维护。使得 Docker 技术比虚拟机技术更为轻便、快捷。




#### Docker基本概念

**镜像（image）**- 一个独立的文件系统，类似虚拟机里的镜像，包含运行时需要的系统、软件、代码、库、环境变量、配置文件等

**容器（container）**- 由镜像（image）创建的运行实例，类似虚拟机，可以对它执行启动、停止、删除等操作

**仓库（repository）**- 提供集中存储、镜像分发的服务，类似github。用户可以从仓库（repository）上传或下载镜像




#### 容器和传统VM的区别

**传统VM架构**

![]({static}/images/v2-7ee61067dfb9eac458ced806d2bd4fa6_r.jpg)

**容器架构**

![]({static}/images/v2-f211aa72def9826fb7050944bdd5c108_r.jpg)

每个虚拟机都有自己独立的操作系统，而不同的容器可以共享同一个操作系统。虚拟机面向操作系统，而Docker是面向应用的。容器一般被设计为运行一个主要进程，而不是管理多个进程集合。




#### 安装Docker

以ubuntu为例，运行以下命令

```bash
$ apt-get install docker
$ apt-get install docker.io

```

测试docker是否安装成功，运行

```bash
$ docker run hello-world

Hello from Docker.
This message shows that your installation appears to be working correctly.
...

```




#### Docker命令简介

以busybox镜像为例

**下载镜像**

```bash
$ docker pull busybox

```

这条命令从docker hub上下载busybox镜像存在本地

**列出本地的镜像**

```text
$ docker images
REPOSITORY
busybox                                     latest              6ad733544a63        3 weeks ago         1.129 MB

```

**基于镜像创建容器**

```bash
$ docker run busybox
$

```

这里没有任何输出，容器被创建后并没有运行任何命令，所以创建后就退出了

**在容器中执行命令**

```bash
$ docker run busybox echo "hello from busybox"
hello from busybox 

```

echo命令退出，容器也随即退出。

**显示所有的容器**

```bash
$ docker ps -a 
CONTAINER ID        IMAGE                                       COMMAND                  CREATED             STATUS                     PORTS               NAMES
0f6621b18dbe        busybox                                     "sh"                     3 minutes ago       Exited (0) 3 minutes ago                       desperate_torvalds

```

**显示正在运行的容器**

```bash
$ docker run -d busybox top # 启动一个容器，容器中运行top命令，这里-d表示detach模式
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
27c2844e3a5d        busybox             "top"               5 minutes ago       Up 5 minutes                            sleepy_wilson

```

**在容器中运行命令**

```bash
$ docker run -it busybox # -it表示连接到容器中的tty
/ # ls
bin   dev   etc   home  proc  root  sys   tmp   usr   var
/ # echo "hello"
hello

```

**删除容器**

```bash
$ docker rm  0f6621b18dbe
0f6621b18dbe

```

**删除镜像**

```bash
$ docker rmi busybox
Untagged: busybox:latest
Untagged: busybox@sha256:bbc3a03235220b170ba48a157dd097dd1379299370e1ed99ce976df0355d24f0
Deleted: sha256:6ad733544a6317992a6fac4eb19fe1df577d4dec7529efec28a5bd0edad0fd30
Deleted: sha256:0271b8eebde3fa9a6126b1f2335e170f902731ab4942f9f1914e77016540c7bb

```

**在Docker Hub上搜索镜像**

```bash
$ docker search busybox # 搜索image名字包含busybox的镜像
NAME                        DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
busybox                     Busybox base image.                             1149      [OK]
progrium/busybox                                                            66                   [OK]
hypriot/rpi-busybox-httpd   Raspberry Pi compatible Docker Image with ...   39
radial/busyboxplus          Full-chain, Internet enabled, busybox made...   16                   [OK]
hypriot/armhf-busybox       Busybox base image for ARM.                     8
armhf/busybox               Busybox base image.                             4
arm32v7/busybox             Busybox base image.                             3
...

```

**检查容器中的命令输出**

```bash
$ docker run -d busybox top # 启动一个容器
$ docker logs 10b72de4bd77 # 查看容器中top的输出
Mem: 8700192K used, 15989388K free, 247764K shrd, 299432K buff, 6261884K cached
CPU:  0.0% usr  0.1% sys  0.0% nic 99.7% idle  0.0% io  0.0% irq  0.0% sirq
Load average: 0.16 0.09 0.11 1/363 6

```




#### 创建Docker镜像

Dockerfile可用来自动化Docker镜像的创建，它包含一系列指令来描述如何创建一个镜像。

这里我们来展示如何用Dockerfile创建一个zookeeper的镜像。

首先需要在Dockerfile中指定base镜像，FROM关键字用于指定base镜像。因为zookeeper要用到java，我们的镜像使用openjdk作为base

```docker
FROM openjdk

```

MAINTAINER关键字描述镜像的创建者

```docker
MAINTAINER Zhongqiang Shen

```

WORKDIR设置容器内的当前工作目录，如果不存在则创建目录

```docker
WORKDIR /tmp

```

启动zookeeper服务需要从官网下载zookeeper包，撰写conf/zoo.cfg，并启动zookeeper进程。ADD关键字将URL中的内容下载到指定目录中

```docker
ADD http://apache.osuosl.org/zookeeper/stable/zookeeper-3.4.10.tar.gz /tmp

```

RUN关键字可以在容器中运行命令。在容器中解压zookeeper包，并将加压后的包移到/opt/zookeeper位置

```docker
RUN tar -xzf zookeeper-3.4.10.tar.gz
RUN mv zookeeper-3.4.10 /opt/zookeeper

```

设置zookeeper的路径为当前的工作目录

```docker
WORKDIR /opt/zookeeper

```

撰写conf/zoo.cfg

```docker
RUN echo "tickTime=2000" >> conf/zoo.cfg
RUN echo "dataDir=/var/lib/zookeeper" >> conf/zoo.cfg
RUN echo "clientPort=2181" >> conf/zoo.cfg

```

暴露容器的2181端口，使用expose关键字

```docker
EXPOSE 2181

```

启动zookeeper进程，使用CMD关键字。start-foreground参数让zookeeper在前台运行，如果没有这个参数，.sh脚本退出后会导致容器也退出

```docker
CMD ["/opt/zookeeper/bin/zkServer.sh", "start-foreground"]

```

这里需要注意RUN和CMD的区别，RUN用于创建镜像的时候执行命令，每次执行命令都会创建新的镜像层。CMD用于指定容器启动后默认执行的命令和参数。

完整的Dockerfile是这样的：

```docker
FROM openjdk
MAINTAINER Zhongqiang Shen

WORKDIR /tmp
ADD http://apache.osuosl.org/zookeeper/stable/zookeeper-3.4.10.tar.gz /tmp
RUN tar -xzf zookeeper-3.4.10.tar.gz
RUN mv zookeeper-3.4.10 /opt/zookeeper
WORKDIR /opt/zookeeper
RUN echo "tickTime=2000" >> conf/zoo.cfg
RUN echo "dataDir=/var/lib/zookeeper" >> conf/zoo.cfg
RUN echo "clientPort=2181" >> conf/zoo.cfg
EXPOSE 2181
CMD ["/opt/zookeeper/bin/zkServer.sh", "start-foreground"]

```

创建完Dockerfile，就可以用下面的命令来创建镜像了

```bash
$ docker build -t zookeeper .
Sending build context to Docker daemon  5.632kB
Step 1/12 : FROM openjdk
latest: Pulling from library/openjdk
3e17c6eae66c: Pull complete
fdfb54153de7: Pull complete
a4ca6e73242a: Pull complete
93bd198d0a5f: Pull complete
ca4d78fb08d6: Pull complete
ad3d1bdcab4b: Pull complete
4853d1e6d0c1: Pull complete
49e4624ad45f: Pull complete
bcbcd4c3ef93: Pull complete
Digest: sha256:b89826260c9f5ebb94ebff7ef23720f2b6de9f879df52e91afd112f53f5f7531
Status: Downloaded newer image for openjdk:latest
 ---> 377371113dab
Step 2/12 : MAINTAINER zhongqiang Shen
 ---> Running in 03bf1c8ef563
 ---> 7cd7ffa57b0c
Removing intermediate container 03bf1c8ef563
Step 3/12 : WORKDIR /tmp
 ---> b180924d0413
Removing intermediate container 1461e2b93f70
Step 4/12 : ADD http://apache.osuosl.org/zookeeper/stable/zookeeper-3.4.10.tar.gz /tmp
Downloading [==================================================>]  35.04MB/35.04MB
 ---> c2858e418073
Step 5/12 : RUN tar -xzf zookeeper-3.4.10.tar.gz
 ---> Running in 0cb7b253c12f
 ---> 0f7afb29ae74
Removing intermediate container 0cb7b253c12f
Step 6/12 : RUN mv zookeeper-3.4.10 /opt/zookeeper
 ---> Running in 68ce7228ca7e
 ---> 65d309c5340a
Removing intermediate container 68ce7228ca7e
Step 7/12 : WORKDIR /opt/zookeeper
 ---> b2dbec2aed3c
Removing intermediate container 8ac9df07f732
Step 8/12 : RUN echo "tickTime=2000" >> conf/zoo.cfg
 ---> Running in ef1d9dd5269a
 ---> 0c20dd205282
Removing intermediate container ef1d9dd5269a
Step 9/12 : RUN echo "dataDir=/var/lib/zookeeper" >> conf/zoo.cfg
 ---> Running in 7dcdb7eb07b1
 ---> a0a0a7341dba
Removing intermediate container 7dcdb7eb07b1
Step 10/12 : RUN echo "clientPort=2181" >> conf/zoo.cfg
 ---> Running in c2b0127e5cca
 ---> 6f7564eeaf4f
Removing intermediate container c2b0127e5cca
Step 11/12 : EXPOSE 2181
 ---> Running in cd97242108e5
 ---> eb91473e8a4c
Removing intermediate container cd97242108e5
Step 12/12 : CMD /opt/zookeeper/bin/zkServer.sh start-foreground
 ---> Running in 665686b5ec56
 ---> c4515a39ff83
Removing intermediate container 665686b5ec56
Successfully built c4515a39ff83
Successfully tagged zk:latest

```

这样一个docker镜像就创建好了。可以用下面的命令来启动它

```bash
$ docker run zookeeper

```




#### 多容器部署

一个应用通常由多个服务构成，将这些服务运行在容器中，就涉及到多个容器的部署。使用Docker Compose可以实现复杂的多容器应用的部署运行。

Docker Compose使用docker-compose.yml来定义服务。在docker-compose.yml中，所有的容器通过services来定义。

这里以kafka为例，kafka下层使用zookeeper作协调，因此这里需要定义zookeeper和kafka两个服务，先启动zookeeper，后启动kafka。

首先安装Docker Compose

```bash
$ apt-get install docker-compose

```

定义docker-compose.yml，如下：

```docker
version: '2'
services:
  zookeeper:
    container_name: iop-zookeeper
    image: jplock/zookeeper
    ports:
      - "2181:2181"
  kafka:
    container_name: iop-kafka
    image: wurstmeister/kafka
    environment:
      KAFKA_ZOOKEEPER_CONNECT: iop-zookeeper:2181
      KAFKA_CREATE_TOPICS: "metrics"
      KAFKA_ADVERTISED_HOST_NAME: localhost
      KAFKA_BROKER_ID: 1
    ports:
      - "9092:9092"
    links:
      - zookeeper

```

version指定Docker Compose的版本

container\_name指定容器的名字

image指定使用的镜像的名字，这里使用了docker hub上现有的Dockerfile来创建zookeeper和kafka的镜像

ports定义端口映射

environment设置环境变量

links定义容器之间的关联关系和依赖关系，这里kafka依赖于zookeeper，定义了这个依赖关系后，kafka启动前会先启动zookeeper

定义了docker-compose.yml文件后，就可以通过如下命令来一键启动服务

```bash
$ docker-compose up -d # -d表示后台模式运行服务
Pulling zookeeper (jplock/zookeeper:latest)...
latest: Pulling from jplock/zookeeper
b56ae66c2937: Pull complete
81cebc5bcaf8: Pull complete
3b27fd892ecb: Pull complete
40bb2918284a: Pull complete
Digest: sha256:5fe911a016393439a963bcab2f1cc03d107816ce2c6977bfa77bfb45edef5ad0
Status: Downloaded newer image for jplock/zookeeper:latest
Pulling kafka (wurstmeister/kafka:latest)...
latest: Pulling from wurstmeister/kafka
90f4dba627d6: Pull complete
11dbde1d93a0: Pull complete
c89218b0f06c: Pull complete
134279c08227: Pull complete
341b4d59b9c3: Pull complete
2ce0b628d981: Pull complete
82b065c991b8: Pull complete
d4f3b865c0e2: Pull complete
af829f3a4ec8: Pull complete
Digest: sha256:2aa183fd201d693e24d4d5d483b081fc2c62c198a7acb8484838328c83542c96
Status: Downloaded newer image for wurstmeister/kafka:latest
Creating iop-zookeeper ...
Creating iop-zookeeper ... done
Creating iop-kafka ...
Creating iop-kafka ... done

```

运行下列命令可以看到容器已启动

```bash
$ docker ps
CONTAINER ID        IMAGE                COMMAND                  CREATED             STATUS                             PORTS                                        NAMES
08a14f1c462a        wurstmeister/kafka   "start-kafka.sh"         28 seconds ago      Up 26 seconds                      0.0.0.0:9092->9092/tcp                       iop-kafka
f47d27f80aac        jplock/zookeeper     "/opt/zookeeper/bi..."   28 seconds ago      Up 27 seconds (health: starting)   2888/tcp, 0.0.0.0:2181->2181/tcp, 3888/tcp   iop-zookeeper

```

我们用python写个程序来测试一下启动的kafka服务

```python
from optparse import OptionParser
from kafka import KafkaConsumer
from kafka import KafkaProducer

parser = OptionParser()
parser.add_option("--action", action="store", choices=["produce", "consume"], type="choice", dest="action")
(options, args) = parser.parse_args()
if options.action == "produce":
    producer = KafkaProducer(bootstrap_servers="localhost:9092")
    for i in range(10):
            producer.send("test", str(i))
            producer.flush()
if options.action == "consume":
    consumer = KafkaConsumer("test", bootstrap_servers=["localhost:9092"], auto_offset_reset='earliest')
    for message in consumer:
        print message

```

上面的代码包含两个功能：向kafka队列生产数据和从kafka队列消费数据。

我们先向kafka队列生产数据

```bash
$ python test.py --action=produce

```

随后从kafka队列中消费数据，并打印出数据

```bash
$ python test.py --action=consume
ConsumerRecord(topic=u'test', partition=0, offset=0, timestamp=1511934733036, timestamp_type=0, key=None, value='0', checksum=1395146535, serialized_key_size=-1, serialized_value_size=1)
ConsumerRecord(topic=u'test', partition=0, offset=1, timestamp=1511934733045, timestamp_type=0, key=None, value='1', checksum=-7035501, serialized_key_size=-1, serialized_value_size=1)
ConsumerRecord(topic=u'test', partition=0, offset=2, timestamp=1511934733047, timestamp_type=0, key=None, value='2', checksum=1650992148, serialized_key_size=-1, serialized_value_size=1)
ConsumerRecord(topic=u'test', partition=0, offset=3, timestamp=1511934733049, timestamp_type=0, key=None, value='3', checksum=195437617, serialized_key_size=-1, serialized_value_size=1)
ConsumerRecord(topic=u'test', partition=0, offset=4, timestamp=1511934733051, timestamp_type=0, key=None, value='4', checksum=-1858641489, serialized_key_size=-1, serialized_value_size=1)
ConsumerRecord(topic=u'test', partition=0, offset=5, timestamp=1511934733053, timestamp_type=0, key=None, value='5', checksum=-349298306, serialized_key_size=-1, serialized_value_size=1)
ConsumerRecord(topic=u'test', partition=0, offset=6, timestamp=1511934733055, timestamp_type=0, key=None, value='6', checksum=1993515257, serialized_key_size=-1, serialized_value_size=1)
ConsumerRecord(topic=u'test', partition=0, offset=7, timestamp=1511934733057, timestamp_type=0, key=None, value='7', checksum=-824249467, serialized_key_size=-1, serialized_value_size=1)
ConsumerRecord(topic=u'test', partition=0, offset=8, timestamp=1511934733059, timestamp_type=0, key=None, value='8', checksum=1519664681, serialized_key_size=-1, serialized_value_size=1)
ConsumerRecord(topic=u'test', partition=0, offset=9, timestamp=1511934733061, timestamp_type=0, key=None, value='9', checksum=546143992, serialized_key_size=-1, serialized_value_size=1)

```

可以看到之前插入的数据被成功的读取到。




#### 总结

本文对Docker做了个简单介绍，包括Docker的基本概念、基本命令、如何创建Docker镜像、以及如何部署多容器。

除以上内容，Kubernetes也是Docker生态圈中的重要一员。Kubernetes是一个开源的容器集群管理系统，提供资源调度、均衡容灾、服务注册、动态扩缩容等功能，可以作为下一步学习的内容。

