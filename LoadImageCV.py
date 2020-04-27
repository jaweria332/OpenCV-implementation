#How to load image in opencv2
import cv2
import numpy as np
img=cv2.imread('clouds.jpg')
cv2.imshow('CLOUDS',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#how to save image using openCV
import cv2
import numpy as np
img=cv2.imread('clouds.jpg')
img=cv2.imwrite('clouds.jpg',img)
cv2.imshow('Original CLouds',img)
cv2.waitKey()
cv2.destroyAllWindows()