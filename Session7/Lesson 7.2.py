import numpy as np
import cv2

#connect webcam
cap = cv2.VideoCapture(0)

lower = np.array([0,30,48])
higher = np.array([179,217,255])

while (True):
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    cv2.rectangle(frame,(0,0),(int(frame.shape[1]/2),3*int(frame.shape[0]/4)),(0,0,255),5)

    # get ROI
    roi = frame[5:3*int(frame.shape[0]/4)-5,5:int(frame.shape[1]/2)-5,:]


    hsvImage = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # convert to binary
    binImage = cv2.inRange(hsvImage,lower,higher)

    # find contour
    ret, contours, hierarchy = cv2.findContours(binImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for i in contours:
        cv2.drawContours(binImage,i,-1,(255,0,255),5)

    if len(contours)>0:
        maxlen = cv2.arcLength(contours[0],True)
        indexmax = 0
        for i in range(len(contours)):
            leni = cv2.arcLength(contours[i],True)
            if leni > maxlen:
                maxlen = leni
                indexmax = i
            cv2.drawContours(roi, contours[i], -1, (0, 255, 0), 5)
        M = cv2.moments(contours[indexmax])
        if M['m00'] !=0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            cv2.circle(roi, (cx, cy), 10, (120, 255, 0), 3)

    # cv2.imshow("hsvImage",hsvImage)
    cv2.imshow("video",frame)
    # cv2.imshow("binImage",binImage)
    cv2.imshow("roiImage", roi)
    key = cv2.waitKey(30)
    if key == ord('q'):
        break