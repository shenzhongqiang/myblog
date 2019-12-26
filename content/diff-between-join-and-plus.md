Title: Python面试之连接字符串用join还是+
url: diff-between-join-and-plus.html
save_as: diff-between-join-and-plus.html
Date: 2018-06-23
Category: Python
Tags: Python
Authors: Zhongqiang Shen

上一篇[Python面试之可变对象和不可变对象](https://zhuanlan.zhihu.com/p/35389687)的最后留了一个问题

```python
class Group(object):
    def __init__(self, group_id, members=[]):
        self.group_id = group_id
        self.members = members

    def add_member(self, member):
        self.members.append(member)

```

上述代码中默认参数值对象会被缓存，造成Group类型的对象共享同一个members列表，怎样才能解决这个问题呢？

其实很简单，只要传入None作为默认参数，在创建对象的时候动态生成列表，如下

```python
class Group(object):
    def __init__(self, group_id, members=None):
        self.group_id = group_id
        if members is None:
            self.members = []

    def add_member(self, member):
        self.members.append(member)

```

这样对于不同的group对象，它们的members也是不同的对象，所以不会再出现更新一个group对象的members也会更新另外一个group对象的members了。




本篇要讲的是，连接字符串的时候可以用join也可以用+，但这两者有没有区别呢？

我们先来看一下用join和+连接字符串的例子

```python
str1 = " ".join(["hello", "world"])
str2 = "hello " + "world"

print(str1)  # 输出 “hello world"
print(str2)  # 输出 “hello world"

```

两者的结果是一样，那么考虑这样一个问题，这两者在性能上有区别吗？




我们来做个实验，比较下join和+的性能

```python
import timeit
def test1(strlist):
    return "".join(strlist)

def test2(strlist):
    result = ""
    for v in strlist:
        result = result+v
    return result

if __name__ == "__main__":
    strlist = ["a very very very very very very very long string" for n in range(100000)]
    timer1 = timeit.Timer("test1(strlist)", "from __main__ import strlist, test1")
    timer2 = timeit.Timer("test2(strlist)", "from __main__ import strlist, test2")
    time1 = timer1.timeit(number=100)
    time2 = timer2.timeit(number=100)
    print("join: %f, plus: %f" % (time1, time2))

```

上面的程序有如下的输出

```text
join: 0.116944, plus: 0.394379

```

可以看到，join的性能明显好于+。这是为什么呢？

原因是这样的，上一篇[Python面试之可变对象和不可变对象](https://zhuanlan.zhihu.com/p/35389687)中讲过字符串是不可变对象，当用操作符+连接字符串的时候，每执行一次+都会申请一块新的内存，然后复制上一个+操作的结果和本次操作的右操作符到这块内存空间，因此用+连接字符串的时候会涉及好几次内存申请和复制。而join在连接字符串的时候，会先计算需要多大的内存存放结果，然后一次性申请所需内存并将字符串复制过去，这是为什么join的性能优于+的原因。所以在连接字符串数组的时候，我们应考虑优先使用join。




本文已更新微信同名公众号【Python与数据分析】，欢迎关注~

![]({static}/images/v2-e9b0b9b9584ccdd3ff4c96b7ecfd8a56_r.jpg)



