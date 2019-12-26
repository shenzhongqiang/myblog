Title: 年终奖多发一元，少得千元？Python告诉你为什么
url: annual-bonus-tax.html
save_as: annual-bonus-tax.html
Date: 2019-01-18
Category: Python
Tags: Python
Authors: Zhongqiang Shen

年终奖多发一元，到手却会少一千元，甚至更多。听到这个消息的时候，大家是不是和我一样，觉得很难过？

![]({static}/images/v2-93705d574116cb79418b2d01462f8b88_b.jpg)

上了这么多年班，我也是最近才搞清楚年终奖的税是怎么算的。年终奖的税和工资税的最大区别就是，年终奖**没有阶梯税率，没有阶梯税率，没有阶梯税率**，重要的事情说三遍。

具体怎么算，我们来看下面的公式

![](https://www.zhihu.com/equation?tex=%E5%B9%B4%E7%BB%88%E5%A5%96%E7%A8%8E+%3D+%E5%B9%B4%E7%BB%88%E5%A5%96+%5Ctimes+%E7%A8%8E%E7%8E%87+-+%E9%80%9F%E7%AE%97%E6%89%A3%E9%99%A4%E6%95%B0) 

税率和速算扣除数按照税率表，最新的税率表如下

![]({static}/images/v2-7aec470a0d883849088aff69bcb8f971_r.jpg)

我们假设一个人的年终奖是30000元，因为没超过36000元，查上表得到税率3%，速算扣除数是0，因此他要交的税是![](https://www.zhihu.com/equation?tex=30000+%5Ctimes+3%5C%25+-+0+%3D+900%E5%85%83) 。

如果一个人的年终奖是120000元，因为在36000元~144000元的区间内，查上表得到税率10%，速算扣除数210，所以他要交的税是 ![](https://www.zhihu.com/equation?tex=120000+%5Ctimes+10%5C%25+-+210+%3D+11790%E5%85%83) 。

基于年终奖税的计算方式，我们用Python实现了一个算税的函数。代码如下

```python
import bisect
import numpy as np
import matplotlib.pyplot as plt 

def bonus_tax(bonus):
    ranges = [0, 36000, 144000, 300000, 420000, 660000, 960000]
    deducts = [0, 210, 1410, 2660, 4410, 7160, 15160]
    rate = [0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]

    i = bisect.bisect_left(ranges, bonus)
    tax = bonus * rate[i-1] - deducts[i-1]
    return tax 

```

上面的bonus\_tax函数就是算税的函数，它接受一个参数bonus，就是我们的年终奖。

我们用这个函数来算一下，从1000元到1000000元区间内所有年终奖的税各是多少。具体代码如下

```python
if __name__ == "__main__":
    bonuses = range(10000, 1000000, 1)
    taxes = []
    net_incomes = []
    for bonus in bonuses:
        tax = bonus_tax(bonus)
        taxes.append(tax)
        net_incomes.append(bonus-tax)

    plt.plot(bonuses, net_incomes)
    plt.show()

```

这段程序的末尾会将税后年终奖和税前年终奖的关系制作成一张折线图，展现出来，如下

![]({static}/images/v2-6a5dc17cda5d9a8c572b30b2beacd7d8_r.jpg)

横轴是税前的年终奖，纵轴是税后拿到手的收入。可以看到上图中税后到手的收入和税前年终奖并不是呈现单调递增的关系，在几个节点上会出现突然的下跌，也就是说税前年终奖虽然增加了，但税后到手的收入却减少了。

这是为什么呢？

我们注意到这些突然的下跌都是出现在跨税档的边界上。比如36000元的年终奖，需要交的税是 ![](https://www.zhihu.com/equation?tex=36000+%5Ctimes+3%5C%25+-+0+%3D+1080%E5%85%83) ，但36001元的年终奖，就需要交 ![](https://www.zhihu.com/equation?tex=36001+%5Ctimes+10%5C%25+-+210+%3D+3390%E5%85%83) 的税，年终奖增加一元，收入反而减少了。同样的问题也出现在144000元、300000元、420000元、660000元、960000元这些年终奖上。在这些跨税档的边界上，年终奖虽然增加了，但因为跨了税档，税率提高了，导致税后所得反而减少了。

出现这个问题的根本原因，还是在于年终奖的计税存在一个漏洞。年终奖计税的税率是基于工资税的税率表，工资税的税率表上收入额这一栏是月收入，而上面的表格里的收入额是年收入，收入额乘以了12，但速算扣除数没有，这就导致跨税档的时候会出现收入突然下跌。

如果我们把上面表格中的速算扣除数都乘以12，再画一下税后年终奖和税前年终奖的关系图，可以得到下面的图

![]({static}/images/v2-15460c017b74acf4ac7d9fff7e35792b_r.jpg)

这张图就正常多了，图上没有突然下跌的断层，税后年终奖和税前年终奖呈现单调递增的关系。

看到这里，大家是不是理解了年终奖的计税方式了呢？祝大家都能避开跨税档的陷阱~

完整代码已上传网盘，公众号【Python与数据分析】后台回复“**年终奖**”可获取地址。

