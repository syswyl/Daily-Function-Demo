# -*- encoding: utf-8 -*-

'''
@File    :   sum_xml.py
@Time    :   2020/12/09 22:52:13
@Author  :   chaser_ss 
@Version :   1.0
@Contact :   chaser_ss@qq.com
'''

# Here put the import Lib

# 根据路径xml统计数据集中各个零部件类别的数量
import os
import xml.etree.ElementTree as ET
 
def parse_obj(xml_path, filename):
    tree=ET.parse(xml_path+filename)
    objects=[]
    for obj in tree.findall('object'):
        obj_struct={}
        obj_struct['name']=obj.find('name').text
        objects.append(obj_struct)
    return objects
 
 
 
if __name__ == '__main__':
    text_path = './normal_high/ImageSets/Main/train.txt'
    xml_path = './normal_high/Annotations/'
    filenames = []
    for line in open(text_path,'r'):
        filenames.append(line.strip('\n'))
    recs={}
    obs_shape={}
    classnames=[]
    num_objs={}
    obj_avg={}
#    filenames = ['100001','100002']
#    print(filenames)
    for i,name in enumerate(filenames):
        recs[name]=parse_obj(xml_path, name+ '.xml' )
    back_file = []
    for name in filenames:
        # print(name)
        for object in recs[name]:
            if object['name'] not in num_objs.keys():
                num_objs[object['name']]=1
            else:
                num_objs[object['name']]+=1
            if object['name'] not in classnames:
                classnames.append(object['name'])
        if object['name'] in ['side_brake_display','side_grid','side_overhaul','side_screw','side_wheel']:
            back_file.append(name)
    # print(classnames)
    print('根据' + text_path +  '中的xml文件名字统计' + xml_path +  '对应文件中各类别数')
    for name in classnames:
        print('{}:{}个'.format(name, num_objs[name]))
    print('信息统计算完毕。')
    print(back_file[-10:])
 
