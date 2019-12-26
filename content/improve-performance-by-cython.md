Title: 用Cython和PyPy提升Python性能
url: improve-performance-by-cython.html
save_as: improve-performance-by-cython.html
Date: 2018-03-22
Category: Python
Tags: Python
Authors: Zhongqiang Shen

最近在比较Python和Java的性能。Python在做科学计算方面的性能的确蛮弱的，但网上查阅了一些文档，发现有很多方法可以优化Python的性能。这里以一个简单的积分程序为例，尝试用几种方法优化Python性能，并将优化的结果做个比较。

这里计算的积分如下

![](http://www.zhihu.com/equation?tex=%5Cint_%7Ba%7D%5E%7Bb%7De%5E%7B-x%5E%7B2%7D%7D) 

未作优化的Python代码如下

```python
def integrate_f(a, b, N):
    s = 0
    dx = (b-a) /N
    for i in range(N):
        s += 2.71828182846**(-(a+i*dx)**2)
    return s*dx

if __name__ == "__main__":
    print integrate_f(1.0,10.0, 100000000)

```

在自己的机器上执行这段代码，耗时46.33s




同样功能的Java代码

```java
import java.lang.Math;

public class Test {
    public static double integrate_f(double a, double b, int N) {
        double s = 0;
        double dx = (b-a)/N;
        for(int i =0; i <N; i++) {
            s += Math.pow(2.71828182846, -Math.pow(a+i*dx, 2));
        }
        return s*dx;
    }
    public static void main(String args[]) {
        double result = integrate_f(1,10, 100000000);
        System.out.println(result);
    }
}

```

编译后执行，耗时8.58s




下面用几种方法优化上面的Python的代码

**1. PyPy**

一般说Python都是指CPython解释器，CPython是广泛接受的Python标准。PyPy是另一个解释器，使用了JIT编译，和CPython高度兼容。不过PyPy的缺点是不支持C扩展模块，所以如果程序中用到Numpy，Scipy，就没法用PyPy优化了。

用PyPy执行上面的python程序，耗时8.16s。

**2. Numba**

Numba是一个加速Python执行的库，可以用其中的JIT编译加速代码的执行。使用Numba JIT的代码如下

```python
from numba import jit
@jit
def integrate_f(a, b, N):
    s = 0
    dx = (b-a) /N
    for i in range(N):
        s += 2.71828182846**(-(a+i*dx)**2)
    return s*dx

if __name__ == "__main__":
    print integrate_f(1.0,10.0, 100000000)

```

使用numba的代码执行耗时14.41s。

**3. Cython**

Cython将Python代码编译成C源码，再把C源码转换成Python扩展模块。用Cython改写Python代码，将动态类型用Cython中的静态类型声明后，可以大大提升执行的效率。

不过用Cython优化的步骤有点复杂。需要先生成Python扩展模块，然后在另外一个程序里import这个模块并调用模块中的方法。

Cython改写的代码如下：

```python
def integrate_f(double a, double b, int N):
    cdef double s = 0
    cdef int i
    cdef double dx = (b-a) /N
    for i in range(N):
        s += 2.71828182846**(-(a+i*dx)**2)
    return s*dx

if __name__ == "__main__":
    print integrate_f(1,10, 100000000)

```

执行Cython优化的代码，耗时7.36s。




下图展示了上述优化前和优化后的性能比较：

![]({static}/images/v2-2192bca03dcb5a441ed5aece94dea038_r.jpg)

可以看到，三种优化方式对性能都有很大的提升，其中Cython优化代码后对性能的提升最大。用Cython优化后的执行时间（7.36s）差不多比未经优化的CPython代码（46.33s）少了一个数量级，和Java版本（8.58s）的性能相当。




**总结**

在涉及大量科学计算的项目中，通过优化Python还是有希望达到非常不错的性能的。Python自带了很多做科学计算的库，如Numpy，Scipy等，底层都是用C实现的，性能上已经做了很大的优化。如果需要自己实现算法，也可以用Cython做优化，将耗费CPU的部分编译成高效的C代码来达到性能的提升。

