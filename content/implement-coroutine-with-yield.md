Title: 用yield实现协程
url: implement-coroutine-with-yield.html
save_as: implement-coroutine-with-yield.html
Date: 2018-05-28
Category: Python
Tags: Python
Authors: Zhongqiang Shen

上一篇 [理解python中的yield关键字](https://zhuanlan.zhihu.com/p/37257918) 介绍了使用yeld实现生成器函数，这一篇我们来继续深入的了解一下yield，用yield实现协程。

先来解答一下上一篇留下的问题：下面的代码为什么第二次调用next打印None呢？

```python
def echo(n):
    while True:
        n = yield n

g = echo(1)
print(next(g))
print(next(g))

```

事实是这样的，yield语句默认返回None。当第一次调用next方法时，生成器函数开始执行，执行到yield表达式为止，但此时赋值操作并为执行。上面的代码中，在第一次调用next的时候，echo生成了1。第二次调用next的时候，yield表达式的值赋给了n，n此时变成None了，再次yield n的时候就自然生成None了。

好了，接下来开始本文的主题。




#### 什么是协程

引用官方的说法：

> 协程是一种用户态的轻量级线程，协程的调度完全由用户控制。协程拥有自己的寄存器上下文和栈。协程调度切换时，将寄存器上下文和栈保存到其他地方，在切回来的时候，恢复先前保存的寄存器上下文和栈，直接操作栈则基本没有内核切换的开销，可以不加锁的访问全局变量，所以上下文的切换非常快。

与线程相比，协程更轻量。一个Python线程大概占用8M内存，而一个协程只占用1KB不到内存。协程更适用于IO密集型的应用。

在讲述协程的实现前，我们有必要先来看一下send方法。




#### send方法

yield表达式有一个返回值，send方法的作用就是控制这个返回值，send的参数就是yield表达式的返回值。我们来看一下官方文档上关于send的定义

> generate.send(*value*)：

生成器的send(value)方法会将value值“发送”给生成器中的方法。value参数变成当前yield表达式的值。send()方法会返回生成器生成的下一个yield值或者StopIteration异常（如果生成器没有生成下一个yield值就退出了）。当通过调用send()启动生成器时，value值必须为None，因为当前还没有yield表达式可以接收参数。




是不是看晕了？我们来看一个例子

```python
def func():
    while True:
        print("before yield")
        x = yield
        print("after yield:",x)

g = func()
next(g) # 程序运行到yield并停在该处,等待下一个next
g.send(1) # 给yield发送值1,这个值被赋值给了x，并且打印出来,然后继续下一次循环停在yield处
g.send(2) # 给yield发送值2,这个值被赋值给了x，并且打印出来,然后继续下一次循环停在yield处
next(g) # 没有给x赋值，执行print语句，打印出None,继续循环停在yield处

```

上面的代码输出

```text
before yield
after yield: 1
before yield
after yield: 2
before yield
after yield: None
before yield

```

第一次调用next的时候，程序从函数最开始处运行，打印出

before yield

执行到yield处，停在该处。

接下来，向生成器send(1)。send在这里起到两个作用，一个是将参数值赋给yield的返回值，然后该返回值赋给了变量x；一个是继续程序的执行，直到下一次遇到yield停下来。第二个功能和next类似。其实，next 就相当于 send(None) 。

执行了 send(1) 后，x被赋值给yield的返回值，即send的参数1，并继续往下执行，打印出了

after yield: 1

继续执行，回到循环的开始，向下执行，打印出

before yield

再次遇到yield，停在该处，等待下一次send或next的调用。

向生成器send(2)。这里的步骤和 send(1) 相同，打印出下面两条后，在yield处停住。

after yield: 2

before yield

执行 next(g)，x被赋值为yield表达式的返回值，也就是None，继续向下执行，打印出

after yield: None

再次回到循环的开始，向下执行，打印出

before yield

程序运行结束。




现在是不是有点理解send了？




#### yield和send实现Python协程

我们来用协程实现一个生产者/消费者的例子

```python
import time

def consume():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[consumer] consuming %s...' % n)
        time.sleep(1)
        r = 'well received'

def produce(c):
    next(c)
    n = 0
    while n < 5:
        n = n + 1
        print('[producer] producing %s...' % n)
        r = c.send(n)
        print('[producer] consumer return: %s' % r)
    c.close()

if __name__=='__main__':
    c = consume()
    produce(c)

```

运行上面的程序，会输出

```text
[producer] producing 1...
[consumer] consuming 1...
[producer] consumer return: well received
[producer] producing 2...
[consumer] consuming 2...
[producer] consumer return: well received
[producer] producing 3...
[consumer] consuming 3...
[producer] consumer return: well received
[producer] producing 4...
[consumer] consuming 4...
[producer] consumer return: well received
[producer] producing 5...
[consumer] consuming 5...
[producer] consumer return: well received

```

produce函数负责生产数据，consume函数负责消费数据。具体执行过程如下：

1. + 首先调用consume函数，consume函数的返回是一个生成器，把这个生成器传入produce函数。
2. + produce函数中调用next(c)启动生成器。
3. + 计算 n = n+1 生成数据，一旦生产了数据，调用 c.send(n) 切换到consume执行。
4. + consume函数中拿到数据后赋值给n，继续执行yield后面的语句。
5. + consume函数中打印消费的数据，并设置返回值r，又回到循环的开始，通过yield把结果传回。
6. + produce拿到consume返回的值，继续生产下一个数据。
7. + 5个数据生产完毕后，循环结束，通过c.close()关闭consume，结束全过程。


produce和consume函数在一个线程内执行，通过调用send方法和yield互相切换，实现协程的功能。




本文已更新微信同名公众号【Python与数据分析】，欢迎关注~

![]({static}/images/v2-e9b0b9b9584ccdd3ff4c96b7ecfd8a56_r.jpg)







