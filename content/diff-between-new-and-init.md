Title: Python面试之理解__new__和__init__的区别
url: diff-between-new-and-init
save_as: diff-between-new-and-init.html
Date: 2018-06-23
Category: Python
Tags: Python
Authors: Zhongqiang Shen

很多同学都以为Python中的\_\_init\_\_是构造方法，但其实不然，Python中真正的构造方法是\_\_new\_\_。\_\_init\_\_和\_\_new\_\_有什么区别？本文就来探讨一下。




我们先来看一下\_\_init\_\_的用法

```python
class Person(object):
    def __init__(self, name, age):
        print("in __init__")
        self._name = name
        self._age = age 

p = Person("Wang", 33) 

```

上面的代码会输出如下的结果

```text
in __init__
<__main__.Person object at 0x7fb2e0936450>

```

那么我们思考一个问题，Python中要实现Singleton怎么实现，要实现工厂模式怎么实现？

用\_\_init\_\_函数似乎没法做到呢~

实际上，\_\_init\_\_函数并不是真正意义上的构造函数，\_\_init\_\_方法做的事情是在对象创建好之后初始化变量。真正创建实例的是\_\_new\_\_方法。

我们来看下面的例子

```python
class Person(object):
    def __new__(cls, *args, **kwargs):
        print("in __new__")
        instance = object.__new__(cls, *args, **kwargs)
        return instance

    def __init__(self, name, age):
        print("in __init__")
        self._name = name
        self._age = age

p = Person("Wang", 33)

```

上面的代码输出如下的结果

```text
in __new__
in __init__

```

上面的代码中实例化了一个Person对象，可以看到\_\_new\_\_和\_\_init\_\_都被调用了。\_\_new\_\_方法用于创建对象并返回对象，当返回对象时会自动调用\_\_init\_\_方法进行初始化。\_\_new\_\_方法是静态方法，而\_\_init\_\_是实例方法。

好了，理解\_\_new\_\_和\_\_init\_\_的区别后，我们再来看一下前面提出的问题，用Python怎么实现Singleton，怎么实现工厂模式？

先来看Singleton

```python
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2) 

```

上面的代码输出

```text
<__main__.Singleton object at 0x7fdef58b1190>
<__main__.Singleton object at 0x7fdef58b1190>

```

可以看到s1和s2都指向同一个对象，实现了单例模式。




再来看下工厂模式的实现

```python
class Fruit(object):
    def __init__(self):
        pass

    def print_color(self):
        pass

class Apple(Fruit):
    def __init__(self):
        pass

    def print_color(self):
        print("apple is in red")

class Orange(Fruit):
    def __init__(self):
        pass

    def print_color(self):
        print("orange is in orange")

class FruitFactory(object):
    fruits = {"apple": Apple, "orange": Orange}

    def __new__(cls, name):
        if name in cls.fruits.keys():
            return cls.fruits[name]()
        else:
            return Fruit()

fruit1 = FruitFactory("apple")
fruit2 = FruitFactory("orange")
fruit1.print_color()    
fruit2.print_color()    

```

上面的代码输出

```python
apple is in red
orange is in orange

```




看完上面两个例子，大家是不是对\_\_new\_\_和\_\_init\_\_的区别有了更深入的理解？




本文已更新微信同名公众号【Python与数据分析】，欢迎关注~

![]({static}/images/v2-e9b0b9b9584ccdd3ff4c96b7ecfd8a56_r.jpg)



