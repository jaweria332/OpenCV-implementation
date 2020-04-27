#Image face detection of picture
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('faces.jpg')

faces = face_cascade.detectMultiScale(img, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow('image', img)
cv2.waitKey()

#Image face detection using webcam

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    _, img =cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY
                        )
    faces = face_cascade.detectMultiScale(img, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow('image', img)
    k = cv2.waitKey(30) & 0xff

    if k==27:
        break
cap.release()
