import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("C:\\Users\\Dell\\PycharmProjects\\Fundamental\\Session7\\haarcascade_frontalface_alt2.xml")
mask = cv2.imread("C:\\Users\\Dell\\PycharmProjects\\Fundamental\\Session7\\6.jpg")

while (True):
    ret,frame = cap.read()
    # convert image to gray
    gray = cv2.cvtColor(frame,cv2.COLOR_RGBA2GRAY)
    # detect face
    faces = cascade.detectMultiScale(gray)

    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        newmask = cv2.resize(mask,(w,h),cv2.INTER_CUBIC)
        frame[y:y+h,x:x+w,:] = frame[y:y+h,x:x+w,:]+newmask
    cv2.imshow("video",frame)
    key = cv2.waitKey(30)
    if key == ord('q'):
        break