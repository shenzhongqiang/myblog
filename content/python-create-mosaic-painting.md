Title: 用Python生成马赛克画
url: python-create-mosaic-painting.html
save_as: python-create-mosaic-painting.html
Date: 2018-09-12
Category: 图像处理
Tags: Python, 图像处理
Authors: Zhongqiang Shen

大家知道马赛克画是什么吗？不是动作片里的马赛克哦~~

马赛克画是一张由小图拼成的大图，本文的封面就是我们的效果图，放大看细节，每一块都是一张独立的图片，拼在一起组成一张大图，感觉像是用马赛克拼出来的画，所以叫马赛克画。看到网上的一些马赛克画觉得很酷，于是自己用Python实现了一下将一张原图转换成马赛克画。




封面的原图是这样的

![]({static}/images/v2-02d2a072293c25d903646202c30e8410_r.jpg)




实现的具体思路是这样

第一步：首先收集一组图片，这些图片会作为大图中的小方格图片。图片越多，最后生成的图片颜色越接近。

第二步：将要转换的图片分割成一个一个小方格图片，像下面这样

![]({static}/images/v2-13616576364baef8063e962f9cb8ae6e_r.jpg)

第三步：对于每一个小方格图片，取图片集里面最接近的图片替换。所有小方格都替换后，就生成了我们最终的马赛克画。

听上去是不是很简单？




我们来看一下具体的实现步骤，下面是一些核心代码。完整代码可在公众号【Python与数据分析】后台回复“mosaic”获取。


我们的图片集存在images目录下，下面的代码加载目录下所有的图片，并缩放成统一的尺寸

```python
import re
import os
import cv2
import numpy as np
from tqdm import tqdm

IMG_DIR = "images"

def load_all_images(tile_row, tile_col):
    img_dir = IMG_DIR
    filenames = os.listdir(img_dir)
    result = []
    print(len(filenames))
    for filename in tqdm(filenames):
        if not re.search(".jpg", filename, re.I):
            continue
        try:
            filepath = os.path.join(img_dir, filename)
            im = cv2.imread(filepath)
            row = im.shape[0]
            col = im.shape[1]
            im = resize(im, tile_row, tile_col)
            result.append(np.array(im))
        except Exception as e:
            msg = "error with {} - {}".format(filepath, str(e))
            print(msg)
    return np.array(result, dtype=np.uint8)

```

这里load\_all\_images函数的参数就是统一后的尺寸，tile\_row和tile\_col分别对应高和宽。




下面的代码对要转换的图片进行分割

```python
img = cv2.imread(infile)
tile_row, tile_col = get_tile_row_col(img.shape)
for row in range(0, img_shape[0], tile_row):
    for col in range(0, img_shape[1], tile_col):
        roi = img[row:row+tile_row,col:col+tile_col,:]

```

我们将要转换的图片分割成一个个小方格，tile\_row和tile\_col是小方格的高和宽，roi存取小方格中的图片数据。




下面是计算两张图片相似度的函数

```python
from scipy.spatial.distance import euclidean
def img_distance(im1, im2):
    if im1.shape != im2.shape:
        msg = "shapes are different {} {}".format(im1.shape, im2.shape)
        raise Exception(msg)
    array1 = im1.flatten()
    array2 = im2.flatten()
    dist = euclidean(array1, array2)
    return dist

```

im1和im2是两张图片的数据，图片数据是一个三维的numpy数组，这里我们将三维数组转换成一维数组后，比较两者的欧式距离。之后要找出最相似的图片，只需遍历图片集中所有的图片，找到距离最短的那张图片，去替换原图中的小方格就可以了。




我们再来看一下最终实现的效果

![]({static}/images/v2-97cb4cfc307a40b0121560e6f1de3dcd_r.jpg)

放大图中局部的细节如下

![]({static}/images/v2-c4506d984d721fb8cfbd9f502911d36d_r.jpg)

如果对图片的画质不满意，想要更精细的画质，可以考虑在分割的时候把图片分割成更小的方格，不过这样也会增加程序运行的时间。

生成图片的过程比较耗时，考虑到性能原因，原程序中使用多进程的方式并行处理。




完整代码已上传github，公众号【Python与数据分析】后台回复“mosaic”可获取地址。



