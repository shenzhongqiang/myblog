Title: Github启用SSH key认证
url: connect-github-with-ssh.html
save_as: connect-github-with-ssh.html
Date: 2019-03-09
Category: github
Authors: Zhongqiang Shen

Github的认证方式有两种：HTTPS和SSH key，默认的方式是HTTPS。

以我自己的[博客项目](https://github.com/shenzhongqiang/myblog)为例，在repo里面运行

```bash
git remote show origin
```

可以看到这样的输出

```bash
* remote origin
  Fetch URL: https://github.com/shenzhongqiang/myblog.git
  Push  URL: https://github.com/shenzhongqiang/myblog.git

```

这里URL里面是个https的链接，这个表示的就是，我们用的是HTTPS的认证方式。

使用HTTPS的方式有个不方便的地方，就是每次push代码的时候都要输入用户名密码。而启用SSH key认证的方式可以省去这个麻烦。

接下来我们就来看下怎么样启用SSH key认证。

配置的过程包括这样几个步骤
* 生成密钥对
* 将公钥上传到Github
* 将本地repo的remote改成SSH

# 1. 生成密钥对
运行下面的命令生成一组密钥对
```bash
ssh-keygen -t rsa -b 4096 -C "<username@domain.com>" # <username@domain.com>替换为自己的邮箱
```
在提示`Enter passphrase`的那一步，我们直接回车。这样不输入任何passphrase，push的时候就不需要密码。
这行命令会在`~/.ssh/`下生成两个文件：`id_rsa`和`id_rsa.pub`。`id_rsa`是我们的私钥，`id_rsa.pub`是我们的公钥，后面我们会将公钥上传到Github。

接下来我们把私钥添加到`ssh-agent`。运行下面的命令确保ssh-agent在运行：
```bash
eval $(ssh-agent -s)
```
如果输出类似`Agent pid 13370`，表示ssh-agent在正常工作。

运行下面的命令将私钥添加到`ssh-agent`：
```bash
ssh-add ~/.ssh/id_rsa
```

# 2. 将公钥上传到Github
登录Github，点击右上角自己的头像，选择Settings
![]({static}/images/userbar-account-settings.png)

在新打开的页面中，选择SSH and GPG keys
![]({static}/images/settings-sidebar-ssh-keys.png)

点击New SSH key
![]({static}/images/ssh-add-ssh-key.png)

输入key的Title，并且将刚刚生成的`~/.ssh/id_rsa.pub`里的内容复制粘贴进去，保存即可。

上传公钥后，我们来测一下Github的SSH，运行下面的命令：
```bash
ssh -T git@github.com
```
如果返回
```
Hi shenzhongqiang! You've successfully authenticated, but GitHub does not provide shell access.
```
恭喜你，配置已生效。

# 3. 将本地repo的remote改成SSH
如果本地的repo原先是HTTPS的认证方式，最后我们需要将它改成SSH key的认证方式。设置方式非常简单，只需要重新设置remote的URL即可。

运行下面的命令：
```bash
git remote set-url origin git@github.com:<username>/<reponame>.git # 将username和reponame替换成自己的用户名、repo名字
```

好了，这样我们的配置就全部完成了。现在我们再push看看，是不是不需要密码了？

