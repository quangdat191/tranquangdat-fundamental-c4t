import numpy as np
import cv2

#Load Image RGB
I1 = cv2.imread("C:\\Users\\Dell\\Downloads\\shape.jpg")
I2 = cv2.imread("C:\\Users\\Dell\\PycharmProjects\\Fundamental\\Session7\\Homework\\[1]_image.png")

# convert Whiter color to black
def Image(a):
    [rows, cols, c] = a.shape
    for i in range(rows):
        for j in range(cols):
            if a[i,j,0] > 200 and a[i,j,1] > 200 and a[i,j,2] > 200:
                a[i,j,:] = 0

Img1 = Image(I1)
# Extract chanel B
B = I1[:,:,0]
# Extract chanel G
G = I1[:,:,1]
# Extract chanel R
R = I1[:,:,2]
thresh,blue = cv2.threshold(B,150,255,cv2.THRESH_BINARY)
thresh, green = cv2.threshold(G, 150, 255, cv2.THRESH_BINARY)
thresh, red = cv2.threshold(R, 150, 255, cv2.THRESH_BINARY)
White = blue|green|red
cv2.imshow("binaryImage1", White)

Img2 = Image(I2)
# Extract chanel B
B = I2[:,:,0]
# Extract chanel G
G = I2[:,:,1]
# Extract chanel R
R = I2[:,:,2]
thresh,blue = cv2.threshold(B,150,255,cv2.THRESH_BINARY)
thresh, green = cv2.threshold(G, 150, 255, cv2.THRESH_BINARY)
thresh, red = cv2.threshold(R, 150, 255, cv2.THRESH_BINARY)
White = blue|green|red
cv2.imshow("binaryImage2", White)
cv2.waitKey()


