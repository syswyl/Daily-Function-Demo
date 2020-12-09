# Daily-Function-Demo
Daily write some small function program （most in python &amp; matlab）

# 日常功能demo

#### Description
在日常学习生活中实现的一些小方法，针对特定要求实现，我会对每一个demo进行简单介绍。


#### Instructions

1.   **使用python实现了双边均值滤波，高斯滤波和均值滤波。** 
[滤波代码](https://gitee.com/iis_chaer/daily-function-demo/blob/master/demo/%E6%BB%A4%E6%B3%A2.py)

2.   **在数据训练时，有时候会需要将txt文件转为xml文件。** 或者使用labelimg时候最初读入xml文件，本代码实现根据
txt中的图片文件名字读取图片，获取txt中每行数据（代表一个框），并且转化为xml格式存储的功能。
[txt-to-xml](https://gitee.com/iis_chaer/daily-function-demo/blob/master/demo/%E6%A0%B9%E6%8D%AE%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84%E5%B0%86txt%E6%96%87%E4%BB%B6%E8%BD%AC%E5%8C%96%E4%B8%BAxml%E6%96%87%E4%BB%B6.py)

3.   **根据基础文件进行模糊匹配，对文件夹进行移动的功能。** [文件夹匹配移动](https://gitee.com/iis_chaer/daily-function-demo/blob/master/demo/%E6%A0%B9%E6%8D%AE%E6%96%87%E4%BB%B6%E5%90%8D%E5%AD%97%E4%B8%8D%E7%B2%BE%E5%87%86%E5%8C%B9%E9%85%8D%E7%B2%98%E8%B4%B4.py)

在工作中可能出现，不同路径下建立了名字类似的文件夹，比如d:\A\张三，d:\b\张三-简历，但是现在需要见简历文件夹下的所有文件移动
到张三中，一个一个的移动太慢了，通过遍历和模糊匹配再copy就可以很好的解决，代码就实现了遍历路径下的文件夹，并且匹配，移动的功能，针对自己的问题可以进行自定义调整。
![问题示例](https://images.gitee.com/uploads/images/2020/1008/160839_aede1b02_5398340.jpeg "搜狗截图20201008160626.jpg")


4.   **根据xml结果文件，对图片中的目标框进行裁剪并且保存。** [根据xml裁剪图片中的目标框](https://gitee.com/IIS_Chaser/daily-function-demo/blob/master/demo/%E8%A3%81%E5%89%AAxml%E7%9B%AE%E6%A0%87%E6%A1%86.py)

在使用例如caffe-ssd进行检测后，得到的结果文件是xml文件，有时候为了对每一张图片中的检测结果进行分析，可能
需要将每一个目标框单独裁剪出来，本代码实现了上述功能，文件夹等路径可以根据自己需要进行调整。

#### Contribution

1.  contributor  shuangsong 

#### Gitee Feature

1.  You can use Readme\_XXX.md to support different languages, such as Readme\_en.md, Readme\_zh.md
2.  Gitee blog [blog.gitee.com](https://blog.gitee.com)
3.  Explore open source project [https://gitee.com/explore](https://gitee.com/explore)
4.  The most valuable open source project [GVP](https://gitee.com/gvp)
5.  The manual of Gitee [https://gitee.com/help](https://gitee.com/help)
6.  The most popular members  [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)