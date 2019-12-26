Title: 60行代码爬取知乎神回复
url: crawler-zhihu-funny-answers.html
save_as: crawler-zhihu-funny-answers.html
Date: 2018-11-05 10:20
Category: 数据分析
Tags: Python, 爬虫, 数据分析
Authors: Zhongqiang Shen

之前的一篇文章 [爬虫爬了下知乎上的神回复，已笑趴～](https://zhuanlan.zhihu.com/p/46132179) 在公众号发布后，引发了大家热烈的反响。很多朋友觉得很神奇，在后台问强哥是怎么做到的，有的朋友还表示不太相信。其实爬取知乎神回复很简单，这篇文章 我们就来揭晓一下背后的原理。




知乎神回复都有些什么特点呢？我们先来观察一下。

![]({static}/images/v2-57f6debdb9cf67c21ef0b544f4d8373d_r.jpg)




![]({static}/images/v2-5b2beaeaeed1d6141e6b9fceb69f8b6b_r.jpg)

大家看出什么规律了么？短小精辟有没有？赞同很多有没有？所以爬取知乎神回复我们只要爬取那些赞同多又字数少的回答就可以。 简单的两个步骤就能实现，第一步爬取知乎回答，第二部筛选回答。是不是很easy？




#### 爬取知乎回答

第一步我们爬取知乎上的回答。知乎上的回答太多了，一下子爬取所有的回答会很费时，我们可以选定几个话题，爬取这几个话题里 的内容。

下面的函数用于爬取某一个指定话题的内容

```python
def get_answers_by_page(topic_id, page_no):
    offset = page_no * 10
    url = <topic_url> # topic_url是这个话题对应的url
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    }
    r = requests.get(url, verify=False, headers=headers)
    content = r.content.decode("utf-8")
    data = json.loads(content)
    is_end = data["paging"]["is_end"]
    items = data["data"]
    client = pymongo.MongoClient()
    db = client["zhihu"]
    if len(items) > 0:
        db.answers.insert_many(items)
        db.saved_topics.insert({"topic_id": topic_id, "page_no": page_no})
    return is_end

```

get\_answers\_by\_page函数有两个参数，第一个参数是话题的id，第二个参数表示爬的是第几页的内容。

爬下来的内容当中有几个需要注意的字段，下图中用黄框高亮出来了

![]({static}/images/v2-45fd9f3c05a0ecd3544969c6068aa4f7_r.jpg)

这几个字段的含义如下：

+ question.title - 问题的标题
+ content - 回答的内容
+ voteup_count - 赞同的数量


这些字段在下一步筛选回答的时候会用到。




#### 筛选回答

爬完数据后，我们来筛选一下结果。

我们用MongoDB中的聚合管道对回答做筛选（关于MongoDB的聚合管道的用法可以参考[Aggregation Pipeline Quick Reference](http://link.zhihu.com/?target=https%3A//docs.mongodb.com/manual/meta/aggregation-quick-reference/)），代码如下

```python
client = pymongo.MongoClient()
db = client["zhihu"]
items = db.answers.aggregate([
    {"$match": {"target.type": "answer"}},
    {"$match": {"target.voteup_count": {"$gte": 1000}}},
    {"$addFields": {"answer_len": {"$strLenCP": "$target.content"}}},
    {"$match": {"answer_len": {"$lte": 50}}},
])

```

上面的代码会筛选所有赞同大于1000、字数小于50的回答，筛选出来的结果就是短小精辟的神回复。

以上是核心代码，完整代码已上传github，大家可以在【Python与数据分析】公众号后台回复“**知乎神回复**”获取地址。




#### 知乎神回复

代码写完了，我们来运行下看看。恰好昨天是程序员节，我们就来筛选一下和程序员有关的神回复。结果如下，一共75条搞笑段子。



1

作者: 夏梓耀

链接: [码农们最常说的「谎言」有哪些？](https://www.zhihu.com/question/47606748/answer/106901253)

来源: 知乎

> Q: 码农们最常说的「谎言」有哪些？
A: //TODO

2

作者: 匿名用户

链接: [在 GitHub 上保持 365 天全绿是怎样一种体验？](https://www.zhihu.com/question/34043434/answer/57826281)

来源: 知乎

> Q: 在 GitHub 上保持 365 天全绿是怎样一种体验？
A: 曾经保持了200多天全绿，但是冷落了女朋友，一直绿到现在。

3

作者: 叛逆者

链接: [如何反驳「程序员离开电脑就是废物」这个观点？](https://www.zhihu.com/question/48894278/answer/113185239)

来源: 知乎

> Q: 如何反驳「程序员离开电脑就是废物」这个观点？
A: 不不不，很多程序员在电脑前也是废物。

4

作者: xlzd

链接: [假如有一天所有的人都使用计算机语言说话，会是怎样的场景？](https://www.zhihu.com/question/38748367/answer/148126016)

来源: 知乎

> Q: 假如有一天所有的人都使用计算机语言说话，会是怎样的场景？
A: hello, world.烫烫烫烫烫烫烫�d}��R�0:�v�?.

5

作者: 知乎用户

链接: [突然想开一家程序员主题的餐馆，名字就叫程序员的菜，菜名就叫各种语言中的关键字，各位指点一哈，有前途没？](https://www.zhihu.com/question/48690700/answer/112221009)

来源: 知乎

> Q: 突然想开一家程序员主题的餐馆，名字就叫程序员的菜，菜名就叫各种语言中的关键字，各位指点一哈，有前途没？
A: 进门一个大大的 hello world 招牌菜叫“红烧产品经理” 一定会爆满的

7

作者: 匿名用户

链接: [编程最基本的术语 “bug” 该怎么翻译？](https://www.zhihu.com/question/59445070/answer/345045044)

来源: 知乎

> Q: 编程最基本的术语 “bug” 该怎么翻译？
A: 幺蛾子，你的程序又出幺蛾子了。

8

作者: neksusk

链接: [编程的乐趣是什么？](https://www.zhihu.com/question/20029839/answer/13732329)

来源: 知乎

> Q: 编程的乐趣是什么？
A: 人的成就感来源于两样东西，创造和毁灭。

9

作者: 麦克灵伟

链接: [如何反驳「程序员离开电脑就是废物」这个观点？](https://www.zhihu.com/question/48894278/answer/113193764)

来源: 知乎

> Q: 如何反驳「程序员离开电脑就是废物」这个观点？
A: 老实说 跟这种女人都能聊下去 你是不是想上她？

10

作者: Amb BAI

链接: [作为程序员，你在编程时吃了哪些数学的亏？](https://www.zhihu.com/question/28056906/answer/39217410)

来源: 知乎

> Q: 作为程序员，你在编程时吃了哪些数学的亏？
A: 看论文时候一个"显然"推了我一下午

11

作者: 知乎用户

链接: [土豪程序员的设备都有啥？](https://www.zhihu.com/question/26089279/answer/32091743)

来源: 知乎

> Q: 土豪程序员的设备都有啥？
A: 女朋友。。。

12

作者: 兔二

链接: [祈求代码不出 bug 该拜哪个神仙？](https://www.zhihu.com/question/30313169/answer/47580934)

来源: 知乎

> Q: 祈求代码不出 bug 该拜哪个神仙？
A: 拜雍正，专治八阿哥。

13

作者: 知乎用户

链接: [考上好大学学 IT 是不是当今中国穷人家孩子晋级中产唯一的出路？](https://www.zhihu.com/question/37989425/answer/74424369)

来源: 知乎

> Q: 考上好大学学 IT 是不是当今中国穷人家孩子晋级中产唯一的出路？
A: 对，就4条路 写代码 搞金融 在代码圈搞金融 在金融圈写代码

14

作者: Cascade

链接: [为什么程序员无论到哪儿都喜欢背电脑包，哪怕里面没有装电脑？](https://www.zhihu.com/question/21400402/answer/18111520)

来源: 知乎

> Q: 为什么程序员无论到哪儿都喜欢背电脑包，哪怕里面没有装电脑？
A: 因为他们没有别的包。

15

作者: SErHo

链接: [「Talk is cheap. Show me the code」怎么翻译比较好？](https://www.zhihu.com/question/23090743/answer/23581453)

来源: 知乎

> Q: 「Talk is cheap. Show me the code」怎么翻译比较好？
A: 屁话少说，放码过来。

16

作者: An0th3r

链接: [为什么程序员的女朋友或老婆颜值普遍要高于男方很多？还是说程序员已经算是婚恋市场的优质股了？](https://www.zhihu.com/question/63765274/answer/214281927)

来源: 知乎

> Q: 为什么程序员的女朋友或老婆颜值普遍要高于男方很多？还是说程序员已经算是婚恋市场的优质股了？
A: 程序员女朋友颜值高，我是服的，因为随便问十个程序员他的女朋友是谁，有九个回答是新垣结衣

17

作者: fullsail

链接: [为什么一部分人宁可买几个机械键盘换着用，也不愿意给自己敷一下面膜？](https://www.zhihu.com/question/266816276/answer/320996324)

来源: 知乎

> Q: 为什么一部分人宁可买几个机械键盘换着用，也不愿意给自己敷一下面膜？
A: 老子不靠脸吃饭。 老子的辛辛苦苦挣来的钞票。老子想怎么花就怎么花。

18

作者: 苏予

链接: [程序员夫妻结婚戒指刻什么字好？](https://www.zhihu.com/question/23396163/answer/24457537)

来源: 知乎

> Q: 程序员夫妻结婚戒指刻什么字好？
A: 0 error 0 warning

19

作者: 苏莉安

链接: [IT 工程师被叫「码农」时是否会不舒服？](https://www.zhihu.com/question/25153900/answer/30206460)

来源: 知乎

> Q: IT 工程师被叫「码农」时是否会不舒服？
A: 我们好歹还是人，产品和设计已经是狗了……

20

作者: 白如冰

链接: [为什么一个销售男（30岁）会约我一个男程序员（24岁）去小区附近的星巴克？](https://www.zhihu.com/question/23386954/answer/24420889)

来源: 知乎

> Q: 为什么一个销售男（30岁）会约我一个男程序员（24岁）去小区附近的星巴克？
A: 根据哥多年的经验，他应该是有巨牛逼的idea然后只差程序员去实现了

21

作者: 随喜

链接: [怎么找到喜欢程序员的妹子做女友？](https://www.zhihu.com/question/66249920/answer/300623623)

来源: 知乎

> Q: 怎么找到喜欢程序员的妹子做女友？
A: 看缘分，知乎上这么多用户，你关注到我就是缘分。

22

作者: 知乎用户

链接: [程序员女朋友如何给程序员男朋友过生日？](https://www.zhihu.com/question/19921151/answer/13550240)

来源: 知乎

> Q: 程序员女朋友如何给程序员男朋友过生日？
A: 告诉他，接口已经准备好了。

23

作者: 程序员大叔

链接: [作为程序员，你是如何在工作以后找到女朋友的？](https://www.zhihu.com/question/38200429/answer/75361639)

来源: 知乎

> Q: 作为程序员，你是如何在工作以后找到女朋友的？
A: 题主作了这么久的程序员，还喜欢女孩子已经难能可贵了。

24

作者: 某个小超

链接: [程序员转行烧烤需要做哪些准备，有哪些优势和劣势？](https://www.zhihu.com/question/21333711/answer/17953891)

来源: 知乎

> Q: 程序员转行烧烤需要做哪些准备，有哪些优势和劣势？
A: 你看，你连自己做烧烤都不知道优势劣势在哪里，所以，你还是需要一名产品经理。

25

作者: Jack Ma

链接: [哪些话可以惹火程序员？](https://www.zhihu.com/question/37017953/answer/70032115)

来源: 知乎

> Q: 哪些话可以惹火程序员？
A: 路过他电脑前时说一句，呦，又在写bug呢!

26

作者: 姚冬

链接: [我的一位老师说，Java 适用于大型软件而 C# 适用中小型软件。这是真的么？](https://www.zhihu.com/question/27511902/answer/36931243)

来源: 知乎

> Q: 我的一位老师说，Java 适用于大型软件而 C# 适用中小型软件。这是真的么？
A: Java有项天赋，就是能把中小型软件写成大型的。
27

作者: 大猫 链接: [为什么 2014 年程序员薪资那么高？](https://www.zhihu.com/question/26025387/answer/31873025) 来源: 知乎

> Q: 为什么 2014 年程序员薪资那么高？ A: 时薪又不高

28

作者: 廖雪峰

链接: [是不是大部分程序员都在抱怨工资低？](https://www.zhihu.com/question/20082607/answer/356841938)

来源: 知乎

> Q: 是不是大部分程序员都在抱怨工资低？
A: 谁、谁在抱怨工资高？

29

作者: ze ran

链接: [单身程序狗解决了一个技术难题后没有妹子可以炫耀或夸一下自己怎么办？](https://www.zhihu.com/question/28987904/answer/42805814)

来源: 知乎

> Q: 单身程序狗解决了一个技术难题后没有妹子可以炫耀或夸一下自己怎么办？
A: 现在你明白了吧，为什么那么多程序员要写技术博客。

30

作者: 知乎用户

链接: [中国程序员是否偏爱「冲锋衣+牛仔裤+运动鞋」的衣着？如果是，为何会形成这样的潮流？](https://www.zhihu.com/question/23344932/answer/24308022)

来源: 知乎

> Q: 中国程序员是否偏爱「冲锋衣+牛仔裤+运动鞋」的衣着？如果是，为何会形成这样的潮流？
A: 穿那么好看给程序看吗？

31

作者: 匿名用户

链接: [作为 IT 从业人员，你觉得有什么工具大大提高了你的工作效率？](https://www.zhihu.com/question/24429345/answer/27761796)

来源: 知乎

> Q: 作为 IT 从业人员，你觉得有什么工具大大提高了你的工作效率？
A: 单身

32

作者: 温酒

链接: [为什么我认为程序员似乎大多不善言辞？](https://www.zhihu.com/question/267094042/answer/319107651)

来源: 知乎

> Q: 为什么我认为程序员似乎大多不善言辞？
A: 你就当是我们情商低就好了， 这样你开心， 我们也开心。

33

作者: vczh

链接: [在中国，年龄最大的程序员不过40岁左右，请问中国的程序员未来还可以做什么？](https://www.zhihu.com/question/19920560/answer/363981684)

来源: 知乎

> Q: 在中国，年龄最大的程序员不过40岁左右，请问中国的程序员未来还可以做什么？
A: 这跟为什么90后没人活过30岁是同一个原理

34

作者: ze ran

链接: [如何回复程序员发来的短信：「Hello world」？](https://www.zhihu.com/question/25655170/answer/31328622)

来源: 知乎

> Q: 如何回复程序员发来的短信：「Hello world」？
A: hello nerd.

35

作者: 李继刚

链接: [怎么看出 IT 男喜欢一个女生？](https://www.zhihu.com/question/19892427/answer/13286326)

来源: 知乎

> Q: 怎么看出 IT 男喜欢一个女生？
A: 当他拼着自己早已养成的寡言少语的习惯去死命的跟你套近乎的时候

36

作者: 叛逆者

链接: [为什么程序员不应该会修电脑？](https://www.zhihu.com/question/20662631/answer/43395016)

来源: 知乎

> Q: 为什么程序员不应该会修电脑？
A: 范冰冰需要会修电视机吗？

37

作者: 匿名用户

链接: [同事说自己 C++ 水平全中国第一，怎么让他意识到自己没那么厉害？](https://www.zhihu.com/question/42115074/answer/93621264)

来源: 知乎

> Q: 同事说自己 C++ 水平全中国第一，怎么让他意识到自己没那么厉害？
A: 实不相瞒，我也不是装逼：我的 C++ 水平全国第 0。

38

作者: 刘小脑袋

链接: [为什么 iPhone 删软件时，所有图标都要抖？](https://www.zhihu.com/question/26470075/answer/32898565)

来源: 知乎

> Q: 为什么 iPhone 删软件时，所有图标都要抖？
A: 第三方软件是吓得，系统自带软件是嘚瑟

39

作者: AcFun弹幕视频网

链接: [左轮手枪装有一颗子弹，对着自己头开一枪奖励10万元，两枪1亿，三枪2亿，四枪4亿，5枪16亿，值得吗？](https://www.zhihu.com/question/67576286/answer/254405561)

来源: 知乎

> Q: 左轮手枪装有一颗子弹，对着自己头开一枪奖励10万元，两枪1亿，三枪2亿，四枪4亿，5枪16亿，值得吗？
A: 只要不打要害，我告诉你，我能打到我们A站上市！！！！

40

作者: 张小贱

链接: [iPhone 处理器的性能按照现在每年翻一倍的节奏，是不是很快就能赶上甚至超过台式电脑的处理器？](https://www.zhihu.com/question/25145861/answer/30202727)

来源: 知乎

> Q: iPhone 处理器的性能按照现在每年翻一倍的节奏，是不是很快就能赶上甚至超过台式电脑的处理器？
A: 小时候我总觉得过两年我就能和大我两岁的哥哥一样大了。

41

作者: 解磊

链接: [知乎给你带来的最小限度的好处是什么？](https://www.zhihu.com/question/19631509/answer/25393717)

来源: 知乎

> Q: 知乎给你带来的最小限度的好处是什么？
A: 消磨时间还不觉得罪恶。

42

作者: Derek Chan

链接: [有哪些反人类的科技发明或设计？](https://www.zhihu.com/question/22331607/answer/24951350)

来源: 知乎

> Q: 有哪些反人类的科技发明或设计？
A: 电脑连不上网，诊断以后它提示我要联网解决

43

作者: 汪惟

链接: [为什么设计师不愿意被称为美工？](https://www.zhihu.com/question/21584213/answer/18861007)

来源: 知乎

> Q: 为什么设计师不愿意被称为美工？
A: 只要工资开的高，叫我阿姨都行。

44

作者: Mr.Robot

链接: [为什么有人认为网易云音乐是业界良心？](https://www.zhihu.com/question/24495947/answer/28076585)

来源: 知乎

> Q: 为什么有人认为网易云音乐是业界良心？
A: 有一天突然给我推送一条消息说我要的歌词找到了

45

作者: 知乎用户

链接: [为什么没有出现无人机自毁式攻击武器呢？恐怖分子用过吗？](https://www.zhihu.com/question/33279324/answer/56191019)

来源: 知乎

> Q: 为什么没有出现无人机自毁式攻击武器呢？恐怖分子用过吗？
A: 你是说导弹么？

46

作者: 安雅

链接: [既然思想是我的，那么为什么有时候我控制不了我的负面情绪？](https://www.zhihu.com/question/20051430/answer/23065827)

来源: 知乎

> Q: 既然思想是我的，那么为什么有时候我控制不了我的负面情绪？
A: 操作系统不会允许用户访问、修改及删除核心系统文件，因为这会损坏系统，导致运行异常。

47

作者: isotone

链接: [鲁迅虽然很牛，但在这世界十大文豪里是不是凑数的？](https://www.zhihu.com/question/40942442/answer/89479641)

来源: 知乎

> Q: 鲁迅虽然很牛，但在这世界十大文豪里是不是凑数的？
A: 为什么文豪要为文盲排的榜买单？

48

作者: 念缺一Miracle

链接: [人类的哪些科技已经接近瓶颈，很久没有重大突破了？](https://www.zhihu.com/question/67992675/answer/259398868)

来源: 知乎

> Q: 人类的哪些科技已经接近瓶颈，很久没有重大突破了？
A: 烧开水

49

作者: vczh

链接: [如何看待某些人下载软件喜欢到官网的偏好？](https://www.zhihu.com/question/30985440/answer/50188231)

来源: 知乎

> Q: 如何看待某些人下载软件喜欢到官网的偏好？
A: 同学你没中过百度全家桶吧？

50

作者: 知乎用户

链接: [为什么很多人买笔记本打游戏，而不用性能更好的台式机？](https://www.zhihu.com/question/29717932/answer/45915429)

来源: 知乎

> Q: 为什么很多人买笔记本打游戏，而不用性能更好的台式机？
A: 因为买不起房子。。。

51

作者: DillyLiu

链接: [第一次听好耳机对你带来的震撼有多大？](https://www.zhihu.com/question/27755657/answer/37953999)

来源: 知乎

> Q: 第一次听好耳机对你带来的震撼有多大？
A: 第一次听好耳机不会给人多大震撼，但是当换回普通耳机的时候，震撼就来了

52

作者: 林灿斌

链接: [Chrome 真的很费电吗？](https://www.zhihu.com/question/24503682/answer/37979707)

来源: 知乎

> Q: Chrome 真的很费电吗？
A: 不费电，我现在就在用Chrome，用到现在这么久，笔记本电量还有50%，我估讠

53

作者: 王文瀚

链接: [MacBook 上安装 Windows 后的使用体验如何？](https://www.zhihu.com/question/24884517/answer/29320483)

来源: 知乎

> Q: MacBook 上安装 Windows 后的使用体验如何？
A: 像突然间有了软肋，并且还失去了铠甲。

54

作者: suchsu

链接: [家里所有有关产品都用苹果产品是一种什么体验？](https://www.zhihu.com/question/27573401/answer/37173454)

来源: 知乎

> Q: 家里所有有关产品都用苹果产品是一种什么体验？
A: 来个电话全家都响了起来

55

作者: 蛋黄酱摧毁停车场

链接: [你为什么不买 iPhone X？](https://www.zhihu.com/question/67264455/answer/251124814)

来源: 知乎

> Q: 你为什么不买 iPhone X？
A: 日益增长的美好生活需要和贫穷的现实之间的矛盾

56

作者: 张鑫

链接: [为什么有人愿意花几千元买 iPhone ，却不愿意花几十元买正版 iPhone 软件和游戏？](https://www.zhihu.com/question/21971889/answer/19895502)

来源: 知乎

> Q: 为什么有人愿意花几千元买 iPhone ，却不愿意花几十元买正版 iPhone 软件和游戏？
A: 因为他们下载不到iphone

57

作者: 苦瓜

链接: [有什么 App 取的名字特别惊艳？](https://www.zhihu.com/question/29739045/answer/46795719)

来源: 知乎

> Q: 有什么 App 取的名字特别惊艳？
A: 水表助手…是查快递的…

58

作者: 王斯塔

链接: [你为什么要买移动硬盘？](https://www.zhihu.com/question/20418839/answer/88198576)

来源: 知乎

> Q: 你为什么要买移动硬盘？
A: 条件好了也要给自己的女人们住舒适点啊

59

作者: 叛逆者

链接: [如何用 iPad 遥控 PC 关机？](https://www.zhihu.com/question/35339495/answer/62324107)

来源: 知乎

> Q: 如何用 iPad 遥控 PC 关机？
A: 瞄准pc电源键扔过去

60

作者: 知乎用户

链接: [如何评价 2016 年 9 月 7 日的苹果发布会？](https://www.zhihu.com/question/50391841/answer/120978712)

来源: 知乎

> Q: 如何评价 2016 年 9 月 7 日的苹果发布会？
A: 为了新MacBook Pro，半年看了三场发布会……

61

作者: 陈肖恩

链接: [如何评价 Internet Explorer？](https://www.zhihu.com/question/21416623/answer/18162511)

来源: 知乎

> Q: 如何评价 Internet Explorer？
A: 下载其他浏览器的浏览器 -----一年后----- IE8以下好烂，做前端想哭的节奏。

62

作者: 知乎用户

链接: [爸妈让我攒钱买房，我却想买苹果电脑怎么办？](https://www.zhihu.com/question/31338218/answer/51509136)

来源: 知乎

> Q: 爸妈让我攒钱买房，我却想买苹果电脑怎么办？
A: 你要真能3年攒50万的房子,差这1万7买个电脑么,大哥?

63

作者: 温馨

链接: [有哪些垃圾手机软件？](https://www.zhihu.com/question/21083505/answer/27100834)

来源: 知乎

> Q: 有哪些垃圾手机软件？
A: 短信拦截软件！ 拦截后告诉你它拦截了一条短信。 我相信99%的人会再去点进去看一下被拦截的短信！

64

作者: Simon阿文

链接: [一个完整的 PPT 做下来，最让你头疼的是什么？](https://www.zhihu.com/question/27804105/answer/38329967)

来源: 知乎

> Q: 一个完整的 PPT 做下来，最让你头疼的是什么？
A: 怎样向领导隐藏自己的实力。

65

作者: 孙经东

链接: [什么是 Vim 可以做而 Emacs 做不到的？](https://www.zhihu.com/question/22093333/answer/20296027)

来源: 知乎

> Q: 什么是 Vim 可以做而 Emacs 做不到的？
A: 帮助乌干达的可怜儿童……

66

作者: 王二小

链接: [苹果用户为什么选择苹果？](https://www.zhihu.com/question/31839209/answer/53522654)

来源: 知乎

> Q: 苹果用户为什么选择苹果？
A: 因为不用苹果的用户不是苹果用户。

67

作者: 唐缺

链接: [计算机世界里有哪些经典谣言？](https://www.zhihu.com/question/22933777/answer/23172556)

来源: 知乎

> Q: 计算机世界里有哪些经典谣言？
A: windows正在联机寻找解决方案。

68

作者: 羽扇纶巾2010

链接: [有线鼠标会被无线鼠标取代吗？](https://www.zhihu.com/question/20977602/answer/17242303)

来源: 知乎

> Q: 有线鼠标会被无线鼠标取代吗？
A: 我觉得在网吧有线鼠标就不会被取代

69

作者: 北上

链接: [计算机世界里有哪些经典谣言？](https://www.zhihu.com/question/22933777/answer/23113353)

来源: 知乎

> Q: 计算机世界里有哪些经典谣言？
A: 我已阅读并同意该条款

70

作者: 有时右逝

链接: [魔兽圈中有哪些搞笑的事件？](https://www.zhihu.com/question/23524157/answer/90207540)

来源: 知乎

> Q: 魔兽圈中有哪些搞笑的事件？
A: 你好，我觉得我就是魔兽世界里最大的笑话……

71

作者: CCafe

链接: [计算机系的学生都有哪些口头禅？](https://www.zhihu.com/question/52551550/answer/131149935)

来源: 知乎

> Q: 计算机系的学生都有哪些口头禅？
A: 我电脑上运行的好好的啊⋯⋯

72

作者: 贝尔

链接: [在飞机上遇到了马云该怎么聊天？](https://www.zhihu.com/question/38482487/answer/76714182)

来源: 知乎

> Q: 在飞机上遇到了马云该怎么聊天？
A: Hello Jack, my name is Jackson.

73

作者: 匿名用户

链接: [如何理解马云说八年后房如葱？](https://www.zhihu.com/question/264163101/answer/279437857)

来源: 知乎

> Q: 如何理解马云说八年后房如葱？
A: 赶紧买葱啊，葱要涨价了！！！

74

作者: Colliot

链接: [如何理解马云说的「把地主杀了，不等于你能富起来」这句话？](https://www.zhihu.com/question/26759276/answer/156706164)

来源: 知乎

> Q: 如何理解马云说的「把地主杀了，不等于你能富起来」这句话？
A: 他的意思是「别杀我」

75

作者: justjavac

链接: [如何看待百度在魏则西事件过去之后又悄悄的把承诺整改的广告提示颜色调淡了？](https://www.zhihu.com/question/48491508/answer/111391437)

来源: 知乎

> Q: 如何看待百度在魏则西事件过去之后又悄悄的把承诺整改的广告提示颜色调淡了？
A: 请大家不要黑百度，我是做前端开发的，这是时间久了，网页CSS掉色了


