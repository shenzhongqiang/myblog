Title: Python告诉你上海有哪些高性价比的西餐厅
url: python-shanghai-best-western-restaurants.html
save_as: python-shanghai-best-western-restaurants.html
Date: 2018-08-29
Category: 数据分析
Tags: Python, 数据分析, 爬虫
Authors: Zhongqiang Shen

七夕节就要到了，我们用Python爬了下点评上所有上海的西餐厅，看看上海都有哪些高性价比的西餐厅。

爬虫的原理不多说了，很简单，按行政区爬取每个区的西餐厅，存入数据库。需要代码的同学可以在公众号【**Python与数据分析**】后台回复“西餐厅”获取代码地址。

#### 餐厅综合评分

在展现数据前，我们先介绍一下我们的餐厅综合评分。

点评上对每家餐厅的评分有口味、环境和服务三项，如下

![]({static}/images/v2-c5274378fae66e576bdce8c7187d16d5_b.jpg)

我们综合这三项算出一个评分，作为对这家餐厅的综合评分，计算公式如下

![](http://www.zhihu.com/equation?tex=%E7%BB%BC%E5%90%88%E8%AF%84%E5%88%86+%3D+3+%5Cdiv+%281%5Cdiv%E5%8F%A3%E5%91%B3%E8%AF%84%E5%88%86%2B1%5Cdiv%E7%8E%AF%E5%A2%83%E8%AF%84%E5%88%86%2B1%5Cdiv%E6%9C%8D%E5%8A%A1%E8%AF%84%E5%88%86%29) 




#### 餐厅数据分析

我们共爬取了5000多家西餐厅，西餐厅的人均消费从10元到5000+不等，下图是不同价位的餐厅数量分布情况

![]({static}/images/v2-97f7263fdec129ae4179aee8767157bd_r.jpg)

可以看到，人均消费越低的餐厅数量越多，越是贵的餐厅数量越少。




餐厅综合评分的分布情况如下

![]({static}/images/v2-362b6ec98fd0812a5a91d07514caf13a_r.jpg)

上图呈现偏态分布。放大图片可以看到，大部分餐厅的评分在7.8~8.6之间。




我们来看看土豪们都去哪些餐厅。下图是上海最贵的10家西餐厅

![]({static}/images/v2-26a689af464583bf26e806da1a054ec3_r.jpg)

每一家的人均消费都在1000以上，最贵的一家更是超过了5000，果然贫穷限制了我的想象，土豪去的餐厅我们普通工薪阶层消费不起啊~




上面的餐厅我们就过过眼瘾吧，我们来看看有哪些综合评分高，但价位又适中的餐厅。我们选取了综合评分8.8分以上，人均消费在200-300之间的餐厅，如下（排名按综合评分从高到低）

[ 双立人美食学院 ZWILLING GOURMET SCHOOL ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/98286435), 人均: 258, 综合评分: 9.30

[ Sky Restaurant & Lounge ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/67138913), 人均: 251, 综合评分: 9.20

[ TR TERRA ROSSA(中海环宇荟店) ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/103629748), 人均: 285, 综合评分: 9.20

[ esee LOUNGE & BAR ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/73553342), 人均: 291, 综合评分: 9.20

[ MOSSO音乐酒吧（live house）(长乐路店) ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/102282960), 人均: 220, 综合评分: 9.13

[ SISTERS BAR & RESTAURANT ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/4227815), 人均: 241, 综合评分: 9.10

[ DATING达庭西餐厅 ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/76854134), 人均: 202, 综合评分: 9.10

[ Crazy Oyster House ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/18982841), 人均: 281, 综合评分: 9.10

[ 碳匠音乐餐厅酒吧 ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/67556261), 人均: 275, 综合评分: 9.06

[ 泥土的味道Gout de Terroir ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/93473032), 人均: 211, 综合评分: 9.06

[ La casetta意式私家厨房(南京西路店) ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/21341829), 人均: 269, 综合评分: 9.03

[ C&R ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/97732766), 人均: 242, 综合评分: 9.03

[ JSTONE.ITALIAN KITCHEN&BAR(襄阳公园店) ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/37942497), 人均: 240, 综合评分: 9.03

[ Entrecôte法国牛扒馆 ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/96401331), 人均: 234, 综合评分: 9.03

[ Efes Turkish & Mediterranean Cuisine 艾菲斯餐厅 ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/8866486), 人均: 211, 综合评分: 9.00

[ Babbo ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/9071330), 人均: 204, 综合评分: 9.00

[ 夏朵花园 ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/1926859), 人均: 262, 综合评分: 9.00

[ 远方北纬30度餐厅Horizone Restaurant ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/95931702), 人均: 224, 综合评分: 9.00

[ Porto Matto意大利餐厅 ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/17683780), 人均: 259, 综合评分: 8.97

[ CHEF PAPA(协信星光店) ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/69448371), 人均: 211, 综合评分: 8.97

[ DIONNE红酒西餐厅(天钥桥路店) ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/21343952), 人均: 293, 综合评分: 8.96

[ Brownstone Tapas & Lounge布朗石西班牙餐厅酒吧(陆家嘴店) ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/77218611), 人均: 258, 综合评分: 8.96

[ DE CARBON BAR烤肉匠 ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/93747240), 人均: 213, 综合评分: 8.96

[ 凤凰西餐吧Phoenix Restaurant&Bar ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/18338823), 人均: 208, 综合评分: 8.96

[ Ermans Kitchen 珥玛厨房 ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/22303119), 人均: 233, 综合评分: 8.96

[ Mayita小玛雅墨西哥餐厅 ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/18021257), 人均: 217, 综合评分: 8.96

[ CommBiz康睦社 ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/94309318), 人均: 220, 综合评分: 8.96

[ 衡山99 Francis ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/72556891), 人均: 274, 综合评分: 8.95

[ 弗兰克牛排馆 Ribone steakhouse(外滩店) ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/69482454), 人均: 284, 综合评分: 8.93

[ husk restaurant ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/20877970), 人均: 255, 综合评分: 8.93

[ Brownstone Tapas & Lounge布朗石西班牙餐厅酒吧(永嘉庭店) ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/4599475), 人均: 246, 综合评分: 8.93

[ MAYA玛雅墨西哥餐厅(四方新城店) ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/2713810), 人均: 231, 综合评分: 8.93

[ 阿尔贝鲁西班牙餐厅 ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/3994102), 人均: 298, 综合评分: 8.93

[ loving Vincent-创意西餐(尚悦湾店) ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/97297788), 人均: 208, 综合评分: 8.89

[ Light & Salt Backstage 光与盐(南京东路店) ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/96027466), 人均: 292, 综合评分: 8.89

[ SILEX ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/69623000), 人均: 265, 综合评分: 8.89

[ La Cabane ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/22415791), 人均: 221, 综合评分: 8.87

[ Host Wine&Kitchen(Antoni) ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/21725401), 人均: 234, 综合评分: 8.87

[ LETS BURGER&LOBSTER(兴业太古汇店) ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/91599682), 人均: 201, 综合评分: 8.86

[ 味可思精品肉类体验馆 ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/66866544), 人均: 260, 综合评分: 8.86

[ 拉蒂娜Latina巴西烧烤音乐餐厅(铜仁路店) ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/19428889), 人均: 208, 综合评分: 8.86

[ Yasmine's 茉莉西餐厅(襄阳店) ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/27525052), 人均: 202, 综合评分: 8.83

[ 煌庭LAVIDA ](http://link.zhihu.com/?target=http%3A//www.dianping.com/shop/95914018), 人均: 206, 综合评分: 8.82




上面共43家餐厅。点开链接可以跳转到点评的餐厅主页，可以看到，点评上这几家在口味、环境、服务方面的评价都不错，性价比很高。上海性价比最高的适合约会的餐厅基本都在这里了。




明天就是七夕了，七夕节还没有安排的，妹子还没追到手的，强哥只能帮你到这儿了~

最后祝大家七夕节快乐：）

![]({static}/images/v2-07dac14a2279972e16cda140648e4cb9_r.jpg)



