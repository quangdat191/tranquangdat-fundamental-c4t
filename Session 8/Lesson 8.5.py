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
# cv2.drawKeypoints(I1,kpt1,I1)
# cv2.imshow("keypoint 1",I1)
# cv2.waitKey()

file = "C:\\Users\\Dell\\PycharmProjects\\Fundamental\\Session 8\\"+str(10)+".png"
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
newgood = []
for m,n in matches:
    if m.distance <0.7*n.distance:
        good.append([m])
        newgood.append(m)

# find Homography
srcPoints = np.float32([kpt1[m.queryIdx].pt for m in newgood]).reshape(-1,1,2)
dstPoints = np.float32([kpt2[m.trainIdx].pt for m in newgood]).reshape(-1,1,2)

M,H = cv2.findHomography(srcPoints,dstPoints)
w = gray1.shape[1]
h = gray1.shape[0]
ncorners = np.float32([[0,0],[w-1,0],[w-1,h-1],[0,h-1]]).reshape(-1,1,2)

if M is None:
    print("khong tim duoc Homography")
else:
    # find new corners in homography
    npts = cv2.perspectiveTransform(ncorners,M)
    cv2.polylines(I2,np.int32([npts]),True,(0,0,255))
    cv2.imshow("result",I2)
    cv2.waitKey()
OutImg2 = cv2.drawMatchesKnn(I1,kpt1,I2,kpt2,good,None)
cv2.imshow("matching good",OutImg2)
cv2.waitKey()
