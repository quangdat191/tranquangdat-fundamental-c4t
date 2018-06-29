import numpy as np
import cv2

I = cv2.imread("C:\\Users\\Dell\\Downloads\\noise_house.jpg")
print(I.shape)
print(I[0,0,:])
gray = cv2.cvtColor(I,cv2.COLOR_RGBA2GRAY)
ret,binImg = cv2.threshold(gray,50,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print(ret)
cv2.imshow("binImg",binImg)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
bin_erode = cv2.erode(binImg,kernel)
bin_dilate = cv2.dilate(bin_erode,kernel)
cv2.imshow("input Image",I)
cv2.imshow("dilitation",bin_dilate)
cv2.imshow("erosion",bin_erode)
cv2.waitKey()