Title: 50行代码实现人脸检测
url: python-face-detection.html
save_as: python-face-detection.html
Date: 2018-06-23
Category: 图像处理
Tags: Python, 图像处理
Authors: Zhongqiang Shen

现在的人脸识别技术已经得到了非常广泛的应用，支付领域、身份验证、美颜相机里都有它的应用。用iPhone的同学们应该对下面的功能比较熟悉

![]({static}/images/v2-ccf07fb5689f8b6037eb619a5a5ce11a_r.jpg)

iPhone的照片中有一个“人物”的功能，能够将照片里的人脸识别出来并分类，背后的原理也是人脸识别技术。

这篇文章主要介绍怎样用Python实现人脸检测。人脸检测是人脸识别的基础。人脸检测的目的是识别出照片里的人脸并定位面部特征点，人脸识别是在人脸检测的基础上进一步告诉你这个人是谁。

好了，介绍就到这里。接下来，开始准备我们的环境。

#### 准备工作

本文的人脸检测基于dlib，dlib依赖Boost和cmake，所以首先需要安装这些包，以Ubuntu为例：

```bash
$ sudo apt-get install build-essential cmake
$ sudo apt-get install libgtk-3-dev
$ sudo apt-get install libboost-all-dev

```

我们的程序中还用到numpy，opencv，所以也需要安装这些库：

```bash
$ pip install numpy
$ pip install scipy
$ pip install opencv-python
$ pip install dlib

```

人脸检测基于事先训练好的模型数据，从这里可以下到模型数据

[http://](http://link.zhihu.com/?target=http%3A//dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)

下载到本地路径后解压，记下解压后的文件路径，程序中会用到。




#### dlib的人脸特征点

上面下载的模型数据是用来估计人脸上68个特征点(x, y)的坐标位置，这68个坐标点的位置如下图所示：

![]({static}/images/v2-b67561b84f543b5d3138c8fcdb580f91_r.jpg)

我们的程序将包含两个步骤：

第一步，在照片中检测人脸的区域

第二部，在检测到的人脸区域中，进一步检测器官（眼睛、鼻子、嘴巴、下巴、眉毛）




#### 人脸检测代码

我们先来定义几个工具函数：

```python
def rect_to_bb(rect):
    x = rect.left()
    y = rect.top()
    w = rect.right() - x 
    h = rect.bottom() - y 
    return (x, y, w, h)

```

这个函数里的rect是dlib脸部区域检测的输出。这里将rect转换成一个序列，序列的内容是矩形区域的边界信息。




```python
def shape_to_np(shape, dtype="int"):
    coords = np.zeros((68, 2), dtype=dtype)
    for i in range(0, 68):
            coords[i] = (shape.part(i).x, shape.part(i).y)

    return coords

```

这个函数里的shape是dlib脸部特征检测的输出，一个shape里包含了前面说到的脸部特征的68个点。这个函数将shape转换成Numpy array，为方便后续处理。




```python
def resize(image, width=1200):
    r = width * 1.0 / image.shape[1]
    dim = (width, int(image.shape[0] * r)) 
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return resized

```

这个函数里的image就是我们要检测的图片。在人脸检测程序的最后，我们会显示检测的结果图片来验证，这里做resize是为了避免图片过大，超出屏幕范围。




接下来，开始我们的主程序部分

```python
import sys 
import numpy as np
import dlib
import cv2 

if len(sys.argv) < 2:
    print "Usage: %s <image file>" % sys.argv[0]
    sys.exit(1)

image_file = sys.argv[1]
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

```

我们从sys.argv[1]参数中读取要检测人脸的图片，接下来初始化人脸区域检测的detector和人脸特征检测的predictor。shape\_predictor中的参数就是我们之前解压后的文件的路径。




```python
image = cv2.imread(image_file)
image = resize(image, width=1200)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rects = detector(gray, 1)

```

在检测特征区域前，我们先要检测人脸区域。这段代码调用opencv加载图片，resize到合适的大小，转成灰度图，最后用detector检测脸部区域。因为一张照片可能包含多张脸，所以这里得到的是一个包含多张脸的信息的数组rects。




```python
for (i, rect) in enumerate(rects):
    shape = predictor(gray, rect)
    shape = shape_to_np(shape)

    (x, y, w, h) = rect_to_bb(rect)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    for (x, y) in shape:
            cv2.circle(image, (x, y), 2, (0, 0, 255), -1) 

cv2.imshow("Output", image)
cv2.waitKey(0)

```

对于每一张检测到的脸，我们进一步检测脸部的特征（鼻子、眼睛、眉毛等）。对于脸部区域，我们用绿色的框在照片上标出；对于脸部特征，我们用红色的点标出来。

最后我们把加了检测标识的照片显示出来，waitKey(0)表示按任意键可退出程序。

以上是我们程序的全部




#### 测试

接下来是令人兴奋的时刻，检验我们结果的时刻到来了。

下面是原图

![]({static}/images/v2-30d21aba6fe402350b11ffe0176ad435_r.jpg)

下面是程序识别的结果

![]({static}/images/v2-1d6ea38d9b087abb9cb84f76573014b6_r.jpg)

可以看到脸部区域被绿色的长方形框起来了，脸上的特征（鼻子，眼睛等）被红色点点标识出来了。

是不是很简单？




欢迎点赞~ 

视点赞情况，后续再另开一篇写写怎样实现人脸识别，告诉你照片里的人是谁。




本文已更新微信同名公众号【Python与数据分析】，欢迎关注~

![]({static}/images/v2-e9b0b9b9584ccdd3ff4c96b7ecfd8a56_r.jpg)



