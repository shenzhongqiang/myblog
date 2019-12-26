Title: Python面试之交换变量值
url: swap-value.html
save_as: swap-value.html
Date: 2018-04-02
Category: Python
Tags: Python
Authors: Zhongqiang Shen

平时时不时会面面实习生，大多数的同学在学校里都已经掌握了Python。面试的时候要求同学们实现一个简单的函数，交换两个变量的值，大多数的同学给出的都是如下的答案

```python
def swap(x, y):
    tmp = x
    x = y
    y = tmp

```

实际上，Python中还有更简洁的更具Python风格的实现，如下

```python
def swap(x, y):
    x, y = y, x

```

相比前一种方法，后一种方法节省一个中间变量，在性能上也优于前一种方法。




我们从Python的字节码来深入分析一下原因。

```python
import dis 
import timeit

def swap1():
    x = 5 
    y = 6 
    x, y = y, x

def swap2():
    x = 5 
    y = 6 
    tmp = x 
    x = y 
    y = tmp 

if __name__ == "__main__":
    print "================= swap1 ================="
    print dis.dis(swap1)
    print "================= swap2 ================="
    print dis.dis(swap2)

```

dis是个反汇编工具，将Python代码翻译成字节码指令。这里的输出如下

```text
================= swap1 =================
  5           0 LOAD_CONST               1 (5)
              3 STORE_FAST               0 (x)

  6           6 LOAD_CONST               2 (6)
              9 STORE_FAST               1 (y)

  7          12 LOAD_FAST                1 (y)
             15 LOAD_FAST                0 (x)
             18 ROT_TWO             
             19 STORE_FAST               0 (x)
             22 STORE_FAST               1 (y)
             25 LOAD_CONST               0 (None)
             28 RETURN_VALUE        
None
================= swap2 =================
 10           0 LOAD_CONST               1 (5)
              3 STORE_FAST               0 (x)

 11           6 LOAD_CONST               2 (6)
              9 STORE_FAST               1 (y)

 12          12 LOAD_FAST                0 (x)
             15 STORE_FAST               2 (tmp)

 13          18 LOAD_FAST                1 (y)
             21 STORE_FAST               0 (x)

 14          24 LOAD_FAST                2 (tmp)
             27 STORE_FAST               1 (y)
             30 LOAD_CONST               0 (None)
             33 RETURN_VALUE        
None

```

通过字节码可以看到，swap1和swap2最大的区别在于，swap1中通过ROT\_TWO交换栈顶的两个元素实现x和y值的互换，swap2中引入了tmp变量，多了一次LOAD\_FAST, STORE\_FAST的操作。执行一个ROT\_TWO指令比执行一个LOAD\_FAST+STORE\_FAST的指令快，这也是为什么swap1比swap2性能更好的原因。

