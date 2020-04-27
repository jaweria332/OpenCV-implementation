#Drawing a line
import cv2
import numpy as np
pic=np.zeros((500,500,3),dtype='uint8')
cv2.line(pic,(10,350),(250,350),(255,0,255))
cv2.imshow('Line',pic)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Drawing a Rectangle
pic=np.zeros((500,500,3),dtype='uint8')
cv2.rectangle(pic,(0,0),(300,300),(0,0,255),3,shift=0)
cv2.imshow('Rectangle',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Drawing a circle
pic2=np.zeros((500,500,3),dtype='uint8')
color=(0,255,0)
cv2.circle(pic2,(250,250),150,color)
cv2.imshow('Circle',pic2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Writing text
pic3=np.zeros((500,500,3),dtype='uint8')
font=cv2.FONT_HERSHEY_DUPLEX
cv2.putText(pic3, 'OpenCV', (100,100), font,  3, (255,0,0), 2, cv2.LINE_AA)
cv2.imshow('Text Window',pic3)
cv2.waitKey(0)
cv2.destroyAllWindows()

#To show all these shapes in single output window
pic=np.zeros((500,500,3),dtype='uint8')
cv2.line(pic,(100,350),(400,350),(255,0,255))  #For line
cv2.rectangle(pic,(100,100),(400,400),(0,0,255),3,shift=0)  #For rectangle
cv2.circle(pic,(250,250),150,(0,255,0))   #For circle
font=cv2.FONT_HERSHEY_DUPLEX
cv2.putText(pic, 'OpenCV', (125,300), font,  2, (255,0,0), 2, cv2.LINE_AA)
cv2.imshow('ALl in one', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()