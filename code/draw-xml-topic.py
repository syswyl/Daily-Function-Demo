# -*- encoding: utf-8 -*-

'''
@File    :   draw_xml.py
@Time    :   2020/12/09 22:38:22
@Author  :   chaser_ss 
@Version :   1.0
@Contact :   chaser_ss@qq.com
'''

# Here put the import Lib

#批量处理img和xml文件，根据xml文件中的坐标把img中的目标标记出来，并保存到指定文件夹，方便自己查看目标标记的是否准确。
import xml.etree.ElementTree as ET
import os, cv2
from tqdm import tqdm

annota_dir = '/home/iis/data/high_data/VOC2020/Annotations/'
origin_dir = '/home/iis/data/high_data/VOC2020/JPEGImages/'
target_dir1='/home/iis/data/high_data/VOC2020/Drawimages/'

def divide_img(oriname):
    if not os.path.exists(target_dir1):
        os.makedirs(target_dir1)
    img_file = os.path.join(origin_dir, oriname + '.jpg')
    im = cv2.imread(img_file)

    xml_file = os.path.join(annota_dir, oriname + '.xml')  # 读取每个原图像的xml文件
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for object in (root.findall('object')):
        object_name = object.find('name').text
        Xmin = int(object.find('bndbox').find('xmin').text)
        Ymin = int(object.find('bndbox').find('ymin').text)
        Xmax = int(object.find('bndbox').find('xmax').text)
        Ymax = int(object.find('bndbox').find('ymax').text)
        color = (4, 250, 7)
        cv2.rectangle(im, (Xmin, Ymin), (Xmax, Ymax), color, 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(im, object_name, (Xmin, Ymin - 7), font, 1, (6, 230, 230), 2)
#        cv2.imshow('01', im)

    img_name = oriname + '.jpg'
    to_name = os.path.join(target_dir1, img_name)
    cv2.imwrite(to_name, im)



img_list = os.listdir(origin_dir)
for index, name in enumerate(tqdm(img_list)):
    if index < 15:
        divide_img(name.rstrip('.jpg'))
    else:
        break
    

