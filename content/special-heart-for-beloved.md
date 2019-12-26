Title: 520用Python画一颗特别的♥送给她
url: special-heart-for-beloved.html
save_as: special-heart-for-beloved.html
Date: 2018-05-20
Category: Python
Tags: Python
Authors: Zhongqiang Shen

今天520，大家有没有和心爱的女生在一起呢？

今天我们来用Python画一颗特别的爱心，送给那个特别的她，给她一份浪漫的惊喜吧~



还记得那个心形曲线的公式吗？

![](http://www.zhihu.com/equation?tex=%28x%5E%7B2%7D%2By%5E%7B2%7D-1%29%5E%7B3%7D-x%5E%7B2%7Dy%5E%7B3%7D%3D0) 

我们用Python基于上面的公式来画一画爱心吧~




#### 准备工作

代码中用到numpy和matplotlib，需要先安装这两个库

```bash
pip3 install numpy
pip3 install matplotlib

```




#### 爱心基本款

我们先来画一颗最朴素的爱心

```python
import numpy as np
import matplotlib.pyplot as plt

x_coords = np.linspace(-100, 100, 500)
y_coords = np.linspace(-100, 100, 500)
points = []
for y in y_coords:
    for x in x_coords:
        if ((x*0.03)**2+(y*0.03)**2-1)**3-(x*0.03)**2*(y*0.03)**3 <= 0:
            points.append({"x": x, "y": y})
heart_x = list(map(lambda point: point["x"], points))
heart_y = list(map(lambda point: point["y"], points))

plt.scatter(heart_x, heart_y, s=10, alpha=0.5)
plt.show()

```

运行后上面的代码会显示下面的图

![]({static}/images/v2-84fbd1170f8691f40c30590575cd2a08_r.jpg)

爱心的形状有了，接下来我们来解锁高级定制款，给爱心填充不同的颜色。




#### 爱心高级定制款

给爱心填充不同的颜色，只需在上面代码的scatter函数中指定cmap参数即可，如下

```python
plt.scatter(heart_x, heart_y, s=10, alpha=0.5, c=range(len(heart_x)), cmap=<cmap>)

```




下面是不同色系的定制款

<cmap="autumn"> 橙色的爱心送给热情洋溢的她

![]({static}/images/v2-b53db16256d7c9fd8b4274195efebdd2_r.jpg)




<cmap="cool"> 紫色的爱心送给优雅宁静的她

![]({static}/images/v2-62bfdd9c5e2fe5b1639b825f47009320_r.jpg)




<cmap="magma"> 晚霞般的爱心送给醇厚脱俗的她

![]({static}/images/v2-88d2cf35d938685cafac388f389cf6b3_r.jpg)




<cmap="rainbow"> 彩虹般的爱心送给充满绚丽幻想的她

![]({static}/images/v2-48f56ffc60082dcfab467d8371bf6fbc_r.jpg)




<cmap="Reds"> 炽热的爱心送给热烈奔放的她

![]({static}/images/v2-c6ecaa9f7e5e5b645caeedbf3d52021d_r.jpg)




<cmap="spring"> 青春的爱心送给充满朝气的她

![]({static}/images/v2-885690905761323f5e0d9959066e42e2_r.jpg)




<cmap="viridis"> 翡翠色的爱心送给平静柔和的她

![]({static}/images/v2-e88092fb87f9e2e465026611128615b3_r.jpg)




<cmap="gist\_rainbow"> 五彩缤纷的爱心送给多姿多彩的她

![]({static}/images/v2-4110f68d43f8dfa8272a496500c65946_r.jpg)




大家是不是学会了呢 ？

最后祝大家520快乐！




本文已更新微信同名公众号，欢迎扫一扫关注~

![]({static}/images/v2-e9b0b9b9584ccdd3ff4c96b7ecfd8a56_r.jpg)



