Title: 破解点评网的反爬
url: dianping-anti-crawler.html
save_as: dianping-anti-crawler.html
Date: 2018-11-24 10:20
Category: 爬虫
Tags: Python, 爬虫
Authors: Zhongqiang Shen

点评网的反爬设置在我们爬取点评网页的时候给我们造成了不小的障碍。在网页上我们看到的是这样的

![]({static}/images/v2-713839a83e9e16e65dc9f76feb23ab90_r.jpg)

网页上可以看到这家餐厅有1405条评论，人均387。但在分析页面源码的时候，我们却看不到网页上的数字，看到是这样的代码

![]({static}/images/v2-4fec3b668135f3e7d3c9418d5baed6db_b.jpg)

点评网对数字做了处理，一些数字的信息像评论条数、人均、评分等都做了反爬保护。上面的网页中评论条数是1405条，但在页面源 码中，除了第一个数字1以外，后面的数字我们看不到，都是一些像随机编码一样的css class。




如果我们仔细分析这个css class，其实是不难发现背后的原理的。

通过开发者工具，我们找到这个css的定义，可以看到是下面这样的

![]({static}/images/v2-99963314a3cb5aec9f80ecb9adb22311_r.jpg)

background-image属性里面是一个url，我们在浏览器里打开它，看到它的内容是

![]({static}/images/v2-c1080556faba624a1d434bbdbe84e1e6_b.jpg)

lc-mY1i 这个css class里面是一个background属性，定义了背景图片偏移的位置。

所以点评网上显示数字的原理就是通过设置不同的偏移位置，显示背景图片相应位置上的数字。我们可以想象背景图片的前面有一个 窗口，窗口的大小刚好够显示一个数字。窗口是固定不动的，背景图片在后面移动，移动到不同的位置就能显示这个位置上的数字。

进一步分析背景图片，我们可以发现，这是一个SVG图片，图片中的数字可以在svg的源码中看到，如下

![]({static}/images/v2-677f504d989747ef91fb5bc9de80a136_b.jpg)




理解了原理后，我们用代码来实现一下解析的过程。

首先我们从点评的网页上找出css文件的url，代码如下

```python
def get_css():
    url = "http://www.dianping.com/shanghai/ch10"
    r = requests.get(url, headers=headers)
    content = r.content.decode("utf-8")
    matched = re.search(r'href="([^"]+svgtextcss[^"]+)"', content, re.M)
    if not matched:
        raise Exception("cannot find svgtextcss file")
    css_url = matched.group(1)
    css_url = fix_url(css_url)
    return css_url

```




随后我们从css里找到背景图片的路径，并获取SVG图片中的每个数字

```python
def get_svg(css_url):
    r = requests.get(css_url, headers=headers)
    content = r.content.decode("utf-8")
    matched = re.search(r'span\[class\^="lc\-"\].*?background\-image: url\((.*?)\);', content)
    if not matched:
        raise Exception("cannot find svg file")
    svg_url = matched.group(1)
    svg_url = fix_url(svg_url)
    r = requests.get(svg_url, headers=headers)
    content = r.content.decode("utf-8")
    matched = re.search(r'class="textStyle">(\d+)</text>', content)
    if not matched:
        raise Exception("cannot find digits")
    digits = list(matched.group(1))
    return digits

```

这个函数返回一个数组，数组的内容是SVG图片中的所有数字。




对于点评网页中的用css class表示的数字，我们来解析一下css class和数字之间的对应关系

```python
def get_class_offset(css_url):
    r = requests.get(css_url, headers=headers)
    content = r.content.decode("utf-8")
    matched = re.findall(r'(\.[a-zA-Z0-9-]+)\{background:(\-\d+\.\d+)px', content)
    result = {}
    for item in matched:
        css_class = item[0][1:]
        offset = item[1]
        result[css_class] = offset
    return result

```

这个函数返回的是一个字典，它的key是css class的名字，value是css class对应的数字在背景图片中的偏移量。




接下来，我们以评论条数为例，来获取点评上一个页面里每家餐厅的评论条数。先定义函数，用于获取评论条数

```python
def get_review_num(page_url, class_offset, digits):
    r = requests.get(page_url, headers=headers)
    content = r.content.decode("utf-8")
    root = etree.HTML(content)
    shop_nodes = root.xpath('.//div[@id="shop-all-list"]/ul/li')
    for shop_node in shop_nodes:
        name_node = shop_node.xpath('.//div[@class="tit"]/a')[0]
        name = name_node.attrib["title"]
        review_num_node = shop_node.xpath('.//div[@class="comment"]/a[@class="review-num"]/b')[0]
        num = 0
        if review_num_node.text:
            num = num * 10 + int(review_num_node.text)
        for digit_node in review_num_node:
            css_class = digit_node.attrib["class"]
            offset = class_offset[css_class]
            index = int((float(offset)+7)/-12)
            digit = int(digits[index])
            num = num * 10 + digit
        last_digit = review_num_node[-1].tail
        if last_digit:
            num = num * 10 + int(last_digit)
        print("restaurant: {}, review num: {}".format(name, num))

```




然后调用函数，爬一下页面中每家餐厅的评论条数

```python
css_url = get_css()
digits = get_svg(css_url)
class_offset = get_class_offset(css_url)
url = "http://www.dianping.com/shanghai/ch10/g116"
get_review_num(url, class_offset, digits)

```




运行代码后，得到如下的结果

```bash
restaurant: 1886汽车主题德国餐厅(环宇荟店), review num: 1021
restaurant: Mia Fringe迷芬奇餐厅&酒吧, review num: 152
restaurant: Oyster EXPO江月蚝庭西餐生蚝吧(世博源店), review num: 1405
restaurant: 宝莱纳餐厅(陆家嘴店), review num: 7854
restaurant: Pizza Marzano玛尚诺(港汇店), review num: 7527
restaurant: love&salt牛排馆, review num: 86
restaurant: Da Ivo 意大利魔镜餐厅, review num: 3497
restaurant: Mr Nice好好先生餐厅(月星环球港店), review num: 9052
restaurant: L'ATELIER de Joël Robuchon, review num: 2821
restaurant: Stone Sal 言盐西餐厅, review num: 62
restaurant: 夏朵花园, review num: 3031
restaurant: 壳里西餐厅Coquille Seafood Bistro, review num: 322
restaurant: ICHA Chateau Bar & Restaurant(酒吧创意料理), review num: 496
restaurant: 菲斯特花园西餐厅, review num: 655
restaurant: 宝丽嘉酒店Cafe Bellagio(宝丽嘉西餐厅), review num: 598

```

对照网页上的数据，可以看到，餐厅的评论条数都被正确的解析出来了。




本文已同步更新到公众号【Python与数据分析】，欢迎关注~
