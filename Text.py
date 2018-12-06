# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 15:33:53 2018

@author: Sanat Mohrir
"""

import numpy as np
import cv2

img = cv2.imread("C:\\Users\\Sanat Mohrir\\Desktop\\cris.png",1)
font =cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img ,'G.O.A.T',(0,150),font,4,(255,0,0),4, cv2.LINE_AA)
cv2.imshow('image' ,img)

cv2.waitKey(0)

cv2.destroyAllWindows()