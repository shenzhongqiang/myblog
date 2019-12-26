Title: Python 2与Python 3的区别
url: diff-between-python2-and-python3.html
save_as: diff-between-python2-and-python3.html
Date: 2018-06-23
Category: Python
Tags: Python
Authors: Zhongqiang Shen

越来越多的库要放弃Python 2了，强哥也开始转向Python 3了。最近的项目开始用Python3写了，也体会了一下2和3的区别。主要的一些区别在以下几个方面：

+ print函数
+ 整数相除
+ Unicode
+ 异常处理
+ xrange
+ map函数
+ 不支持has_key





#### print函数

Python 2中print是语句（statement），Python 3中print则变成了函数。在Python 3中调用print需要加上括号，不加括号会报SyntaxError

Python 2

```python
print "hello world"

```

输出

```text
hello world

```




Python 3

```python
print("hello world")

```

输出

```text
hello world

```




```python
print "hello world"

```

输出

```text
 File "<stdin>", line 1
    print "hello world"
                      ^
SyntaxError: Missing parentheses in call to 'print'

```




#### 整数相除

在Python 2中，3/2的结果是整数，在Python 3中，结果则是浮点数

Python 2

```python
print '3 / 2 =', 3 / 2
print '3 / 2.0 =', 3 / 2.0

```

输出

```text
3 / 2 = 1
3 / 2.0 = 1.5

```




Python 3

```python
print('3 / 2 =', 3 / 2)
print('3 / 2.0 =', 3 / 2.0)

```

输出

```text
3 / 2 = 1.5
3 / 2.0 = 1.5

```




#### Unicode

Python 2有两种字符串类型：str和unicode，Python 3中的字符串默认就是Unicode，Python 3中的str相当于Python 2中的unicode。

在Python 2中，如果代码中包含非英文字符，需要在代码文件的最开始声明编码，如下

```python
# -*- coding: utf-8 -*-

```

在Python 3中，默认的字符串就是Unicode，就省去了这个麻烦，下面的代码在Python 3可以正常地运行

```python
a = "你好"
print(a)

```




#### 异常处理

Python 2中捕获异常一般用下面的语法

```python
try:
    1/0 
except ZeroDivisionError, e:
    print str(e)

```

或者

```python
try:
    1/0 
except ZeroDivisionError as e:
    print str(e)

```

Python 3中不再支持前一种语法，必须使用as关键字。




#### xrange

Python 2中有 range 和 xrange 两个方法。其区别在于，range返回一个list，在被调用的时候即返回整个序列；xrange返回一个iterator，在每次循环中生成序列的下一个数字。Python 3中不再支持 xrange 方法，Python 3中的 range 方法就相当于 Python 2中的 xrange 方法。




#### map函数

在Python 2中，map函数返回list，而在Python 3中，map函数返回iterator。

Python 2

```python
map(lambda x: x+1, range(5))

```

输出

```text
[1, 2, 3, 4, 5]

```




Python 3

```python
map(lambda x: x+1, range(5))

```

输出

```text
<map object at 0x7ff5b103d2b0>

```




```python
list(map(lambda x: x+1, range(5)))

```

输出

```text
[1, 2, 3, 4, 5]

```

filter函数在Python 2和Python 3中也是同样的区别。




#### 不支持has\_key

Python 3中的字典不再支持has\_key方法

Python 2

```python
person = {"age": 30, "name": "Xiao Wang"}
print "person has key \"age\": ", person.has_key("age")
print "person has key \"age\": ", "age" in person

```

输出

```text
person has key "age":  True
person has key "age":  True

```




Python 3

```python
person = {"age": 30, "name": "Xiao Wang"}
print("person has key \"age\": ", "age" in person)

```

输出

```text
person has key "age":  True

```




```python
print("person has key \"age\": ", person.has_key("age"))

```

输出

```text
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'has_key'

```




以上是最近整理的一些，后续会继续更新，也欢迎大家补充。




本文已更新微信同名公众号【Python与数据分析】，欢迎关注~

![]({static}/images/v2-e9b0b9b9584ccdd3ff4c96b7ecfd8a56_r.jpg)



