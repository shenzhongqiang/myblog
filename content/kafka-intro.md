Title: Kafka入门简介
url: kafka-intro.html
save_as: kafka-intro.html
Date: 2018-03-22
Category:
Authors: Zhongqiang Shen

本文简单的介绍下kafka，主要包含以下部分：

+ 什么是Kafka
+ Kafka的基本概念
+ Kafka分布式架构
+ 配置单机版Kafka
+ 实验一：kafka-python实现生产者消费者
+ 实验二：消费组实现容错性机制
+ 实验三：offset管理





#### 什么是Kafka

Kafka是一个分布式流处理系统，流处理系统使它可以像消息队列一样publish或者subscribe消息，分布式提供了容错性，并发处理消息的机制。




#### Kafka的基本概念

kafka运行在集群上，集群包含一个或多个服务器。kafka把消息存在topic中，每一条消息包含键值（key），值（value）和时间戳（timestamp）。

kafka有以下一些基本概念：

**Producer **- 消息生产者，就是向kafka broker发消息的客户端。

**Consumer **- 消息消费者，是消息的使用方，负责消费Kafka服务器上的消息。

**Topic **- 主题，由用户定义并配置在Kafka服务器，用于建立Producer和Consumer之间的订阅关系。生产者发送消息到指定的Topic下，消息者从这个Topic下消费消息。

**Partition** - 消息分区，一个topic可以分为多个 partition，每个
partition是一个有序的队列。partition中的每条消息都会被分配一个有序的
id（offset）。

**Broker **- 一台kafka服务器就是一个broker。一个集群由多个broker组成。一个broker可以容纳多个topic。

**Consumer Group** - 消费者分组，用于归组同类消费者。每个consumer属于一个特定的consumer group，多个消费者可以共同消息一个Topic下的消息，每个消费者消费其中的部分消息，这些消费者就组成了一个分组，拥有同一个分组名称，通常也被称为消费者集群。

**Offset **- 消息在partition中的偏移量。每一条消息在partition都有唯一的偏移量，消息者可以指定偏移量来指定要消费的消息。




#### Kafka分布式架构

![]({static}/images/v2-f04083507c2860e62a686c3e868c719a_b.jpg)

如上图所示，kafka将topic中的消息存在不同的partition中。如果存在键值（key），消息按照键值（key）做分类存在不同的partiition中，如果不存在键值（key），消息按照轮询（Round Robin）机制存在不同的partition中。默认情况下，键值（key）决定了一条消息会被存在哪个partition中。

partition中的消息序列是有序的消息序列。kafka在partition使用偏移量（offset）来指定消息的位置。一个topic的一个partition只能被一个consumer group中的一个consumer消费，多个consumer消费同一个partition中的数据是不允许的，但是一个consumer可以消费多个partition中的数据。

kafka将partition的数据复制到不同的broker，提供了partition数据的备份。每一个partition都有一个broker作为leader，若干个broker作为follower。所有的数据读写都通过leader所在的服务器进行，并且leader在不同broker之间复制数据。




![]({static}/images/v2-e9b8513d58089eee6a131278ea949502_r.jpg)

上图中，对于Partition 0，broker 1是它的leader，broker 2和broker 3是follower。对于Partition 1，broker 2是它的leader，broker 1和broker 3是follower。




![]({static}/images/v2-a247b3d0f9fc622224f69bbdda1ab933_r.jpg)

在上图中，当有Client（也就是Producer）要写入数据到Partition 0时，会写入到leader Broker 1，Broker 1再将数据复制到follower Broker 2和Broker 3。




![]({static}/images/v2-9f15b48732fb965a8ed0644cc902bd67_r.jpg)

在上图中，Client向Partition 1中写入数据时，会写入到Broker 2，因为Broker 2是Partition 1的Leader，然后Broker 2再将数据复制到follower Broker 1和Broker 3中。

上图中的topic一共有3个partition，对每个partition的读写都由不同的broker处理，因此总的吞吐量得到了提升。




#### 配置单机版Kafka

这里我们使用kafka 0.10.0.0版本。

第一步：下载并解压包

```bash
$ wget https://archive.apache.org/dist/kafka/0.10.0.0/kafka_2.11-0.10.0.0.tgz
$ tar -xzf kafka_2.11-0.10.0.0.tgz
$ cd kafka_2.11-0.10.0.0

```




第二步：启动Kafka

kafka需要用到zookeeper，所以需要先启动zookeeper。我们这里使用下载包里自带的单机版zookeeper。

```bash
$ bin/zookeeper-server-start.sh config/zookeeper.properties
[2013-04-22 15:01:37,495] INFO Reading configuration from: config/zookeeper.properties (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
...

```

然后启动kafka

```bash
$ bin/kafka-server-start.sh config/server.properties
[2013-04-22 15:01:47,028] INFO Verifying properties (kafka.utils.VerifiableProperties)
[2013-04-22 15:01:47,051] INFO Property socket.send.buffer.bytes is overridden to 1048576 (kafka.utils.VerifiableProperties)
...

```




第三步：创建topic

```bash
$ bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test

```

查看创建的topic

```bash
$ bin/kafka-topics.sh --list --zookeeper localhost:2181
test

```




第四步：向topic中发送消息

```text
$ bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test
This is a message
This is another message

```




第五步：从topicc中消费消息

```bash
$ bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic test --from-beginning
This is a message
This is another message

```




#### 实验一：kafka-python实现生产者消费者

kafka-python是一个python的Kafka客户端，可以用来向kafka的topic发送消息、消费消息。

这个实验会实现一个producer和一个consumer，producer向kafka发送消息，consumer从topic中消费消息。结构如下图

![]({static}/images/v2-198d01ebb230395234999a3b8ac07502_r.jpg)




producer代码

```python
# producer.py
import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092")
i = 0
while True:
    ts = int(time.time() * 1000)
    producer.send(topic="test", value=str(i), key=str(i), timestamp_ms=ts)
    producer.flush()
    print i
    i += 1
    time.sleep(1)

```




consumer代码

```python
# consumer.py
from kafka import KafkaConsumer

consumer = KafkaConsumer("test", bootstrap_servers=["localhost:9092"])
for message in consumer:
    print message

```




接下来创建test topic

```bash
$ bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
Created topic "test".

```




打开两个窗口中，我们在window1中运行producer，如下

```bash
# window1
$ python producer.py
0
1
2
3
4
5
...

```




在window2中运行consumer，如下

```bash
# window2
$ python consumer.py
ConsumerRecord(topic=u'test', partition=0, offset=128, timestamp=1512554839806, timestamp_type=0, key='128', value='128', checksum=-1439508774, serialized_key_size=3, serialized_value_size=3)
ConsumerRecord(topic=u'test', partition=0, offset=129, timestamp=1512554840827, timestamp_type=0, key='129', value='129', checksum=1515993224, serialized_key_size=3, serialized_value_size=3)
ConsumerRecord(topic=u'test', partition=0, offset=130, timestamp=1512554841834, timestamp_type=0, key='130', value='130', checksum=453490213, serialized_key_size=3, serialized_value_size=3)
ConsumerRecord(topic=u'test', partition=0, offset=131, timestamp=1512554842841, timestamp_type=0, key='131', value='131', checksum=-632119731, serialized_key_size=3, serialized_value_size=3)
...

```

可以看到window2中的consumer成功的读到了producer写入的数据




#### 实验二：消费组实现容错性机制

这个实验将展示消费组的容错性的特点。这个实验中将创建一个有2个partition的topic，和2个consumer，这2个consumer共同消费同一个topic中的数据。结构如下所示

![]({static}/images/v2-c13a7ea159c44df872a5845c3cd3f6c6_r.jpg)




producer部分代码和实验一相同，这里不再重复。consumer需要指定所属的consumer group，代码如下

```python
# consumer.py
from kafka import KafkaConsumer

consumer = KafkaConsumer("test", bootstrap_servers=["localhost:9092"], group_id="testgoup")
for message in consumer:
    print message

```




接下来我们创建topic，名字test，设置partition数量为2

```text
$ bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 2 --topic test
Created topic "test".

```




打开三个窗口，一个窗口运行producer，还有两个窗口运行consumer。

运行consumer的两个窗口的输出如下：

```bash
# window1
$ python consumer.py
ConsumerRecord(topic=u'test', partition=0, offset=11, timestamp=1512556619298, timestamp_type=0, key='15', value='15', checksum=-1492440752, serialized_key_size=2, serialized_value_size=2)
ConsumerRecord(topic=u'test', partition=0, offset=12, timestamp=1512556621308, timestamp_type=0, key='17', value='17', checksum=-1029407634, serialized_key_size=2, serialized_value_size=2)
ConsumerRecord(topic=u'test', partition=0, offset=13, timestamp=1512556622316, timestamp_type=0, key='18', value='18', checksum=1544755853, serialized_key_size=2, serialized_value_size=2)
ConsumerRecord(topic=u'test', partition=0, offset=14, timestamp=1512556624326, timestamp_type=0, key='20', value='20', checksum=2130557725, serialized_key_size=2, serialized_value_size=2)
...


# window2
$ python consumer.py
ConsumerRecord(topic=u'test', partition=1, offset=6, timestamp=1512556617287, timestamp_type=0, key='13', value='13', checksum=-1494513008, serialized_key_size=2, serialized_value_size=2)
ConsumerRecord(topic=u'test', partition=1, offset=7, timestamp=1512556618293, timestamp_type=0, key='14', value='14', checksum=-1499251221, serialized_key_size=2, serialized_value_size=2)
ConsumerRecord(topic=u'test', partition=1, offset=8, timestamp=1512556620303, timestamp_type=0, key='16', value='16', checksum=-783427375, serialized_key_size=2, serialized_value_size=2)
ConsumerRecord(topic=u'test', partition=1, offset=9, timestamp=1512556623321, timestamp_type=0, key='19', value='19', checksum=-1902514040, serialized_key_size=2, serialized_value_size=2)
ConsumerRecord(topic=u'test', partition=1, offset=10, timestamp=1512556626337, timestamp_type=0, key='22', value='22', checksum=782849423, serialized_key_size=2, serialized_value_size=2)
...

```

可以看到两个consumer同时运行的情况下，它们分别消费不同partition中的数据。window1中的consumer消费partition 0中的数据，window2中的consumer消费parition 1中的数据。




我们尝试关闭window1中的consumer，可以看到如下结果

```bash
# window2

ConsumerRecord(topic=u'test', partition=1, offset=105, timestamp=1512557514410,                                                                                                     timestamp_type=0, key='46', value='46', checksum=-1821060627, serialized_key_siz                                                                                                    e=2, serialized_value_size=2)
ConsumerRecord(topic=u'test', partition=1, offset=106, timestamp=1512557518428,                                                                                                     timestamp_type=0, key='50', value='50', checksum=281004575, serialized_key_size=                                                                                                    2, serialized_value_size=2)
ConsumerRecord(topic=u'test', partition=1, offset=107, timestamp=1512557521442,                                                                                                     timestamp_type=0, key='53', value='53', checksum=1245067939, serialized_key_size                                                                                                    =2, serialized_value_size=2)
ConsumerRecord(topic=u'test', partition=1, offset=108, timestamp=1512557525461,                                                                                                     timestamp_type=0, key='57', value='57', checksum=-1003840299, serialized_key_siz                                                                                                    e=2, serialized_value_size=2)
ConsumerRecord(topic=u'test', partition=0, offset=98, timestamp=1512557494325, t                                                                                                    imestamp_type=0, key='26', value='26', checksum=-1576244323, serialized_key_size                                                                                                    =2, serialized_value_size=2)
ConsumerRecord(topic=u'test', partition=0, offset=99, timestamp=1512557495329, t                                                                                                    imestamp_type=0, key='27', value='27', checksum=510530536, serialized_key_size=2                                                                                                    , serialized_value_size=2)
ConsumerRecord(topic=u'test', partition=0, offset=100, timestamp=1512557502360,                                                                                                     timestamp_type=0, key='34', value='34', checksum=1781705793, serialized_key_size                                                                                                    =2, serialized_value_size=2)
ConsumerRecord(topic=u'test', partition=0, offset=101, timestamp=1512557504368,                                                                                                     timestamp_type=0, key='36', value='36', checksum=2142677730, serialized_key_size                                                                                                    =2, serialized_value_size=2)
ConsumerRecord(topic=u'test', partition=0, offset=102, timestamp=1512557505372,                                                                                                     timestamp_type=0, key='37', value='37', checksum=-1376259357, serialized_key_siz                                                                                                    e=2, serialized_value_size=2)
...

```

刚开始window2中的consumer只消费partition1中的数据，当window1中的consumer退出后，window2中的consumer中也开始消费partition 0中的数据了。




#### 实验三：offset管理

kafka允许consumer将当前消费的消息的offset提交到kafka中，这样如果consumer因异常退出后，下次启动仍然可以从上次记录的offset开始向后继续消费消息。

这个实验的结构和实验一的结构是一样的，使用一个producer，一个consumer，test topic的partition数量设为1。

producer的代码和实验一中的一样，这里不再重复。consumer的代码稍作修改，这里consumer中打印出下一个要被消费的消息的offset。consumer代码如下

```python
from kafka import KafkaConsumer, TopicPartition

tp = TopicPartition("test", 0)
consumer = KafkaConsumer(bootstrap_servers=["localhost:9092"], group_id="testgoup", auto_offset_reset="earliest", enable_auto_commit=False)
consumer.assign([tp])
print "starting offset is", consumer.position(tp)
for message in consumer:
    print message

```




在一个窗口中启动producer，在另一个窗口并且启动consumer。consumer的输出如下

```bash
$ python consumer.py
start offset is 98
ConsumerRecord(topic=u'test', partition=0, offset=98, timestamp=1512558902904, timestamp_type=0, key='98', value='98', checksum=-588818519, serialized_key_size=2, serialized_value_size=2)
ConsumerRecord(topic=u'test', partition=0, offset=99, timestamp=1512558903909, timestamp_type=0, key='99', value='99', checksum=1042712647, serialized_key_size=2, serialized_value_size=2)
ConsumerRecord(topic=u'test', partition=0, offset=100, timestamp=1512558904915, timestamp_type=0, key='100', value='100', checksum=-838622723, serialized_key_size=3, serialized_value_size=3)
ConsumerRecord(topic=u'test', partition=0, offset=101, timestamp=1512558905920, timestamp_type=0, key='101', value='101', checksum=-2020362485, serialized_key_size=3, serialized_value_size=3)
ConsumerRecord(topic=u'test', partition=0, offset=102, timestamp=1512558906926, timestamp_type=0, key='102', value='102', checksum=-345378749, serialized_key_size=3, serialized_value_size=3)
...

```

可以尝试退出consumer，再启动consumer。每一次重新启动，consumer都是从offset=98的消息开始消费的。




修改consumer的代码如下，在consumer消费每一条消息后将offset提交回kafka

```python
from kafka import KafkaConsumer, TopicPartition, OffsetAndMetadata

tp = TopicPartition("test2", 0)
consumer = KafkaConsumer(bootstrap_servers=["localhost:9092"], group_id="testgoup", auto_offset_reset="earliest", enable_auto_commit=False)
consumer.assign([tp])
print "start offset is ", consumer.position(tp)
for message in consumer:
    print message
    consumer.commit(message.offset + 1)

```




启动consumer

```text
$ python consumer.py
start offset is 98
ConsumerRecord(topic=u'test', partition=0, offset=98, timestamp=1512559632153, timestamp_type=0, key='824', value='824', checksum=828849435, serialized_key_size=3, serialized_value_size=3)
...
ConsumerRecord(topic=u'test', partition=0, offset=827, timestamp=1512559635164, timestamp_type=0, key='827', value='827', checksum=442222330, serialized_key_size=3, serialized_value_size=3)
ConsumerRecord(topic=u'test', partition=0, offset=828, timestamp=1512559636169, timestamp_type=0, key='828', value='828', checksum=-267344764, serialized_key_size=3, serialized_value_size=3)
ConsumerRecord(topic=u'test', partition=0, offset=829, timestamp=1512559637173, timestamp_type=0, key='829', value='829', checksum=1225853586, serialized_key_size=3, serialized_value_size=3)

```

可以看到consumer从offset=98的消息开始消费，到offset=829时，我们Ctrl+C退出consumer。




我们再次启动consumer

```text
$ python consumer.py
start offset is 830
ConsumerRecord(topic=u'test', partition=0, offset=830, timestamp=1512559638177, timestamp_type=0, key='830', value='830', checksum=1003305652, serialized_key_size=3, serialized_value_size=3)
ConsumerRecord(topic=u'test', partition=0, offset=831, timestamp=1512559639181, timestamp_type=0, key='831', value='831', checksum=-361607666, serialized_key_size=3, serialized_value_size=3)
ConsumerRecord(topic=u'test', partition=0, offset=832, timestamp=1512559640185, timestamp_type=0, key='832', value='832', checksum=-345891932, serialized_key_size=3, serialized_value_size=3)
...

```

可以看到重新启动后，consumer从上一次记录的offset开始继续消费消息。之后每一次consumer重新启动，consumer都会从上一次停止的地方继续开始消费。




#### 总结

本文主要介绍了一下kafka的基本概念，并结合一些实验帮助理解kafka中的一些难点，如多个consumer的容错性机制，offset管理。




#### 引用资料

kafka-python在线文档 - [kafka-python - kafka-python 1.3.6.dev documentation](http://link.zhihu.com/?target=http%3A//kafka-python.readthedocs.io/en/master/)

kafka官方文档 - [Apache Kafka](http://link.zhihu.com/?target=https%3A//kafka.apache.org/0100/documentation.html)

