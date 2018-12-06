# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 13:33:59 2018

@author: Sanat Mohrir
"""

import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread("C:\\Users\\Sanat Mohrir\\Desktop\\rma.jpg" ,0)

edge = cv2.Canny(img ,100,50)

plt.subplot(121),plt.imshow(img,cmap = 'gray')

plt.title('Original Image'), plt.xticks([]),plt.yticks([])

plt.subplot(122),plt.imshow (edge, cmap ='gray')

plt.title ('Edged Image'), plt.xticks([]) ,plt.yticks([])

plt.show()
