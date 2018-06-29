import cv2
import numpy as np

# read Image
I1 = cv2.imread("C:\\Users\\Dell\\PycharmProjects\\Fundamental\\Session 8\\1.png")
cv2.imshow("Image 1",I1)
# cv2.waitKey()
#compute SIFT
gray1 = cv2.cvtColor(I1,cv2.COLOR_RGB2GRAY)
sift1 = cv2.xfeatures2d.SIFT_create()
kpt1, des1 = sift1.detectAndCompute(gray1,None)
cv2.drawKeypoints(I1,kpt1,I1)
cv2.imshow("keypoint 1",I1)
cv2.waitKey()

indexgood = -1
max_point = -1
for i in range(1,9):
    file = "C:\\Users\\Dell\\PycharmProjects\\Fundamental\\Session 8\\"+str(i)+".png"
    I2 = cv2.imread(file)
    gray2 = cv2.cvtColor(I2, cv2.COLOR_RGB2GRAY)
    sift2 = cv2.xfeatures2d.SIFT_create()
    kpt2, des2 = sift2.detectAndCompute(gray2,None)

    # Matching Bruce force
    bf = cv2.BFMatcher_create()
    matches = bf.knnMatch(des1,des2,2)
    OutImg = cv2.drawMatchesKnn(I1,kpt1,I2,kpt2, matches, None)
    cv2.imshow("matching",OutImg)
    # cv2.waitKey()

    # Choose match good
    good = []
    for m,n in matches:
        if m.distance <0.7*n.distance:
            good.append([m])
    if len(good)>max_point:
        max_point = len(good)
        indexgood = i
    # OutImg2 = cv2.drawMatchesKnn(I1,kpt1,I2,kpt2,good,None)
    # cv2.imshow("matching good",OutImg2)
    # cv2.waitKey()
# show result
file = "C:\\Users\\Dell\\PycharmProjects\\Fundamental\\Session 8\\"+str(indexgood)+".png"
I2 = cv2.imread(file)
cv2.imshow("best matching",I2)
cv2.waitKey()