# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib as mpl
import cv2
img = cv2.imread ("C:\\Users\\Sanat Mohrir\\Desktop\\cris.png", 1)
resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("goat",resized)
cv2.waitKey(2000)
cv2.destroyAllWindows()