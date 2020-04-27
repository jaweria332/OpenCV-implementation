import cv2
import numpy as np
pic=cv2.imread('clouds.jpg')
thresholdval1=50
thresholdval2=100
canny=cv2.Canny(pic,thresholdval1,thresholdval2)
cv2.imshow('Canny',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()