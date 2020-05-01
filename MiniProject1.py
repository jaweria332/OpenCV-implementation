import numpy as np
import cv2

img = cv2.imread('person-1.jpg')
print(img.shape)
cv2.imshow('Original', img)

kernel_sharpening = np.array([[-1, -1, -1],[-1, 9, -1], [-1, -1, -1]])
sharpened = cv2.filter2D(img, -1, kernel_sharpening)
cv2.imshow('Sharpened image', sharpened)

gray = cv2.cvtColor(sharpened, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)

inv = 255-gray
gauss = cv2.GaussianBlur(inv, ksize=(15,15), sigmaX=0,sigmaY=0)
canny=cv2.Canny(255-gauss,50, 100)

cv2.imshow('Original', img)
cv2.imshow('rough sketch', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()