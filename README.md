# Daily-Function-Demo
Daily write some small function program （most in python &amp; matlab）

# 日常功能demo

#### Description
在日常学习生活中实现的一些小方法，针对特定要求实现，我会对每一个demo进行简单介绍。
## *Attention！ 这些代码都是本地针对特定环境和要求写的，可能与你所需要的有区别，但是整体我提供了一个方法和思路，并且代码应该都是bug free，只需要简单修改即可* ## 


#### Instructions

- **xml**
1.   **在数据训练时，有时候会需要将txt文件转为xml文件。** [txt-to-xml](https://github.com/syswyl/Daily-Function-Demo/blob/main/code/txt-to-xml.py)</br>&emsp;&emsp;或者使用labelimg时候最初读入xml文件，本代码实现根据
txt中的图片文件名字读取图片，获取txt中每行数据（代表一个框），并且转化为xml格式存储的功能。
2.   **根据xml结果文件，对图片中的目标框进行裁剪并且保存。** [根据xml裁剪图片中的目标框](https://github.com/syswyl/Daily-Function-Demo/blob/main/code/Crop-images-according-to-XML.py)</br>&emsp;&emsp;在使用例如caffe-ssd进行检测后，得到的结果文件是xml文件，有时候为了对每一张图片中的检测结果进行分析，可能
需要将每一个目标框单独裁剪出来，本代码实现了上述功能，文件夹等路径可以根据自己需要进行调整。
3.   **图像大小修改之后,需要把对应的xml的框进行缩放。** [缩放xml中的目标框](https://github.com/syswyl/Daily-Function-Demo/blob/main/code/change-xml.py)</br>&emsp;&emsp;在进行数据增强时候，图像缩放是一个常用的手段，在一些算法中已经实现了，本代码也就是根据xml，在图像大小修改之后，把对应的xml标签进行修改，以确保ground_truth不会错误，只是简单的缩放修改，很粗糙，可能在特定条件下能使用。</br>图像缩放是个很强的数据增强操作，在yolov4中，作者使用了一个随机的图像缩放和拼接的方法（Mosaic  具体可以参见论文[YOLOv4](https://arxiv.org/abs/2004.10934)）。
知乎有人单独实现了类似的操作，并且对于小目标的检测涨分效果很好。[知乎链接](https://www.zhihu.com/question/390191723?rf=390194081)，扯远了，所以图像缩放还是重要的！</br>图像大小修改之后，需要把对应的xml的框进行缩放，在所以需要把对应的xml的框进行缩放，本脚本即实现对应功能，缩放具体系数需要根据缩放尺寸进行修改
4.   **根据xml文件中的坐标把img中的目标标记出来。** [根据xml绘制图片中的目标框](https://github.com/syswyl/Daily-Function-Demo/blob/main/code/draw-xml-topic.py)</br>&emsp;&emsp;在一些文件中，可能返回结果只是xml，没有绘制好的目标框（比如caffe？），本代码实现，批量处理img和xml文件，根据xml文件中的坐标把img中的目标标记出来，并保存到指定文件夹，方便自己查看目标标记的是否准确。
5.   **根据路径xml统计数据集中各个目标类别的数量。** [根据xml统计各个类别的数量](https://github.com/syswyl/Daily-Function-Demo/blob/main/code/sum-class_num-xml.py)

- **other**
1.   **根据基础文件进行模糊匹配，对文件夹进行移动的功能。** [文件夹匹配移动](https://github.com/syswyl/Daily-Function-Demo/blob/main/code/File-mismatch.py)</br>&emsp;&emsp;在工作中可能出现，不同路径下建立了名字类似的文件夹，比如d:\A\张三，d:\b\张三-简历，但是现在需要见简历文件夹下的所有文件移动到张三中，一个一个的移动太慢了，通过遍历和模糊匹配再copy就可以很好的解决，代码就实现了遍历路径下的文件夹，并且匹配，移动的功能，针对自己的问题可以进行自定义调整。
![问题示例](https://github.com/syswyl/Daily-Function-Demo/blob/main/images/file-mismatch.jpeg)
2.   **使用python实现了双边均值滤波，高斯滤波和均值滤波。** [滤波代码](https://github.com/syswyl/Daily-Function-Demo/blob/main/code/wave-iltering.py)


#### Contribution

1.  contributor  （IIS Chaser)[chaser_ss@qq.com] 
