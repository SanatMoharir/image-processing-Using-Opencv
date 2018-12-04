# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:44:23 2018

@author: Sanat Mohrir
"""
import numpy as np
import matplotlib as mpl
import cv2
face_cascade = cv2.CascadeClassifier("C:\\Users\\Sanat Mohrir\\Desktop\\haarcascade_frontalface_default.xml")
img = cv2.imread("C:\\Users\\Sanat Mohrir\\Desktop\\cris.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors=5)
print(type(faces))
print(faces)

for x,y,w,h in faces:
    img =cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)
    
resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Gray", resized) 

cv2.waitKey(2000000)  

cv2.destroyAllWindows()  

