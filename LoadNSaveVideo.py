
#Load a video

import cv2
import numpy as np

cap = cv2.VideoCapture('nature.mp4')

while (cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#Save a video in different format


#already read the video in cap

fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 30
framesize = (720, 480)
out = cv2.VideoWriter('sample.avi',fourcc, fps, framesize)
while (cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
out.release()
cap.release()
cv2.destroyAllWindows()