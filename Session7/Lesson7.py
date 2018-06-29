import cv2
import numpy as np
I = cv2.imread("C:\\Users\\Dell\\Downloads\\shape.jpg")
cv2.imshow("origin",I)
# cv2.waitKey()

# exteact 3 channels
B = I[:,:,0]
G = I[:,:,1]
R = I[:,:,2]
cv2.imshow("Blue",B)
cv2.imshow("Green",G)
cv2.imshow("Red",R)
# cv2.waitKey()

# Black
C_plus = B&G&R
cv2.imshow("Black",C_plus)
# cv2.waitKey()

#Convert Image to binary
ret, binImg = cv2.threshold(C_plus,100,255,cv2.THRESH_BINARY_INV)
cv2.imshow("binary",binImg)
# cv2.waitKey()

# find contour
ret,contours,hierarchy = cv2.findContours(binImg,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

# for i in contours:
#     cv2.drawContours(I,i,-1,(255,0,255),5)

#find contour (C2)
for i in range(len(contours)):
    cv2.drawContours(I,contours,i,(255,0,255),5)
    leni = cv2.arcLength(contours[i],True)
    print("len of contour: ",leni)
    areai = cv2.contourArea(contours[i])
    print("area of contour",areai)
    # approximate polygon
    no_edges = cv2.approxPolyDP(contours[i],5,True)
    print("poliedge: ",len(no_edges))
    if len(no_edges) == 3:
        cv2.putText(I,"tam giac",(no_edges[1][0][0],no_edges[1][0][1]),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
    if len(no_edges) == 4:
        cv2.putText(I,"HCN",(no_edges[0][0][0],no_edges[0][0][1]),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
    if len(no_edges) > 8:
        cv2.putText(I,"tron",(no_edges[0][0][0],no_edges[0][0][1]),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
    M = cv2.moments(contours[i])
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv2.circle(I,(cx,cy),10,(120,255,0),3)
cv2.imshow("Image contour",I)
cv2.waitKey()