Title: 理解python中的yield关键字
url: understand-yield-in-python.html
save_as: understand-yield-in-python.html
Date: 2018-05-26
Category: Python
Tags: Python
Authors: Zhongqiang Shen

想必大家都看到过这样的代码：

```python
def generate_square(n):
    i = 0
    while i < n:
        yield i * i
        i += 1

result = generate_square(10)
print(list(result))

```

上面的这段代码会计算0-9的平方并打印出来。

那么问题来了，这段代码和下面的这段代码有什么区别呢？

```python
def generate_square(n):
    i = 0
    result = []
    while i < n:
        result.append(i * i)
        i += 1
    return result

result = generate_square(10)
print(result)

```

这里的关键点是，前一段代码使用了yield关键字。那么yield是什么呢？要理解yield，还得从容器开始说起。

#### 容器（container）

像列表（list）、集合（set）、序列（tuple）、字典（dict）都是容器。简单的说，容器是一种把多个元素组织在一起的数据结构，可以逐个迭代获取其中的元素。容器可以用in来判断容器中是否包含某个元素，如

```python
'a' in {'a', 'b', 'c'} # 输出 True
'a' in {'a': 1, 'b': 2} # 输出 True
'a' in set(['a', 'b', 'c']) # 输出 True

```

大多数的容器都是可迭代对象，可以使用某种方式访问容器中的每一个元素。




#### 迭代器（iterator）

实现了\_\_iter\_\_和\_\_next\_\_方法的对象都称为迭代器。迭代器是一个有状态的对象，在调用next() 的时候返回下一个值，如果容器中没有更多元素了，则抛出StopIteration异常。

看下面的例子

```python
a = ['a', 'b', 'c']
it = a.__iter__()
print(next(it))
print(next(it))
print(next(it))
print(next(it))

```

输出

```text
a
b
c
Traceback (most recent call last):
  File "/tmp/a.py", line 19, in <module>
    print(next(it))
StopIteration

```

为更好地理解迭代器的内部运行机制，我们再来看一个斐波那契数列的例子

```python
class Fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.curr, self.prev = self.prev + self.curr, self.curr
        return self.curr

fib = Fib()
for i in range(10):
    print(next(fib))

```

输出

```text
1
1
2
3
5
8
13
21
34
55

```

只要不断地调用next() 方法，上面的生成器可以生成一个无限长的斐波那契数列。

迭代器是一种Lasy Load的模式，只有在调用时才生成值，没有调用的时候就等待下一次调用。




#### 生成器和yield

生成器其实是一种特殊的迭代器，但是不需要像迭代器一样实现\_\_iter\_\_和\_\_next\_\_方法，只需要使用关键字yield就可以。

我们来实现一个同样的斐波那契数列，但这次使用的是生成器

```python
def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        curr, prev = prev + curr, curr

f = fib()
for i in range(10):
    print(next(f))

```

输出

```text
1
1
2
3
5
8
13
21
34
55

```

上面的 fib 函数中没有 return 关键字。当运行 f = fib() 的时候，它返回的是一个生成器对象。在调用 fib() 的时候并不会运行 fib 函数中的代码，只有在调用 next() 的时候才会真正运行其中的代码。




回到文章最开始的问题，两种方式实现的generate\_square函数，一个使用了yield关键字，一个使用了列表保存所有的值并返回列表，两者的区别在什么地方？

对于前一种实现方式，使用了生成器，在调用函数的时候不会一次性生成所有的元素，而是在每次调用 next() 才生成一个元素；而后一种方式，在调用函数的时候就生成了所有元素，相比之下，更耗费内存和CPU。




看到这里，大家是不是理解了yield关键字呢？

那么给大家出一个思考题：下面的代码为什么第二次调用next打印None呢？

```python
def echo(n):
    while True:
        n = yield n

g = echo(1)
print(next(g))
print(next(g))

```

答案下期揭晓~




本文已更新微信同名公众号【Python与数据分析】，欢迎关注~

![]({static}/images/v2-e9b0b9b9584ccdd3ff4c96b7ecfd8a56_r.jpg)









