Title: Windows上做Python开发太痛苦？Docker了解一下
url: windows-py-on-docker
save_as: windows-py-on-docker.html
Date: 2018-11-26 10:20
Category: Python
Authors: Zhongqiang Shen
Slug:

用Windows的朋友应该都体会过，Windows上做Python开发有多痛苦。用pip装库各种报错，然后每次都要花很多时间找解决办法，每次的心情都像这样

![]({static}/images/v2-402a08b55cd89812b83bb3848c33cbc0_b.jpg)

之前我的解决方法是在Windows上装VMWare，VMWare上运行Ubuntu，然后在Ubuntu里面做开发。但这样也不太方便，每次进入开发环境都要先启动VMWare，再启动Ubuntu，然后打开命令行窗口开始开发，而且有时候需要在宿主机和虚拟机之间来回切换，也很麻烦。

最近了解到Docker也有Windows的版本，于是就想到在windows上利用Docker运行一个Ubuntu镜像，在容器里搭建Python开发环境，这 样既解决了安装库的问题，也解决了VMWare虚拟机的不方便之处。

![]({static}/images/v2-5e97f157eb2f8660c60672b440cdd4f0_r.jpg)




关于容器的基本使用，可以参考我之前的一篇文章 [Docker初体验](https://zhuanlan.zhihu.com/p/31436920)。




需要注意的是，Windows上安装Docker对系统有以下的要求：

+ 需要支持Hyper-V的windows版本，Hyper-V目前仅在Windows 10之后的版本支持
+ BIOS里需要启用Virtualization（虚拟化）


如果你的系统满足上面的要求，接下来，我们来一步一步搭建环境。

#### 安装Docker for Windows

安装程序可以从这里下载 [Docker for Windows](http://link.zhihu.com/?target=https%3A//download.docker.com/win/stable/Docker%2520for%2520Windows%2520Installer.exe)

安装完之后，运行Docker for Windows。

Docker运行后可以在状态栏里看到有一个小鲸鱼的图标，如下所示

![]({static}/images/v2-2dc9098e780c3bb757fd5e94957768d7_b.jpg)




打开命令行窗口，运行下面的命令查看Docker版本

```bash
docker --version
```


输出


```bash
Docker version 18.09.0, build 4d60db4
```



#### 下载镜像

docker hub上提供了很多docker镜像，我们以ubuntu:18.04为基础，打造我们的python开发环境。运行

```text
docker pull ubuntu:18.04

```

下载完后，我们来查看一下本地的镜像，运行

```text
docker images

```

可以看到如下的输出

```bash
REPOSITORY                  TAG                 IMAGE ID            CREATED             SIZE
ubuntu                      18.04               93fd78260bd1        6 days ago          86.2MB

```




#### 安装常用工具和Python

我们启动一个容器，并进到容器内的bash，运行

```text
docker run -it ubuntu:18.04 bash

```




我们的这个镜像现在只是一个最基本的ubuntu的系统，里面很多工具都没有，如ping、ifconfig、wget、vim等，也没有python。接下来我们把这些一个一个都装上。

由于镜像默认用的是ubuntu官方的源，从国内连官方的源很慢，我们先把源改成163的源。修改/etc/apt/sources.list的内容为下面 的内容

```text
deb http://mirrors.163.com/ubuntu/ bionic main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ bionic-security main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ bionic-updates main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ bionic-backports main restricted universe multiverse

```

运行

```bash
apt update

```

接下来，安装ping，wget，ifconfig，vim等工具

```bash
apt install iputils-ping wget net-tools vim

```




安装python3.6

```bash
apt install python3.6
ln -s /usr/bin/python3.6 /usr/bin/python

```

安装pip

```bash
apt install python3-pip

```




#### 配置VIM

安装完工具后，我们来配置一下vim。打开~/.vimrc文件，输入vim的配置。比如我的配置是这样的

```text
set ru
syntax on
set background=dark
set sw=4
set ts=4
set tabstop=4
set shiftwidth=4
set expandtab
filetype plugin on
set autoindent
set smartindent
set number
set viminfo='10,\"100,:20,%,n~/.viminfo
function! ResCur()
    if line("'\"") <= line("$")
        normal! g`"
        return 1
    endif
endfunction

augroup resCur
    autocmd!
    autocmd BufWinEnter * call ResCur()
augroup END

highlight WhiteSpaces ctermbg=green guibg=#55aa55
match WhiteSpaces /\s\+$/

```

好了，至此，我们的开发环境配置好了。




#### 提交镜像

为方便以后的使用，我们把这个配置好的容器打成一个新的镜像。在容器中执行exit退出，我们现在来到了windows的命令行窗口。我们查看一下我们刚刚配置好的容器，运行

```bash
docker ps -a

```

输出

```text
CONTAINER ID        IMAGE                       COMMAND             CREATED             STATUS                      PORTS               NAMES
39ca895c725e        ubuntu:18.04                "bash"              3 hours ago         Exited (0) 19 seconds ago                       relaxed_wiles

```




运行下面的命令，提交更改，将容器打包成一个新的镜像

```bash
docker commit 39ca895c725e shenzhongqiang/python-dev:version1

```

我们再来查看一下本地的镜像

```bash
docker images

```

输出

```text
REPOSITORY                  TAG                 IMAGE ID            CREATED             SIZE
shenzhongqiang/python-dev   version1            fbf0ce58d00d        2 minutes ago       542MB
ubuntu                      18.04               93fd78260bd1        6 days ago          86.2MB

```

可以看到，现在我们本地有2个镜像了。下面一个是原始的docker hub上的ubuntu镜像，上面一个就是我们自己定制的镜像。

之后我们就可以基于我们定制的镜像，启动容器做开发了。启动容器很简单，只要运行

```bash
docker run -it fbf0ce58d00d bash

```

需要注意的是，容器如果被删除了，其中的更改也会丢失。要保存容器中的更改，需要像上面这样把更改commit到镜像中。




好，以上就是定制的所有步骤。这两天我逐渐把项目迁移到容器里了，在容器里开发感觉比在虚拟机里开发顺滑多了。




为方便起见，上面这个镜像放在了我的docker hub上，大家可以通过下面的命令获取

```bash
docker pull shenzhongqiang/python-dev:version1

```

如果大家有更好的Windows上配置Python开发环境的建议，也欢迎在评论里告诉我~




本文已同步更新到公众号【Python与数据分析】，欢迎关注~
