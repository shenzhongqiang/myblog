Title: 用Python给图片加上抖音效果
url: douyin-effect-image.html
save_as: douyin-effect-image.html
Date: 2018-06-15
Category: 图像处理
Tags: Python, 图像处理
Authors: Zhongqiang Shen

前一篇 [Python实现抖音体](https://zhuanlan.zhihu.com/p/37951669) 给文字加上抖音效果，这一篇我们来用Python给图片加上抖音效果。原理其实是类似的，这里我们详细地讲解一下过程，并且给出代码实现。




#### 准备工作

程序用到Pillow，numpy，需要安装这些库

```bash
pip3 install Pillow
pip3 install numpy

```




#### 基本原理

我们来观察一下抖音的logo

![]({static}/images/v2-291e75da28f3d0ada7a7e719a908df44_r.jpg)

上面这张图其实就是一张蓝绿色的图片和一张红色的图片略微错开后叠加在一起。这就是生成抖音效果的基本原理。




我们来做一个简单的实验，这里有一张蓝绿色的正方形

![]({static}/images/v2-ba2b80b203b1c867309f052ca1f2fee9_b.jpg)

和一张红色的正方形

![]({static}/images/v2-7216e62eef417aae12af4444e441cd59_b.jpg)

两张图片已错开一定位置，所以不完全重叠。

现在我们将两张图片相加

![]({static}/images/v2-edc2486a68d32c73ef66df3894c0f9c7_b.jpg)

得到的效果和上面抖音的logo是类似的，这正是我们想要的效果。




那用程序怎样实现上面的效果呢？

其实很简单。计算机里的每张图片都是由一系列的像素组成。对于RGB模式的图片，每个像素点都是一个三元组 (r, g, b)，分别对应红色、绿色和蓝色通道的值。每一张图片都是一个三维数组，保存了了每行每列上的每个像素点的信息。

下面是一张图片的三维数组

```text
[
  [[ 90  88 110], [ 76  73  94], [ 63  60  79], ..., [ 24  26  21], [ 23  25  20], [ 22  24  19]],
  [[131 132 153], [119 120 141], [112 110 131], ..., [ 23  25  20], [ 22  24  19], [ 22  24  19]],
  ...
]

```

每个三元组都是一个像素点，三元组中的值分别代表R，G，B三个通道的值。

前面蓝绿色正方形和红色正方形叠加的过程其实就是两张图片对应的三维数组相加的过程。蓝绿色正方形的每个像素点的值都是 (0, 255, 255)，红色正方形每个像素点的值是 (255, 0, 0)，不重叠的地方就是两张图片各自原来的颜色，重叠的地方就是 (0, 255, 255) + (255, 0, 0) = (255, 255, 255)，也就是我们看到的白色。

理解了上面的原理，要生成抖音效果的图片，我们只需要基于原图生成一张R通道的图片和一张GB通道的图片，略微错开后，生成两个三维数组，然后将两个数组相加就可以了。




#### 代码实现

我们使用Pillow库和numpy库来把图片转换成三维数组。

首先打开图片，假设原图的路径存在filepath中，如下

```python
from PIL import Image
import numpy as np

img_orig = Image.open(filepath) 

```




将图片转化成三维数组

```python
array_orig = np.array(img_orig)

```




复制原图的三维数组，将G和B通道的值设为0，只剩下R通道的值非0，这样操作后就生成了只包含R通道的图片

```python
array_r = np.copy(array_orig)
array_r[:,:,1:3] = 0
image_r = Image.fromarray(array_r)

```




同样的，生成GB通道的图片，只需要把R通道的值设为0，如下

```python
array_gb = np.copy(array_orig)
array_gb[:,:,0] = 0
image_gb = Image.fromarray(array_gb)

```




接下来，生成一张黑色背景的画布，把R通道的图片贴在画布上，这里粘贴的位置设成 (5, 5) 是为了与GB通道的图片错开位置

```python
canvas_r = Image.new("RGB", img_orig.size, color=(0,0,0))
canvas_r.paste(image_r, (5, 5), image_r)

```




对于GB通道的图片也是类似，贴在另一张画布上，粘贴的位置设成 (0, 0)，与上面R通道的图片错开一定位置

```python
canvas_gb = Image.new("RGB", img_orig.size, color=(0,0,0))
canvas_gb.paste(image_gb,(0,0), image_gb)

```




将两张画布的三维数组相加，合成效果并显示

```python
result_array = np.array(canvas_r) + np.array(canvas_gb)
result = Image.fromarray(result_array)
result.show()

```




#### 测试

好了，令人兴奋的时刻到来了，我们来检验一下我们的成果~

这是原图，一直贱贱的小柴犬

![]({static}/images/v2-51b2328f8356a0725b8ae1772d01e21f_r.jpg)




这是程序生成的图片

![]({static}/images/v2-810b2350884291749317a744d8dfac04_r.jpg)

加上特效后仿佛看到了动图的效果。是不是很有趣~ 




完整代码已上传GitHub。公众号【**Python与数据分析**】后台回复“抖音”可获取代码地址。




![]({static}/images/v2-ea99d43d4233dc22bca1718b50db60c2_b.jpg)





