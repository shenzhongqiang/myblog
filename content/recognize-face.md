Title: 基于face_recognition实现人脸识别
url: recognize-face.html
save_as: recognize-face.html
Date: 2018-06-23
Category: 图像处理
Tags: Python, 图像处理
Authors: Zhongqiang Shen

上一篇文章[50行代码实现人脸检测](https://zhuanlan.zhihu.com/p/32781218)收到了很多朋友的点赞，非常感谢大家的鼓励。上一篇中我们实现了检测照片中的人脸并标出人脸特征点（鼻子，眼睛，眉毛等），这一篇我们将在上一篇的基础上，进一步实现人脸识别，告诉你照片里的人是谁。




#### 准备工作

我们的人脸识别基于face\_recognition库。face\_recognition基于dlib实现，用深度学习训练数据，模型准确率高达99.38%。在开始我们的工作前，我们先安装face\_recognition

```bash
pip install face_recognition

```




#### 人脸数字化

人脸识别的第一步是检测照片中的人脸区域，然后将人脸的图像数据转换成一个长度为128的向量，这128个数据代表了人脸的128个特征指标，如下所示

![]({static}/images/v2-a6dd4b87f6ea6085a466958300295095_r.jpg)

对于每一张已知人脸，生成这样的一个128位的向量。对于一张未知人脸，将它的128位向量和所有已知人脸的128位向量一一比对，找到相似度最高的那一个，即找出了未知人脸对应的人。




#### 图片数据

我们准备了两张照片，分别是凯特王妃和威廉王子的单人照，分别存成catherine.jpg和william.jpg，这两张照片中的人脸作为我们的已知人脸

![]({static}/images/v2-5ceafbb24e04f2c23bb1c883f7fb1120_r.jpg)

我们的目标是在下面的合影中识别出两人的脸并在图中标出各自的名字。下图存成unknown.jpg

![]({static}/images/v2-d565c85c26e4111316493249b378778c_r.jpg)




#### 代码实现

接下来开始我们的编程工作

```python
import cv2
import face_recognition

names = [
    "catherine",
    "william",
]

```

首先我们定义了标签集，存在names数组中。

标签名字也是我们图片的文件名。




```python
images = []
for name in names:
    filename = name + ".jpg"
    image = face_recognition.load_image_file(filename)
    images.append(image)
unknown_image = face_recognition.load_image_file("unknown.jpg")

```

调用face\_recognition.load\_image\_file从图片中读取数据。

这里读取了包含已知人脸和未知人脸的图片的数据，未知人脸的图片就是上面的合影图片unknown.jpg。




```python
face_encodings = []
for image in images:
    encoding = face_recognition.face_encodings(image)[0]
    face_encodings.append(encoding)
unknown_face_encodings = face_recognition.face_encodings(unknown_image)

```

将人脸的图像数据转换成128位向量，已知人脸的向量存入face\_encodings数组，未知人脸的图像数据存入unknown\_face\_encodings数组。

face\_recognition.face\_encodings会返回图片中的所有的人脸的128位向量。单人照片只有一张人脸，所以face\_recognition.face\_encodings(image)[0]只取第一个元素。合影图片中包含了2张人脸，所以unknown\_face\_encodings包含2个128位向量。




```python
face_locations = face_recognition.face_locations(unknown_image)
for i in range(len(unknown_face_encodings)):
    unknown_encoding = unknown_face_encodings[i]
    face_location = face_locations[i]
    top, right, bottom, left = face_location
    cv2.rectangle(unknown_image, (left, top), (right, bottom), (0, 255, 0), 2)
    results = face_recognition.compare_faces(face_encodings, unknown_encoding)
    for j in range(len(results)):
        if results[j]:
            name = names[j]
            cv2.putText(unknown_image, name, (left-10, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

unknown_image_rgb = cv2.cvtColor(unknown_image, cv2.COLOR_BGR2RGB)
cv2.imshow("Output", unknown_image_rgb)
cv2.waitKey(0)

```

face\_locations存了每张脸的位置信息。

在循环中我们调用cv2.rectangle框出了检测到的每张脸。

face\_recognition.compare\_faces将已知人脸的128位向量和每张未知人脸的128位向量做比较，结果存入results数组中。results数组中的每一个元素都是True或者False，长度和人脸个数相等。results中的每个元素都和已知人脸一一对应，在某一个位置处的元素为True，表示未知人脸被识别成这张已知人脸。

对识别出来的每张人脸，我们调用cv2.putText在图上标注标签。




以上是代码的全部。




#### 测试

令人兴奋的时刻又来到了！ 我们来检验一下我们的成果。

运行上面的程序，可以看到下面的结果

![]({static}/images/v2-4093c883e5231a7ae1ac3c5eb58752dd_r.jpg)

威廉王子和凯特王妃的人脸都被准确地识别出来。绿色的框框出了人脸区域，框的上方标注了识别到的人的名字。

至此，我们成功地实现了人脸识别。




本文已更新微信同名公众号【Python与数据分析】，欢迎关注~

![]({static}/images/v2-e9b0b9b9584ccdd3ff4c96b7ecfd8a56_r.jpg)



