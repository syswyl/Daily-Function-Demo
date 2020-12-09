#coding=utf-8
import os
import os.path
import shutil  #Python文件复制相应模块
 
def GetFileNameAndExt(filename):
    (filepath,tempfilename) = os.path.split(filename);
    (shotname,extension) = os.path.splitext(tempfilename);
    return shotname,extension
 
source_dir='烟草A'
label_dir='/home/nvidia/xmlReader/label'
annotion_dir='/home/nvidia/xmlReader/annocation'
 
##1.将指定A目录下的文件名取出,并将文件名文本和文件后缀拆分出来
img=os.listdir(source_dir)  #得到文件夹下所有文件名称
print(img)
# s=[]

for fileNum in img: #遍历文件夹
    person=os.listdir(source_dir + '/' + fileNum)  #得到文件夹下所有文件名称
    for person_num in person:
        print(person_num)
#     if not os.path.isdir(fileNum): #判断是否是文件夹,不是文件夹才打开
#         print fileNum  #打印出文件名
#         imgname= os.path.join(source_dir,fileNum)
#         print imgname  #打印出文件路径
#         (imgpath,tempimgname) = os.path.split(imgname); #将路径与文件名分开
#         (shotname,extension) = os.path.splitext(tempimgname); #将文件名文本与文件后缀分开
# 	print shotname,extension
# 	print '~~~~'
# ##2.将取出来的文件名文本与特定后缀拼接,再与路径B拼接,得到B目录下的文件	
# 	tempxmlname='%s.xml'%shotname	
# 	xmlname=os.path.join(label_dir,tempxmlname)
# 	print xmlname
# ##3.根据得到的xml文件名,将对应文件拷贝到指定目录C
# 	shutil.copy(xmlname,annotion_dir)
	
