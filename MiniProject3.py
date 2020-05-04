import numpy as np
import cv2
img = cv2.imread('someshapes.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours (threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x-140,y-205), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.drawContours(img, [approx], 0, (0,255,0), 10)
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        Ratio = float(w)/h
        print(Ratio)
        if Ratio>= 0.95 and Ratio<= 1.05:
            cv2.putText(img, "Square", (x+50, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
            cv2.putText(img, "Rectangle", (x+100, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    elif len(approx) == 5:
        cv2.putText(img, "Pentagone", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    elif len(approx) == 10:
        cv2.putText(img, "Star", (x+120, y-110), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    else:
        cv2.putText(img, "Circle", (x-10, y-20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()