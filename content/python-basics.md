Title: 写给小白看的Python基础知识（上）
url: python-basics.html
save_as: python-basics.html
Date: 2022-03-19
Category:
Authors: Zhongqiang Shen



18000字的长文，建议先收藏后阅读，如果能够点赞转发那就太感谢啦~话不多说，我们正式开始。#### 安装 Python在开始学习 python 之前，我们先要安装 python。安装 python 的步骤根据不同的操作系统会有些差异，以下是几种常见的操作系统下的安装方法Ubuntu命令行下运行 ```bash
apt-get install python3
```Mac命令行下运行```bash
brew install python
```Windows在 python 官网 [https://www.](https://link.zhihu.com/?target=https%3A//www.python.org/downloads/windows/) 上，选择最新的 Python 安装包，下载安装即可。安装完 Python，我们在命令行输入 python3，就可以启动 python 解释器，像下面这样```text
$ python3
Python 3.9.6 (v3.9.6:db3ff76da1, Jun 28 2021, 11:49:53)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```接下来我们就可以开始我们的Python编程之旅了。
#### 初识Python### 酷酷的 Python在开始学习编程之前，我们先来看一个有趣的例子，我们在我们的 Python 解释器中，贴入下面这一行代码```python
print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.04)**2+(y*0.1)**2-1)**3-(x*0.04)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
```然后点击运行，看看会有什么结果？
结果是长这样的```text
                                                            
            veLoveLoveL               LoveLoveLov           
        eLoveLoveLoveLoveLov     LoveLoveLoveLoveLove       
     oveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLove    
    oveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLo   
   oveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLove  
  oveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLo 
  veLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLov 
  eLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLove 
  LoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveL 
   veLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveL  
   eLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLo  
    oveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLo   
     eLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLo    
       veLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveL      
        LoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveL       
          eLoveLoveLoveLoveLoveLoveLoveLoveLoveLove         
            veLoveLoveLoveLoveLoveLoveLoveLoveLov           
               veLoveLoveLoveLoveLoveLoveLoveL              
                  veLoveLoveLoveLoveLoveLov                 
                     veLoveLoveLoveLoveL                    
                         eLoveLoveLo                        
                            eLove                           
                              v                             
                                                    
```有没有惊讶到？对，Python 就是这么酷，一行代码就可以画个爱心❤️。这个例子的代码看不懂没关系，在学习了相关的基础知识后，我们会详细的讲解这个例子。### 打印字符串我们从一段最简单的代码来开始学习 Python```python
print("Hello world")
```这段代码会打印出 "Hello world" 这样一句话。代码里的 print 是一个函数，"Hello world" 是一个字符串。关于函数和字符串，我们会在后面的内容里详细讲解。### 注释在Python中，注释用井号（# ）标识，像下面这样```python
# 这是一段注释
```注释不会被 Python 解释器执行，井号后面的内容都会被Python解释器忽略。注释一般用来对代码做注解，主要是为了让程序更易于理解。### **数和表达式**表达式是运算符和操作数构成的序列，我们看几个例子就很清楚```python
1 + 1 # 加法运算，结果是 2
3 / 2 # 除法运算，结果是 1.5
3 // 2 # 整除运算，结果是 1
3 % 2 # 求余数，结果是 1
2 ** 3 # 指数运算，结果是 8
```### 变量变量很好理解，就是给一个值起一个名字，比如 a = 3，a 就是变量名，3就是它的值。b = "hello"，b 是变量名，"hello" 是它的值。这个将变量设成某一个值的过程叫做**赋值**。一旦变量被赋值，我们就可以在表达式中使用它，像下面这样```python
a = 3 # 将变量 a 设成 3
a * 5 # 将变量 a 乘以 5
b = "hello" # 将变量 b 设成字符串 hello
print(b) # 打印变量 b 的值
```### 语句语句可以理解成做一件事。我们前面提到的 a = 3 是一个赋值语句，print("hello") 是一个函数调用语句。Python 中还有很多其它的语句，我们在后面的内容里会详细的讲解。### 函数函数就是一个实现特定功能的程序，比如我们前面提到的 print 是一个函数，它实现的是打印的功能。python 中还有许多其它的函数，比如```python
pow(2, 3) # 计算2的3次方，结果是 8
abs(-10) # 计算-10的绝对值，结果是 10
round(1.8) # 计算1.8四舍五入后的值，结果是 2
```函数怎么使用，怎么定义函数，我们在后面的内容会展开详细讲解。### 模块模块是一组功能的组合，模块中可以有函数、变量等等。在 python 中我们会经常用到模块。比如我们要用到一些数学函数，这时可以使用  math 这个模块。首先我们用关键字 import 来指定要使用它，像下面这样```python
import math
```接下来我们使用 math 模块中的函数，用下面的方式```python
math.floor(2.1) # 使用 math 模块中的 floor 函数对2.1作向下取整，结果是 2
math.ceil(2.1) # 使用 math 模块中的 ceil 函数对2.1作向上取整，结果是 3
math.sqrt(2) # 使用 math 模块中的 sqrt 函数对2求平方根，结果是 1.4142135623730951
```使用 math 模块中定义的变量，可以用下面的方式```python
math.pi # 输出 3.141592653589793
```模块就像是一个工具箱，使用模块就好像打开了一个工具箱，我们选择我们需要的工具，来做我们想做的事。好，以上就是这一节的全部内容。这一节我们主要是对 Python 的一些基本概念做了个粗浅的介绍，让大家对 Python 有个初步的认识。在接下来的内容里，我们将逐步深入地学习。下一节，我们来看一下 Python 中的几种基本数据类型。#### Python 基本数据类型Python中的数据类型主要有这样几种+ 数字
+ 字符串
+ 列表
+ 元组
+ 字典
下面我们来逐个讲解。### 数字Python里有两种数字类型：整数和浮点数。数字和数字之间可以做各种数值运算，如下```python
# 整数
2 + 3 # 加法运算，结果 5
2 - 3 # 减法运算，结果 -1 
3 // 2 # 整除运算，结果 1 
3 / 2 # 浮点数除法，结果 1.5
2 ** 3 # 指数运算，结果 8

# 浮点数
2.1 + 3.1 # 加法运算，结果 5.2
2.1 - 3.1 # 减法运算，结果 -1.0
3.1 / 2.1 # 浮点数除法运算，结果 1.4761904761904763
3.1 * 2.1 # 乘法运算，结果 6.51
3.1 ** 0.5 # 指数运算，结果 1.760681686165901
```### 字符串字符串顾名思义，就是一串字符，下面是几个定义字符串的例子```python
a = 'hello' 
```字符串可以单引号引起来，也可以用双引号引起来，并没有区别，比如上面的字符串也可以写成```python
a = "hello"
```双引号引起来的字符串中可以包含单引号，如下```python
a = "I'm from China" # 如果双引号引起来的字符串中可以包含单引号
```同样，单引号引起来的字符串中可以包含双引号```python
a = 'I told him, "Python is the best programming language"'
```但如果用单引号引起来的字符串中包含单引号，或者双引号引起来的字符串中包含双引号，就需要用反斜杠（\）进行转义，如下```python
a = 'I\'m from China'
a = "he says \"hello\""
```既然字符串是一串字符的组合，我们就可以截取字符串，截取字符串使用方括号[]，如下```python
a = "hello"
print(a[0]) # 打印第一个字符，输出 h
print(a[1]) # 打印第二个字符，输出 e
print(a[-1]) # -1 表示最后一个字符，输出 o
```
字符串支持几种常见的操作修改大小写```python
name = "albert einstein"
name.title() # 每个字母首字母大写，输出 'Albert Einstein'
name.upper() # 所有字母大写，输出 'ALBERT EINSTEIN'
name.lower() # 所有字母小写，输出 'albert einstein'

```拼接字符串```python
first_name = "albert"
last_name = "einstein"
first_name + " " + last_name # 输出 'albert einstein'
```删除空白```python
a = "  hello "
a.strip() # strip 方法会删除字符串开始处和结尾处的空格，所以输出 'hello'
```使用 join 方法合并多个字符串```python
print(",".join(["name", "age", "location"])) 
```上面的代码中 join 方法将括号內的字符串合并，不同字符串之间用逗号（,）分隔，所以上面的代码会输出  name,age,location
使用 split 方法将字符串拆分为序列 ```python
"name,age,location".split(",")
```split 方法将字符串拆分，括号內指定按什么符号分隔，这里是按逗号（,），所以上面的代码输出 ['name', 'age', 'location']
Python 中有一些特殊的字符串会有特殊的含义，其中一个就是换行符。换行符用 \n 表示，如下```python
newline = '\n' # 这里是一个换行符
```下面我们 print 一个带有换行符的字符串```python
print("Huawei\nXiaomi")
```因为带了换行符，这段代码的结果是这样的```text
Huawei
Xiaomi
```
说到字符串，就不得不提到格式化字符串。什么是格式化字符串呢？格式化字符串就是对数据进行格式化输出，听着很抽象，我们来看一个例子就很清楚了```python
print("My name is %s" % ("John")) 
```这里，"My name is %s" 相当于一个模板，%s 的意思是说我这个位置先占个位，具体填什么值稍后再说。那么到底填什么值呢？这个值就是后面括号里的 "John"，所以上面的代码会输出 'My name is John'。这就是格式化输出。这里的 %s 称为转换说明符，它的作用除了占个位，其实还有更一层的意思，就是表示我这个位置上的值必须是一个字符串。说到这儿，大家一定想到了，既然有字符串的转换说明符，那一定也有整数，浮点数的转换说明符。是的，我们看下面的代码```python
print("I am %d year-old" % (27)) # %d 表示整数类型，输出 'I am 27 year-old'
print("deposit rate is %f" % (5.35)) # %f 表示浮点数类型，输出 'deposit rate is 5.350000'
```除了用百分号（%），我们还可以用format方法来做格式化字符串。原理是类似的，只是写法不同，比如```python
print("{} is {} year-old".format("Jane", 5))
```这里我们用 {} 表示这里需要填入一个值。使用 {} 有一个好处，就是我们不需要指定这个值的类型，这也是它的方便之处。在 {} 里我们可以指定一个数字，比如 {1} 这样，这个大括号里数字代表的这里应该填入的是后面 format 方法里的第几个参数（ {0} 对应第一个参数，{1} 对应第二个参数，等等），比如```python
print("{0}, {1} and {2}".format("first", "second", "third")) # 输出 first, second and third
print("{2}, {1} and {0}".format("first", "second", "third")) # 输出 third, second and first
```如果是数字类型的，还可以指定精度，比如```python
print("{:.2f}".format(3.1415926)) # 显示小数点后2位，输出 3.14
```以上就是关于字符串。### 列表列表是是一个可以包含多个元素的数据结构，列表中的每个元素可以是数字、字符串、也可以是列表，看几个例子```python
squares = [1, 4, 9, 16, 25] # 全是数字组成的列表
names = ['jack', 'jane', 'jammy'] # 全是字符串组成的列表
iphone = ['iphone 11', 5000] # 由字符串和数字组成的列表
database = [['iphone 11', 5000], ['huawei p30', 3000]] # 二维列表，每个元素是列表
```下面，我们来看一下列表的常用基本操作。访问列表元素```python
# 注意：下标从0开始，而不是从1开始
squares = [1, 4, 9, 16, 25]
print(squares[0]) # 输出 1
print(database[1]) # 输出 ['huawei p30', 3000]

# 如果索引超出范围，会报错
print(squares[6]) # squares 列表一共只有5个元素，这里的6代表要访问第7个元素，所以会报错

# 可以指定负索引
print(squares[-1]) # 表示访问 squares 列表的最后一个元素，输出 25
```获取列表长度，用 len 函数```python
print(len(squares)) # 输出 5
```修改列表中的元素的值```python
squares[4] = 30 # 将下标为4的元素设成30
print(squares) # 输出 [1, 4, 9, 16, 30]

words = ['Python', 'is', 'a', 'greet', 'language']
words[3] = 'great' # 将 words 中下标为3的元素改成 great
print(words) # 输出 ['Python', 'is', 'a', 'great', 'language']
```往列表中添加元素```python
squares = [1, 4, 9, 16, 25]
squares.append(36) # 将元素36添加到 squares 末尾
print(squares) # 输出 [1, 4, 9, 16, 25, 36]
```在指定位置插入元素```python
names = ['jack', 'jane', 'jammy']
names.insert(0, 'henry') # 在 names 中下标为0的位置插入'henry'
print(names) # 输出 ['henry', 'jack', 'jane', 'jammy']
names.insert(3, 'mary') # 在 names 中下标为3的位置插入'mary'
print(names) # 输出 ['henry', 'jack', 'jane', 'mary', 'jammy']
```从列表中删除元素```python
names = ['jack', 'jane', 'jammy']
del names[0] # 删除下标为0的元素
print(names) # 输出 ['jane', 'jammy']

names = ['jack', 'jane', 'jammy']
del names[2] # 删除下标为2的元素
print(names) # 输出 ['jack', 'jane']
```根据值删除元素```python
names = ['jack', 'jane', 'jammy']
names.remove('jane') # 从 names 中删除 'jane' 这个元素 
print(names) # 输出 ['jack', 'jammy']
```列表的切片操作```python
squares = [1, 4, 9, 16, 25]
print(squares[1:3]) # 打印 squares 中从下标1到3（不包括3）的所有元素，输出 [4, 9]

# 支持指定步长
print(squares[::2]) # squares 中每隔2个元素取一个，也就是取出 squares 中下标为0，2，4的元素，输出 [1, 9, 25]
```拼接列表```python
[1, 2, 3] + [4, 5, 6] # 输出 [1, 2, 3, 4, 5, 6]
```乘法```python
# 乘法
[1] * 5 # 输出 [1, 1, 1, 1, 1]
```判断列表中是否包含值```python
names = ['jack', 'jane', 'jammy']
'jack' in names # names 中是否存在 'jack' 这个值，输出 True
'henry' in names # names 中是否存在 'henry' 这个值，输出 False
```计算最大值和最小值```python
squares = [1, 4, 9, 16, 25]
min(squares) # 输出 squares 中最小的元素 1
max(squares) # 输出 squares 中最大的元素 25
```排序```python
numbers = [1, 5, 2, 8, 3]
numbers.sort() # 将 numbers 中元素从小到大排序
print(numbers) # 输出 [1, 2, 3, 5, 8]

# sorted函数也可以对列表排序，和上面sort不同的是
# sort修改列表中的元素，而sorted保持列表中的元素不变，但是把结果返回出来
numbers = [1, 5, 2, 8, 3]
sorted(numbers) 
print(numbers) # 输出 [1, 5, 2, 8, 3]
print(sorted(numbers)) # 输出 [1, 2, 3, 5, 8]

# 降序排序
result = sorted(numbers, reverse=True) # 可以指定参数  reverse=True 来进行降序排序
print(result) # 输出 [8, 5, 3, 2, 1]
```查找值第一次出现的下标```python
names = ['jack', 'jane', 'jammy']
names.index('jane')  # 结果是 1，因为 'jane' 在列表中对应下标1的位置
```扩展列表```python
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b) # 将列表 b 的元素填入到列表 a 中
print(a) # 输出 [1, 2, 3, 4, 5, 6]
```遍历列表中的元素```python
names = ['jack', 'jane', 'jammy']
for name in names: # 遍历 names 中的每一个元素，把它打印出来
    print(name)
```列表推导式```python
squares = [x**2 for x in [1, 2, 3, 4, 5]] # 对列表中的每个元素计算平方
print(squares) # 输出 [1, 4, 9, 16, 25]
```以上就是关于列表。### 元组元组与列表很相似，唯一的区别就是**列表可修改，元组不可修改**。元组的定义使用圆括号，如下```python
squares = (1, 4, 9, 16, 25)
```上面 squares 就是一个元组。要访问元组中的值，我们可以使用和列表相同的方法，比如```python
print(squares[0]) # 打印 squares 中下标为0的元素，输出 1
print(squares[1:3]) # 打印 squares 中下标从1到3（不包括3）的元素， 输出 4，9
```前面说到元组的值是不可修改的，我们来尝试修改一下它，看看会发生什么```python
squares[2] = 10 # 修改下标为2的元素，会得到下面的错
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Input In [5], in <cell line: 2>()
      1 # 元组中的值不可修改
----> 2 squares[2] = 10

TypeError: 'tuple' object does not support item assignment
```这里程序报错，告诉我们元组是不可被修改的。### 字典字典是一种**映射**类型，是**键到值的映射**。为了帮助理解，我们可以把 Python 中的字典和我们日常生活中的字典做类比。假设有一本英汉字典，我们想要查找某一个英文单词对应的中文含义，我们会怎么做呢？我们会首先在字典里找到这个英文单词的条目，然后查看它的中文含义。同样的，Python 中的字典也是这样存储信息的。字典的键值对就好比英汉字典中的英文单词和中文含义，给我们一个键，我们就能查到它对应的值。下面是一个电话号码簿的例子```python
tel = {"john": "111", "jane": "222", "jack": "333"}
```获取键对应的值```python
tel["john"] # 获取 john 的电话号码，结果 '111'
```修改键对应的值```python
tel['john'] = '555'
```删除一个键```python
del tel['john'] # 把 john 的号码从号码簿中删除
print(tel) # 输出 {'jane': '222', 'jack': '333'}
```检查字典中是否包含键```python
'jane' in tel # 结果 True
```访问不存在的键会报错```python
tel = {"john": "111", "jane": "222", "jack": "333"}
tel['henry'] # 会报下面的错
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
Input In [28], in <cell line: 2>()
      1 tel = {"john": "111", "jane": "222", "jack": "333"}
----> 2 print(tel["henry"])

KeyError: 'henry'
```get 方法获取值```python
print(tel.get("henry")) # 不会报错，输出 None
print(tel.get("henry", "N/A")) # 这里传入了一个参数告诉 get 方法，如果 henry 这个键不存在，就输出 'N/A'
```keys 方法获取字典中所有的键```python
print(tel.keys()) # 输出 dict_keys(['john', 'jane', 'jack'])
```values 方法获取字典中所有的值```python
print(tel.values()) # 输出 dict_values(['111', '222', '333'])
```items 方法返回包含字典中所有键值对的列表```python
print(tel.items()) 输出 dict_items([('john', '111'), ('jane', '222'), ('jack', '333')])
```setdefault 方法获取键对应的值，当键不存在的时候，setdefault 给这个键设定一个默认值```python
tel = {"john": "111", "jane": "222", "jack": "333"}
tel.setdefault('henry', 'N/A') # 因为 henry 这个键不存在，把它的值设成 'N/A'
print(tel) # 输出 {'john': '111', 'jane': '222', 'jack': '333', 'henry': 'N/A'}
```
以上就是这一节的全部内容。这一节我们详细的介绍了 Python 中的几种基本的数据类型，在下一节中我们将介绍计算机程序中的另一个要素——语句。#### 语句Python 中的语句主要有以下几类+ import 语句
+ 赋值语句
+ 条件语句
+ 循环语句
下面我们来逐个看下每种类型的语句。### import 语句前面说到过，import 语句用于导入模块。模块就好比是一个工具箱，导入模块就是说，我们把这个工具箱准备好，接下来我们要打开工具箱使用里面的工具了。有这样几种导入方式导入时重命名模块```python
import math as m # 将 math 模块重命名成 m
m.sqrt(2) 
```导入模块中的指定函数```python
from math import sqrt # 导入 math 模块中的 sqrt 函数
sqrt(2) # 调用 sqrt 函数
```导入模块中的一切```python
from math import * # 星号*代表导入一切内容，包括函数、变量等等，下面的 sqrt，floor 都是 math 模块中的函数
sqrt(2) 
floor(2.1) 
```### 赋值Python 中有这样几种不同的赋值方式单个变量赋值，这是最简单的赋值方式```python
x = 1
```同时给多个变量赋值```python
x, y = (1, 2)
print(x) # 输出 1
print(y) # 输出 2
```链式赋值```python
x = y = z = 1
print(x, y, z) # 输出 1 1 1
```增强赋值```python
x += 1 # 相当于 x = x + 1
```### 缩进Python 中使用缩进来创建代码块，像下面这样```python
a = 5
for i in range(10):
    if i == a:
        print(i)
        break
```在上面的代码中，if 这一行比上面的 for 这一行缩进了4个空格，从 if 开始的这三行是属于 for 语句的代码块。if 下面的 print 这一行比 if 这一行又缩进了4个空格。，从 print 开始的这两行是属于 if 语句的代码块。Python 中对于缩进量没有限制，可以是3个空格，可以是4个空格，也可以是一个tab，但是**所有的缩进量必须统一**。也就是，如果用3个空格作为缩进量，那代码中所有的缩进量都必须是3个空格。一般推荐的做法是：**使用4个空格作为缩进量**。### 条件语句条件语句用来测试条件是真是假，然后根据测试的结果执行相应的代码块，条件语句包括 if 语句，elif 子句和 else 子句。我们用代码来举例```python
a = 0
if a > 0:
    print("a is positive")
elif a == 0:
    print("a is zero")
else:
    print("a is negative")
```if 判断条件是否为真，当 if 判断不为真时，会判断 elif 子句（可以存在多个 elif 子句），如果 elif 都不为真，那么执行 else。上面的例子中，因为 a = 0，所以 if a > 0 为假，而 elif a == 0 为真，所以就执行 elif 下面的代码块，于是输出 a is zero。当我们要检查多个条件时，可以用 and 和 or 关键字。使用 and 表示只有当 and 左右两边的条件都满足，这个结果才为真，否则就为假，如下```python
age1 = 20
age2 = 16
age1 < 18 and age2 < 18 # 结果为False，因为 age1 < 18 为假
```使用 or 表示只要 or 左右两边的条件中有一个满足，这个结果就为真，如果两边条件都不满足，那就为假，比如```python
age1 = 20
age2 = 16
age1 < 18 or age2 < 18 # 结果为True，因为 age2 < 18为真
```### 循环语句循环是在条件判断为真时，不断的执行代码块，直到条件判断为假，结束循环。循环有 while 循环和 for 循环。while 循环如下```python
x = 1
while x <= 10:
    print(x)
    x += 1
```x 每次加1，只要 x <= 10，就不断地执行代码块，直到 x 的值大于10为止。上面的代码会输出下面的结果```text
1
2
3
4
5
6
7
8
9
10
```for 循环如下```python
text = ["John", "is", "an", "analyst"]
for word in text:
    print(word)
```text 是一个列表，里面包含4个单词，for 循环中我们会遍历 text 中所有的元素，将它赋给 word 变量，然后在循环体內把 word 打印出来。上面的代码会输出下面的结果```text
John
is
an
analyst
```和 for 循环经常一起出现的，有一个 range 函数，非常好用。range 函数的作用是返回一个整数序列，比如```python
range(10) # 创建一个从0-9的10个整数的序列，即 0，1，2，3，4，5，6，7，8，9
range(5, 10) # 创建一个从5-9的5个整数的序列，即 5，6，7，8，9
```我们经常会把 range 和 for 循环结合起来使用，比如```python
for i in range(5):
    print(i)
```这样就可以用非常简洁的代码执行一定次数的循环。### 跳出循环循环中的代码块会不停的执行，直到条件判断为假，但有的时候，我们想提前结束，应该怎么办呢？我们可以使用 break 跳出循环，如下```python
for i in range(6):
    print(i)
    if i == 3:
        break
```上面的代码中，我们依次遍历0到5这6个整数，但是当遍历到3的时候，我们使用 break 跳出循环，循环就此停止，不再往下执行了，也就说后面的4和5这两个整数不会被遍历到了，因为在遍历到之前，我们已经跳出了循环，所以上面的代码会输出```text
0
1
2
3
```### 强制进入下一次循环有的时候，在执行循环的时候，当满足一定的条件时，我们想跳过剩下的代码，直接进入下一次循环，这时我们可以使用 continue 强制进入下一次循环，如下```python
for i in range(6):
    if i < 3:
        continue
    print(i)
```上面的代码中，我们依次遍历0到5这6个数字，但是当遍历的数字小于3的时候，我们不想打印出来，所以直接用 continue 跳过后面的代码，进入下一次遍历。这段代码输出的结果如下```text
3
4
5
```### 重温列表推导式前面我们提到过列表推导式，列表推导式其实类似 for 循环，比如```python
[x**2 for x in range(10)]
```这段代码的含义是对于0-9这10个整数，计算它们的平方。所以结果是 [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]我们也可以在列表推导式中添加 if 语句，比如```python
[x**2 for x in range(10) if x % 2 == 0]
```这段代码的意思是对于0-9这10个整数，只有当它能被2整除的时候，我们才计算它的平方，所以结果是 [0, 4, 16, 36, 64]我们也可以添加多层 for，像下面这样```python
[(x, y) for x in range(3) for y in range(3)]
```这段代码中 x 和 y 会分别遍历0-2这3个整数，所以它生成的结果是一个包含9个二元组的列表，如下```text
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
```
好了，到目前为止，我们已经学了不少Python的基础知识了，还记得最开始的一行代码画爱心的例子吗？我们现在运用我们已经学过的知识，来动手操练一下。### 实操——一行代码画爱心首先需要知道，爱心曲线有一个公式![](https://www.zhihu.com/equation?tex=%28x%5E%7B2%7D+%2B+y%5E%7B2%7D+-+1%29%5E%7B3%7D+-+x%5E%7B2%7Dy%5E%7B3%7D+%3D+0) 在坐标系上画出来是这样的![]({static}/images/v2-1809f5f02d8f23e718ba5949506a2a66_r.jpg)有了这个公式，我们可以根据这个公式来判断一个点是在爱心的内部还是外部，如果点在爱心内部我们用字母填充，如果点在爱心外部我们用空格填充，通过这样的方式我们打印出爱心的形状。我们把打印范围限制在60行x60字符的范围內，进一步我们把这个范围划分成60x60个格子，像下面这样![]({static}/images/v2-553f8ea0503a7b5a25c43629ad30345f_r.jpg)每个格子都有一个坐标。我们的横坐标从-30到30，纵坐标从30到-30。我们要做的就是在这个每个格子里填入一个空格或者Love中的一个字母，让最终的结果看起来是一颗爱心的形状。我们可以这样做，对于上图中的每一个格子，如果坐标是在爱心外，我们就输出一个空格，如果坐标是在爱心内，就输出Love 4个字母中的一个。我们从第一行开始，对每一个格子输出空格或字母，然后第二行，第三行，直到最后一行。当我们遍历完所有的行之后，我们就完成了所有字符的打印。我们用 for 循环来实现一下上面的逻辑，代码如下```python
for y in range(30, -30, -1):
    for x in range(-30, 30):
        if ((x*0.04)**2+(y*0.1)**2-1)**3-(x*0.04)**2*(y*0.1)**3 <= 0: # 套用公式
            # 这里是爱心内部，我们依次输出 Love 4 个字母中的一个，循环反复
            print('Love'[(x-y) % len('Love')], end='')
        else:
            # 这里是爱心外部，我们输出空格
            print(' ', end='')
    print('')
```上面的第一层 for 循环遍历所有的行，第二层 for 循环遍历所有的列。if((x*0.04)**2+(y*0.1)**2-1)**3-(x*0.04)**2*(y*0.1)**3<=0 这一行代码判断点是否在爱心内部。如果是的话，我们打印 Love 4个字母中的一个，如果不是，我们打印一个空格。执行上面的代码，可以看到我们已经实现我们想要的功能。接下来，我们简化代码。对于第二层循环，也就是遍历列的操作，我们用列表推导式来简化，如下```python
for y in range(30, -30, -1):
    print(''.join([('Love'[(x-y) % len('Love')] if ((x*0.04)**2+(y*0.1)**2-1)**3-(x*0.04)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]))
```上面，对于某一行，我们用列表推导式生成这一行所有的字符，然后用 ''.join() 把它们拼接到一起。我们进一步简化，把第一层循环，也就是对于行的遍历也用列表推导式来简化，如下```python
print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.04)**2+(y*0.1)**2-1)**3-(x*0.04)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
```我们用另一个列表推导式生成所有行的内容，然后用 '\n'.join() 把这些行拼接到一起。这样，我们就完成了用一行代码打印爱心的程序。是不是很酷！以上就是这一节的全部内容。这一节我们介绍了 Python 中各种各样的语句，这些都是 Python 的基本功，在学习过程中，我们要多加练习，熟练掌握它们。下一节我们将介绍函数。未完待续

