# -*- coding: utf-8 -*-

"""
Author: zhongwen wang
条码EAN-13
"""
import pyzbar.pyzbar as pyzbar
import numpy
#from PIL import Image, ImageDraw, ImageFont
import cv2

frame=cv2.imread('d:/soft/scan/JPG/test2.jpg')
frame=cv2.imread('d:/soft/scan/JPG/0002.jpg')
frame=cv2.imread('d:/soft/scan/JPG/test2.jpg')
frame=cv2.imread('d:/soft/scan/JPG/0007.jpg')
# 转为灰度图像
ff=frame[200:400,800:1500]
aa=cv2.resize(ff,(300,200))
cv2.imshow('test',ff)
cv2.waitKey(0)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
barcodes = pyzbar.decode(gray)

