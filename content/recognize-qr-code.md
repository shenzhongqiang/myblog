Title: 10行代码识别二维码
url: recognize-qr-code
save_as: recognize-qr-code.html
Date: 2018-06-23
Category:
Authors: Zhongqiang Shen

二维码现在已深入到我们生活的方方面面了，手机支付、微信加好友、app下载、电子票务等方方面面都有它的身影。最近坐地铁又推出了扫二维码进出站。

最近一段时间，上海的很多地铁检票机器都装上了像下面这样的二维码扫描器

![]({static}/images/v2-acebb23eaff588dc3f0844726d0605c0_r.jpg)

只需打开手机app上的二维码，对准扫描窗口扫一扫，就可以进站，到站后再扫一扫，就可以出站并自动扣款。

今天我们就来用Python实现一个简单的识别二维码的程序。




#### 准备工作

识别二维码需要用到zbar，首先安装libzbar0，以Ubuntu为例

```bash
sudo apt-get install libzbar0

```




接着安装pyzbar和opencv

```bash
pip install pyzbar
pip install opencv-python

```




#### 代码实现

接下来是我们的代码实现部分了，可以看到代码非常简单。

```python
# -*- coding: utf-8 -*-
# filename: read_qrcode.py
import sys 
from pyzbar.pyzbar import decode
import cv2 

if len(sys.argv) < 2:
    print "Usage: %s <image file>" % sys.argv[0]
    sys.exit(1)

filepath = sys.argv[1]
image=cv2.imread(filepath) # 读入图片
result = decode(image) # 解码二维码
for item in result:
    print item.type, item.data # 打印解码的数据

```

#### 测试

我们拿下面的二维码来测试一下（因为知乎会自动转换二维码，这里不得已把图片作了下分割）

![]({static}/images/v2-6c12c28182327fd821763cda91ed22a9_b.jpg)

![]({static}/images/v2-40192faa7a28708c254571598c3f9961_b.jpg)

运行上面的read\_qrcode.py，可以看到如下的结果：

```bash
QRCODE 欢迎关注“Python与数据分析”专栏

```

：）




本文已更新微信同名公众号【Python与数据分析】，欢迎关注~

![]({static}/images/v2-e9b0b9b9584ccdd3ff4c96b7ecfd8a56_r.jpg)



