import cv2
import numpy as np

#Load image
I = cv2.imread("C:\\Users\\Dell\\Downloads\\Lenna.png")

#show Image
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
cv2.imshow("Image",I)
#cv2.waitKey()

# #convert Image to gray
# gray = cv2.cvtColor(I,cv2.COLOR_RGB2GRAY)
# cv2.imshow("gray",gray)
# #cv2.waitKey()
#
# #get dimension
# print("rgbImage: ",I.shape)                                     # (rows,columns,channels)
# print("grayImage: ",gray.shape)
# [rows ,cols] = gray.shape
#
# for i in range(rows):
#     for j in range(cols):
#         if i%2 == 0 and j%2 == 0:
#             print(gray[i,j],end = " ")
#             gray[i,j] = 255
#     print('\n')
# cv2.imshow("new gray",gray)
# cv2.waitKey()

#get value color
[rows,cols,channel] = I.shape
for i in range(10):
    for j in range(10):
        print(" {",end= "")
        for k in range(channel):
            print(I[i,j,k], end=",")
        print("}",end=" ")
    print("\n")
cv2.imshow("new color",I)
cv2.waitKey()
