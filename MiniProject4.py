import numpy as np
import cv2
img = cv2.imread('blobs.jpg')

output = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=50, minRadius=0, maxRadius=0)

detected_circles = np.uint16(np.around(circles))
for i in detected_circles[0, :]:
    cv2.circle(output, (i[0], i[1]), i[2], (0, 255, 0), 3)
    cv2.circle(output, (i[0], i[1]), 2, (0, 255, 0), 3)


cv2.imshow('output', output)
cv2.waitKey(0)
cv2.destroyAllWindows()