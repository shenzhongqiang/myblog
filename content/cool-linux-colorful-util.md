Title: 一款超酷的Linux终端工具
url: cool-linux-colorful-util
save_as: cool-linux-colorful-util.html
Date: 2018-10-28 10:20
Category: Linux
Authors: Zhongqiang Shen

今天偶然发现一款超酷的终端工具，可以让你的终端变得像彩虹一样五彩斑斓。这款工具的名字叫做lolcat，类似于`cat`命令，但为`cat`的输出添加彩虹般的效果。封面就是这个工具的help输出。




mac上面安装这款工具非常简单，只需要运行下面的一行命令就行

```bash
brew install lolcat

```

ubuntu上面需要首先安装ruby，然后下载项目代码，安装gem

```bash
apt-get install ruby
wget https://github.com/busyloop/lolcat/archive/master.zip
unzip master.zip
cd lolcat-master/bin
gem install lolcat

```




安装完之后，我们就可以使用它了。我们来感受一下这款工具有多酷~




打印帮助，运行

```text
lolcat -h

```

输出

![]({static}/images/v2-772a2d4a17b1afb677fab3fba1b1bca5_r.jpg)




显示文件内容，运行

```bash
lolcat app.py

```

输出

![]({static}/images/v2-5d1b2b609584b3d537293e6507fcb975_r.jpg)




结合figlet输出艺术字，运行

```bash
figlet I Love You | lolcat

```

输出

![]({static}/images/v2-fc05ba6cfa61d37b726f0b7c9887e8b7_b.jpg)




画爱心，将下面的代码保存成heart.py

```python
print('\n'.join([''.join([('Love'[(x-y)%4]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))

```

运行


```text
python3 heart.py  | lolcat -p 2

```

输出


![]({static}/images/v2-21d474186e1bbf1f49662b518333acf2_r.jpg)

原本黑底白字冷冰冰的爱心也变得有温度起来了。




是不是很酷呢？是不是想赶紧在心仪的女生面前秀一下呢？




听说转发的人都找到妹子了哦

![]({static}/images/v2-12dda8504671a0d68a538551f7879026_b.jpg)



