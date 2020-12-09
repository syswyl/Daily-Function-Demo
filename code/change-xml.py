# -*- encoding: utf-8 -*-

'''
@File    :   change_xml.py
@Time    :   2020/12/09 22:06:24
@Author  :   chaser_ss 
@Version :   1.0
@Contact :   chaser_ss@qq.com
'''

# Here put the import Lib

# 对图像大小修改之后,需要把对应的xml的框进行缩放,本脚本即实现对应功能,缩放具体系数需要根据缩放尺寸进行修改
import os
import os.path
import glob
from tqdm import tqdm
try: 
  import xml.etree.cElementTree as ET 
except ImportError: 
  import xml.etree.ElementTree as ET 
import sys 
for f in tqdm(glob.glob('VOC2019/Annotations/*.xml')):
#    print(f)
    tree = ET.parse(f)     #打开xml文档 
    root = tree.getroot()         #获得root节点  
    for size in root.findall('size'): #找到root节点下的size节点 
        size.find('width').text = '512'
        size.find('height').text = '350'     
    for object in root.findall('object'): #找到root节点下的所有object节点 
        bndbox = object.find('bndbox')      #子节点下属性bndbox的值 
        bndbox.find('xmin').text = str(int(int(bndbox.find('xmin').text) / 4))
        bndbox.find('ymin').text = str(int(int(bndbox.find('ymin').text) / 4))
        bndbox.find('xmax').text = str(int(int(bndbox.find('xmax').text) / 4))
        bndbox.find('ymax').text = str(int(int(bndbox.find('ymax').text) / 4))
    tree.write(f)


