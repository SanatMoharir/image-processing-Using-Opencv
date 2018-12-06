# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 14:07:39 2018

@author: Sanat Mohrir
"""

import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread("C:\\Users\\Sanat Mohrir\\Desktop\\rma.jpg",0)
img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 =cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

th3 =cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

titles =['OG','Global Thresholding (v=127)','Adaptive mean Threshold','Adaptive Gaussian Threshol']

images = [img,th1,th2,th3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()    
