Title: 用Python算一算n阶乘的末尾有几个零
url: algorithms-tailing-zeros-for-factorial
save_as: algorithms-tailing-zeros-for-factorial.html
Date: 2018-07-04
Category: Pyton
Tags: Python
Authors: Zhongqiang Shen

这是Lintcode第二题，原题在此 [尾部的零](http://link.zhihu.com/?target=https%3A//www.lintcode.com/zh-cn/old/problem/trailing-zeros/)。题目虽然标为“简单”，但答对率却不高。

看到这一题，比较直观的想法是计算从1到n的连乘，但这样很容易溢出，因为乘起来的数字太大。

换一个思路，我们将n阶乘做质因数分解，将n阶乘表示成

![](http://www.zhihu.com/equation?tex=n%21+%3D+a+%5Ctimes+2%5E%7Bm%7D+%5Ctimes+5%5E%7Bk%7D) 

其中a, m, n都是非负整数，且a不能被2和5整除。

上面的表达式中，每一对2和5都贡献了一个末尾的零，所以我们只要知道n的阶乘中有多少个因子2，有多少个因子5，求两者的最小值 ![](http://www.zhihu.com/equation?tex=min%28m%2C+k%29) 就是末尾零的个数了。




我们先来看一下n的阶乘有多少个因子5。

![](http://www.zhihu.com/equation?tex=n%21+%3D+1+%5Ctimes+2+%5Ctimes+3+%5Ctimes+...+%5Ctimes+n) 

从1到n中，每一个5的倍数都至少贡献了一个5，比如数字5，10，15，都贡献了一个5。每个 ![](http://www.zhihu.com/equation?tex=5%5E%7B2%7D) 的倍数都至少贡献了两个5，比如数字25，50。所以n的阶乘中包含的5的因子的个数，可以用下面的表达式来计算

![](http://www.zhihu.com/equation?tex=k+%3D+%5Cleft%5B+n%2F5+%5Cright%5D+%2B+%5Cleft%5B+n%2F5%5E%7B2%7D+%5Cright%5D+%2B+%5Cleft%5B+n%2F5%5E%7B3%7D+%5Cright%5D+%2B+...) 

同样的，n的阶乘包含的2的因子的个数可以用下面的表达式计算

![](http://www.zhihu.com/equation?tex=m+%3D+%5Cleft%5B+n%2F2+%5Cright%5D+%2B+%5Cleft%5B+n%2F2%5E%7B2%7D+%5Cright%5D+%2B+%5Cleft%5B+n%2F2%5E%7B3%7D+%5Cright%5D+%2B+...) 

很显然 m > k。前面说过，末尾零的个数是 ![](http://www.zhihu.com/equation?tex=min%28m%2C+k%29) 也就是k了。




理解了上面的步骤，接下来就可以用代码来实现算法了，如下

```python
def trailing_zero_num(n):
    num = 0

    while True:
        n = int(n / 5)
        if n == 0:
            break
        num = num + n

    return num

```

代码其实很简单。我们来思考两个问题

1. + 上面的代码的算法复杂度是多少？
2. + 上面的代码中用到了这样一个假设： 


