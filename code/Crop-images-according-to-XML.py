import os
import xml.dom.minidom
import cv2 as cv
 
ImgPath = 'c:/users/16281/desktop/test_image/'
AnnoPath = 'c:/users/16281/desktop/test_xml/'

ProcessedPath = 'c:/users/16281/desktop/test_out/' 

imagelist = os.listdir(ImgPath)
for image in imagelist:
    image_pre, ext = os.path.splitext(image)
    imgfile = ImgPath + image
    xmlfile = AnnoPath + image_pre + '.xml'
    print(imgfile)
    #打开xml文档
    DOMTree = xml.dom.minidom.parse(xmlfile)
    #得到文档元素对象
    collection = DOMTree.documentElement
    #读取图片
    img = cv.imread(imgfile)
 
    filenamelist = collection.getElementsByTagName("filename")
    filename = filenamelist[0].childNodes[0].data
    #print(filename)
    #得到标签名为object的信息
    objectlist = collection.getElementsByTagName("object")
    i = 1
    for objects in objectlist:
        #每个object中得到子标签名为name的信息
        namelist = objects.getElementsByTagName('name')
        #通过此语句得到具体的某个name的值
        objectname = namelist[0].childNodes[0].data
        savepath = ProcessedPath + objectname
        bndbox = objects.getElementsByTagName('bndbox')
        for box in bndbox:
            x1_list = box.getElementsByTagName('xmin')
            x1 = int(x1_list[0].childNodes[0].data)
            y1_list = box.getElementsByTagName('ymin')
            y1 = int(y1_list[0].childNodes[0].data)
            x2_list = box.getElementsByTagName('xmax')
            x2 = int(x2_list[0].childNodes[0].data)
            y2_list = box.getElementsByTagName('ymax')
            y2 = int(y2_list[0].childNodes[0].data)
            #print('x1:' +str(x1)+' ' +'x2:'+ str(x2)+' ' + 'y1:'+str(y1)+' ' +'y2:'+str(y2))
            #cropped = img[y1:y2, x1:x2]
            cv.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), thickness=2)
            cv.putText(img, objectname, (x1, y1), cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0),
                       thickness=2)
            # cv.imshow('head', img)
            cv.imwrite(savepath + '/' + image_pre + '_' + str(i) + '.jpg', img)   #save picture
            i = i+1
