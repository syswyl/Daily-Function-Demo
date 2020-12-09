import time
import os
from PIL import Image
import cv2

out0 ='''<?xml version="1.0" encoding="utf-8"?>
<annotation>
    <folder>None</folder>
    <filename>%(name)s</filename>
    <source>
        <database>None</database>
        <annotation>None</annotation>
        <image>None</image>
        <flickrid>None</flickrid>
    </source>
    <owner>
        <flickrid>None</flickrid>
        <name>None</name>
    </owner>
    <segmented>0</segmented>
    <size>
        <width>%(width)d</width>
        <height>%(height)d</height>
        <depth>3</depth>
    </size>
'''
out1 = '''    <object>
        <name>%(class)s</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
            <xmin>%(xmin)d</xmin>
            <ymin>%(ymin)d</ymin>
            <xmax>%(xmax)d</xmax>
            <ymax>%(ymax)d</ymax>
        </bndbox>
    </object>
'''

out2 = '''</annotation>
'''

#names = ["CD"]

def translate(lists): 
    source = {}
    label = {}
    for jpg in lists:
        if os.path.splitext(jpg)[1] == '.png':
            #img=cv2.imread(jpg)
            #h,w,_=img.shape[:]
            image= cv2.imread(jpg)
            h,w,_ = image.shape
#            h=320
#            w=320
            
            fxml = jpg.replace('JPEGImages','Annotations')
            fxml = fxml.replace('.png','.xml')
            fxml = open(fxml, 'w');
            imgfile = jpg.split('/')[-1]
            source['name'] = imgfile            

            source['width'] = w
            source['height'] = h
            
            fxml.write(out0 % source)
            txt = jpg.replace('.png','.txt')
            txt = txt.replace('JPEGImages','labels')
            with open(txt,'r') as f:
                lines = [i.replace('\n','') for i in f.readlines()]

            for box in lines:
                box = box.split(' ')
                label['class'] = box[0]
#                _x = int(float(box[1])*w)
#                _y = int(float(box[2])*h)
#                _w = int(float(box[3])*w)
#                _h = int(float(box[4])*h)

                _x = int(float(box[1]))
                _y = int(float(box[2]))
                _w = int(float(box[3]))
                _h = int(float(box[4]))
                
                label['xmin'] = max(_x,0)
                label['ymin'] = max(_y,0)
                label['xmax'] = min(int(_w),w-1)
                label['ymax'] = min(int(_h),h-1)

                # if label['xmin']>=w or label['ymin']>=h or label['xmax']>=w or label['ymax']>=h:
                #     continue
                # if label['xmin']<0 or label['ymin']<0 or label['xmax']<0 or label['ymax']<0:
                #     continue
                    
                fxml.write(out1 % label)
            fxml.write(out2)

if __name__ == '__main__':
    with open('ss.txt','r') as f:
        lines = [i.replace('\n','') for i in f.readlines()]
        translate(lines)
