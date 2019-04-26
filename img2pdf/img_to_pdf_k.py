# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 21:19:56 2019

@author: DHF
"""

import os
from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen import canvas
from PIL import Image
 

 
#ng = im.rotate(180) #逆时针旋转 45 度角。
#im.transpose(img.FLIP_LEFT_RIGHT) #左右对换。
#im.transpose(img.FLIP_TOP_BOTTOM) #上下对换。
#im.transpose(Image.ROTATE_90) #旋转 90 度角。
 
#im.transpose(Image.ROTATE_270) #旋转 270 度角。
#im.show()
#ng.show()
def rotate_img(path_old,path_new):
    img_dir = os.listdir(path_old)
    img_dir.sort(key= lambda x:int(x[:-4]))
    i=0
    for filename in img_dir:
        im = Image.open("%s/%s"%(path_old,filename))
        #ng = im.transpose(img.ROTATE_180) #旋转 180 度角。
        #ng = im.transpose(img.FLIP_LEFT_RIGHT) #左右对换。
        ng = im.transpose(Image.ROTATE_270) #旋转 90 度角。
        #ng = im.transpose(img.FLIP_TOP_BOTTOM)  # 上下对换。
        ng.save(path_new +"/"+ str(i) +'.jpg')
        i+=1

 
def imgtopdf(input_paths, outputpath):
    (maxw, maxh) = Image.open(input_paths).size
    c = canvas.Canvas(outputpath, pagesize=portrait((maxw, maxh)))
    c.drawImage(input_paths, 0, 0, maxw, maxh)
    c.showPage()
    c.save()

def run(img_dir,pdf_dir):
    count=0
    img_list=os.listdir(img_dir)
    img_list.sort(key= lambda x:int(x[:-4]))
    for filename in img_list:
        img_path="%s/%s"%(img_dir,filename)
        pdf_path="%s/%s_%d.pdf"%(pdf_dir,img_dir,count)
        count+=1
        imgtopdf(img_path,pdf_path)
# 调用demo:
rotate_img("bss","bssr")
run("bssr", "bssp")
