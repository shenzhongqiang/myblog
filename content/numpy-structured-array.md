Title: Numpy的结构化数组
url: numpy-structured-array.html
save_as: numpy-structured-array.html
Date: 2018-03-22
Category: Numpy
Tags: Python, Numpy
Authors: Zhongqiang Shen

numpy可以创建包含同类型数据的数组，底层用C实现，效率非常高。我们可以用如下的方式创建一个numpy数组：

```python
import numpy as np
a = np.array([1, 2, 3, 4, 5])

```

上面创建了一个int64的数组a，每个元素都是相同的int64类型。




除了创建简单类型的数组，numpy也支持创建更复杂的结构化数组，底层其实就是C中的结构体，每个元素可以包含不同类型的数据。

举个例子，比如我们要存取一组人事信息，包括每个人的名字、年龄、级别，可以用numpy创建如下的结构化数组

```python
data = np.zeros(4, dtype={
    'names':('name', 'age', 'grade'),
    'formats':('U10', 'i4', 'i4')
})
data['name'] = ['Xiao Lin', 'Xiao Pan', 'Xiao Shen', 'Xiao Zhou']
data['age'] = [28, 33, 34, 29]
data['grade'] = [25, 26, 27, 24]

data
# output
# [(u'Xiao Lin', 28, 25) (u'Xiao Pan', 33, 26) (u'Xiao Shen', 34, 27)
# (u'Xiao Zhou', 29, 24)]

```

dtype指定了key的名称和类型，这里U10表示最大长度为10的unicode字符串，i4表示4字节的整数。

有了上面的定义，我们可以很方便的通过下标来获得对应位置的数据

```python
data[0]
# output
# (u'Xiao Lin', 28, 25)

```

也可以获得指定key的所有值

```python
data["name"]
# output
# array([u'Xiao Lin', u'Xiao Pan', u'Xiao Shen', u'Xiao Zhou'], dtype='<U10')

```

还可以根据key做过滤

```python
data[data["grade"]>26]["name"]
# output
# array([u'Xiao Shen'], dtype='<U10')

```




除了结构化数组，numpy还支持一种record数组，和结构化数组唯一的区别就是，record数组不需要通过字典的key的方式来获取数据，直接通过属性就可以。举个例子就很清楚了

```python
data_rec = data.view(np.recarray)

data_rec
# output
# rec.array([(u'Xiao Lin', 28, 25), (u'Xiao Pan', 33, 26),
#           (u'Xiao Shen', 34, 27), (u'Xiao Zhou', 29, 24)],
#           dtype=[('name', '<U10'), ('age', '<i4'), ('grade', '<i4')])

data_rec.name
# array([u'Xiao Lin', u'Xiao Pan', u'Xiao Shen', u'Xiao Zhou'], dtype='<U10')

data_rec["name"]
# array([u'Xiao Lin', u'Xiao Pan', u'Xiao Shen', u'Xiao Zhou'], dtype='<U10')

```




看到这里，大家可能会有疑问，numpy的结构化数组中的每个元素似乎就是Python的字典，我们为什么还要用numpy呢？

事实是这样的，numpy的结构化数组底层就是C的结构体，占用一块连续的内存区域，并且numpy底层是C实现，numpy数组中的类型都是静态类型的，性能比Python的的字典列表不知道高到哪儿去了。

我们来做一下性能比较。对上面的程序，我们来实现一个用Python字典的版本。快过年了，我们给每个人都长一岁

```python
# -*- coding: utf-8 -*-
import numpy as np

# numpy版本长一岁
def addage_numpy(data):
    data['age'] += 1

# python循环长一岁
def addage_python(data):
    for i in range(4):
        data[i]["age"] += 1

names = ['Xiao Lin', 'Xiao Pan', 'Xiao Shen', 'Xiao Zhou']
ages = [28, 33, 34, 29] 
grades = [25, 26, 27, 24] 
data_np = np.zeros(4, dtype={
    'names':('name', 'age', 'grade'),
    'formats':('U10', 'i4', 'i4')
})
data_np['name'] = names
data_np['age'] = ages
data_np['grade'] = grades

data_py = []
for i in range(4):
    person = {"name": names[i], "age": ages[i], "grade": grades[i]}
    data_py.append(person)

```




在ipython中加载上面的代码，并比较两个函数的性能

```python
In [1]: %load test.py
In [2]: %timeit addage_numpy(data_np)
1000000 loops, best of 3: 1.76 µs per loop

In [3]: %timeit addage_python(data_py)
1000000 loops, best of 3: 451 ns per loop

```

可以看到，两者性能差了250多倍。



