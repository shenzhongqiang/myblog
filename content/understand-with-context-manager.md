Title: Python面试之with与上下文管理器
url: understand-with-context-manager.html
save_as: understand-with-context-manager.html
Date: 2018-05-09
Category: Python
Tags: Python
Authors: Zhongqiang Shen

#### With基本语法

Python老司机应该对下面的语法不陌生

```python
with open('output', 'w') as f:
    f.write('Hello world')

```

上面的代码往output文件写入了Hello world字符串，with语句会在执行完代码块后自动关闭文件。这里无论写文件的操作成功与否，是否有异常抛出，with语句都会保证文件被关闭。

如果不用with，我们可能要用下面的代码实现类似的功能

```python
try:
    f = open("output", "w")
    f.write("Hello world")
finally:
    f.close()

```

可以看到使用了with的代码比上面的代码简洁许多。




上面的with代码背后发生了些什么？我们来看下它的执行流程

1. + 首先执行open('output', 'w')，返回一个文件对象
2. + 调用这个文件对象的__enter__方法，并将__enter__方法的返回值赋值给变量f
3. + 执行with语句体，即with语句包裹起来的代码块
4. + 不管执行过程中是否发生了异常，执行文件对象的__exit__方法，在__exit__方法中关闭文件。


这里的关键在于open返回的文件对象实现了\_\_enter\_\_和\_\_exit\_\_方法。一个实现了\_\_enter\_\_和\_\_exit\_\_方法的对象就称之为**上下文管理器**。




#### 上下文管理器

上下文管理器定义执行 with 语句时要建立的运行时上下文，负责执行 with 语句块上下文中的进入与退出操作。\_\_enter\_\_方法在语句体执行之前进入运行时上下文，\_\_exit\_\_在语句体执行完后从运行时上下文退出。

在实际应用中，\_\_enter\_\_一般用于资源分配，如打开文件、连接数据库、获取线程锁；\_\_exit\_\_一般用于资源释放，如关闭文件、关闭数据库连接、释放线程锁。




#### 自定义上下文管理器

既然上下文管理器就是实现了\_\_enter\_\_和\_\_exit\_\_方法的对象，我们能不能定义自己的上下文管理器呢？答案是肯定的。

我们先来看下\_\_enter\_\_和\_\_exit\_\_方法的定义：

**\_\_enter\_\_() **- 进入上下文管理器的运行时上下文，在语句体执行前调用。如果有as子句，with语句将该方法的返回值赋值给 as 子句中的 target。

**\_\_exit\_\_(exception\_type, exception\_value, traceback) **- 退出与上下文管理器相关的运行时上下文，返回一个布尔值表示是否对发生的异常进行处理。如果with语句体中没有异常发生，则\_\_exit\_\_的3个参数都为None，即调用 \_\_exit\_\_(None, None, None)，并且\_\_exit\_\_的返回值直接被忽略。如果有发生异常，则使用 sys.exc\_info 得到的异常信息为参数调用\_\_exit\_\_(exception\_type, exception\_value, traceback)。出现异常时，如果\_\_exit\_\_(exception\_type, exception\_value, traceback)返回 False，则会重新抛出异常，让with之外的语句逻辑来处理异常；如果返回 True，则忽略异常，不再对异常进行处理。




理解了\_\_enter\_\_和\_\_exit\_\_方法后，我们来自己定义一个简单的上下文管理器。这里不做实际的资源分配和释放，而用打印语句来表明当前的操作。

```python
class ContextManager(object):
    def __enter__(self):
        print("[in __enter__] acquiring resources")

    def __exit__(self, exception_type, exception_value, traceback):
        print("[in __exit__] releasing resources")
        if exception_type is None:
            print("[in __exit__] Exited without exception")
        else:
            print("[in __exit__] Exited with exception: %s" % exception_value)
            return False

with ContextManager():
    print("[in with-body] Testing")

```

运行上面的代码，会得到如下的输出

```text
[in __enter__] acquiring resources
[in with-body] Testing
[in __exit__] releasing resources
[in __exit__] Exited without exception

```




我们在with语句体中人为地抛出一个异常

```python
with ContextManager():
    print("[in with-body] Testing")
    raise(Exception("something wrong"))

```

会得到如下的输出

```text
[in __enter__] acquiring resources
[in with-body] Testing
[in __exit__] releasing resources
[in __exit__] Exited with exception: something wrong
Traceback (most recent call last):
  File "/tmp/a.py", line 15, in <module>
    raise(Exception("something wrong"))
Exception: something wrong

```

如我们所期待，with语句体中抛出异常，\_\_exit\_\_方法中exception\_type不为None，\_\_exit\_\_方法返回False，异常被重新抛出。

以上，我们通过实现\_\_enter\_\_和\_\_exit\_\_方法来实现了一个自定义的上下文管理器。




#### contextlib库

除了上面的方法，我们也可以使用contextlib库来自定义上下文管理器。如果用contextlib来实现，可以用下面的代码来实现类似的上下文管理器

```python
from contextlib import contextmanager

@contextmanager
def func():
    try:
        print("[in __enter__] acquiring resources")
        yield
    finally:
        print("[in __exit__] releasing resources")

with func():
    print("[in with-body] Testing")
    raise(Exception("something wrong"))

```

上面的代码涉及到装饰器（@contextmanager），生成器（yield），有点难读。这里yield之前的代码相当于\_\_enter\_\_方法，在进入with语句体之前执行，yield之后的代码相当于\_\_exit\_\_方法，在退出with语句体的时候执行。

接下来的几篇文章，我们来逐一介绍一下，什么是装饰器，什么是生成器，@contextmanager是如何实现上下文管理器的。敬请期待~




本文已更新微信同名公众号，欢迎扫一扫关注~

![]({static}/images/v2-e9b0b9b9584ccdd3ff4c96b7ecfd8a56_r.jpg)



