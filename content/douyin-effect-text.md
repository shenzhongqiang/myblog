Title: Python实现抖音体
url: douyin-effect-text
save_as: douyin-effect-text.html
Date: 2018-06-11
Category: 图像处理
Tags: Python, 图像处理
Authors: Zhongqiang Shen

周末在家沉迷抖音。看完抖音，索性用Python写了个程序实现抖音效果的字体。




程序的名字就叫***douyinti***，代码已发布到PYPI，直接运行下面的命令即可安装

```text
pip3 install douyinti

```

安装完后，命令行可以直接运行douyinti这个命令。

```bash
$ douyinti --help
usage: douyinti [-h] [--text TEXT] [--out OUT]

optional arguments:
  -h, --help   show this help message and exit
  --text TEXT  text to add effect
  --out OUT    path of output image

```




有了***douyinti***这个命令后，我们就可以生成我们想要的抖音体文字了（中英文都支持哦）

```text
douyinti --text 带我飞 --out fly.jpg

```

![]({static}/images/v2-4af0e7e34f8cff3a54972f372d84bb98_b.jpg)




```text
douyinti --text "Let's rock" --out rock.jpg

```

![]({static}/images/v2-f6b1b8bd663971f1c6367025f1ed0ec3_r.jpg)




是不是很酷~

程序的原理也很简单，就是基于原图生成两张图片，一张红色，一张绿色，略微错开后，叠加在一起，就有了抖音的效果。

对源码感兴趣的同学可以参见github，源码已上传

[](http://link.zhihu.com/?target=https%3A//github.com/pythonml/douyinti)




如果觉得有趣，欢迎点赞~



