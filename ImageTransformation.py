#Image Translation
import cv2
import numpy as np
pic=cv2.imread('clouds.jpg')
cols=pic.shape[1]
rows=pic.shape[0]
M=np.float32([[1,0,-50],[0,1,-100]])    #declaring transformed vertices in matrix form
shifted= cv2.warpAffine(pic,M,(cols,rows))
cv2.imshow('Shifted Image',shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Image Rotation
rows2=pic.shape[1]
cols2=pic.shape[0]
center=(cols2/2, rows2/2)
angle=90
M2=cv2.getRotationMatrix2D(center,angle,1)
rotate=cv2.warpAffine(pic,M2,(cols2,rows2))
cv2.imshow('Rotated Image',rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Image Thresholding
threshold_value=200           #you can change thresold value as your requirement
(t_value,binary_threshold)=cv2.threshold(pic,threshold_value,255,cv2.THRESH_BINARY)
cv2.imshow('Binary',binary_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Gaussian Blur
matrix=(7,7)
blur=cv2.GaussianBlur(pic,matrix,0)
cv2.imshow('Blur',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Medium Blur
kernal=3
median=cv2.medianBlur(pic,kernal)
cv2.imshow('Median blur',median)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Bilateral FIltering
dimpixel=2
color=150
space=50
filter=cv2.bilateralFilter(pic,dimpixel,color,space)
cv2.imshow('Filter',filter)
cv2.waitKey(0)
cv2.destroyAllWindows()