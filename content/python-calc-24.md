Title: 用Python算24点
url: python-calc-24.html
save_as: python-calc-24.html
Date: 2018-06-02
Category: Python
Tags: Python
Authors: Zhongqiang Shen

小外甥女的课后作业是算24点，看了一下题目，发现都挺难的，像下面这些：

7  7  3  3

8  8  3  3

5  5  5  1

1  5  7  10

2  5  5  10

只能用加减乘除，算出24点。

发现心算不容易，于是突发奇想，用Python写了一个程序来算。

#### 基本思路

枚举4个数字可以组成的所有的算式，找到其中等于24的式子。

对于每一个算式，我们用一棵二叉树来存取。根节点保存运算符（+,-,*,/），左子树保存运算符左侧的子算式，右子树保存运算符右侧的子算式，运算结果也存在根节点中。如下图




![]({static}/images/v2-76bec4dc034124082b813a71e333e030_b.jpg)




这棵二叉树对应的算式就是 (4 + 10) + (2 * 5) 。非常简单直观。

有了二叉树后，对于给定的一组数字，我们就可以递归地列出这组数字组成的所有可能的算式。




#### 具体实现

首先定义二叉树。对于树中的每一个节点，我们用一个Node类来保存

```python
class Node(object):
    def __init__(self, result=None):
        self._left = None
        self._right = None
        self._operator = None
        self._result = result

    def set_expression(self, left_node, right_node, operator):
        self._left = left_node
        self._right = right_node
        self._operator = operator
        expression = "{} {} {}".format(left_node._result, operator, right_node._result)
        self._result = eval(expression)

    def __repr__(self):
        if self._operator:
            return '<Node operator="{}">'.format(self._operator)
        else:
            return '<Node value="{}">'.format(self._result)

```

Node类中，如果 \_operator 是None，则 \_result 就是数字本身，如果 \_operator 不为None，则 \_result 表示的是左右两棵子树运算的结果。




对于一组给定顺序的数字，我们用递归的方式获取所有可能的算式

```python
def build_all_trees(array):
    if len(array) == 1:
        tree = Node(array[0])
        return [tree]

    treelist = []
    for i in range(1, len(array)):
        left_array = array[:i]
        right_array = array[i:]
        left_trees = build_all_trees(left_array)
        right_trees = build_all_trees(right_array)
        for left_tree in left_trees:
            for right_tree in right_trees:
                combined_trees = build_tree(left_tree, right_tree)
                treelist.extend(combined_trees)
    return treelist

```

上面函数的输入是一组数字，第一层for循环中将这组数字，拆成左右两部分，分别对应左右两棵子树的部分，输出的 treelist 是所有可能的算式。

对于给定的左子树和右子树，build\_tree 函数用加减乘除把它们连接在一起，组成新的二叉树。build\_tree 函数如下

```python
def build_tree(left_tree, right_tree):
    treelist = []
    tree1 = Node()
    tree1.set_expression(left_tree, right_tree, "+")
    treelist.append(tree1)
    tree2 = Node()
    tree2.set_expression(left_tree, right_tree, "-")
    treelist.append(tree2)
    tree4 = Node()
    tree4.set_expression(left_tree, right_tree, "*")
    treelist.append(tree4)
    if right_tree._result != 0:
        tree5 = Node()
        tree5.set_expression(left_tree, right_tree, "/")
        treelist.append(tree5)
    return treelist

```

build\_tree 中会枚举所有的运算方式，组成新的二叉树并返回所有可能的组合。

这里需要注意的是，如果运算方式是除法，除数也就是右侧子算式的结果不能为0。




罗列出所有的算式后，我们就来找一找有没有算式的结果是24。

```python
def find_24(array):
    perms = itertools.permutations(array)
    found = False
    for perm in perms:
        treelist = build_all_trees(perm)
        for tree in treelist:
            if math.isclose(tree._result, 24, rel_tol=1e-10):
                expression = get_expression(tree)
                print("{} - {}".format(perm, expression))
                found = True
                break
        if found:
            break

```

以上就实现了我们的算法。




#### 测试

下面是令人兴奋的时刻。我们用文章开始的几个例子来测一下我们的算法。

运行结果如下

```text
(7, 7, 3, 3)     - (7 * ((3 / 7) + 3))
(8, 8, 3, 3)     - (8 / (3 - (8 / 3)))
(5, 5, 5, 1)     - ((5 - (1 / 5)) * 5)
(1, 5, 7, 10)    - ((1 + (7 / 5)) * 10)
(2, 5, 5, 10)    - ((5 - (2 / 10)) * 5)

```

哈哈，都用到了小数运算，怪不得心算这么难呢~ 是不是很有趣？




算法中有一些重复的计算，有关于优化算法的建议，欢迎留言~




完整代码已上传GitHub。公众号【Python与数据分析】后台回复“**二十四**”可获取代码地址。



