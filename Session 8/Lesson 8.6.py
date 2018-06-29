import cv2
import numpy as np

# read Image
I1 = cv2.imread("C:\\Users\\Dell\\PycharmProjects\\Fundamental\\Session 8\\1.png")
cv2.imshow("Image 1",I1)
cv2.waitKey(1)

# anh muon chen
pattern = cv2.imread("C:\\Users\\Dell\\PycharmProjects\\Fundamental\\Session 8\\3.png")
pattern = cv2.resize(pattern,(I1.shape[1],I1.shape[0]))
# tao mask
mask = np.ones_like(I1,dtype = np.float32)
#compute SIFT
gray1 = cv2.cvtColor(I1,cv2.COLOR_RGB2GRAY)
sift1 = cv2.xfeatures2d.SIFT_create()
kpt1, des1 = sift1.detectAndCompute(gray1,None)

cap = cv2.VideoCapture(0)
while True:
    ret,I2 = cap.read()
    gray2 = cv2.cvtColor(I2, cv2.COLOR_RGB2GRAY)
    sift2 = cv2.xfeatures2d.SIFT_create()
    kpt2, des2 = sift2.detectAndCompute(gray2,None)

    # Matching Bruce force
    bf = cv2.BFMatcher_create()
    matches = bf.knnMatch(des1,des2,2)

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

        blendmask = cv2.warpPerspective(mask,M,(I2.shape[1],I2.shape[0]))
        newpattern = cv2.warpPerspective(pattern,M,(I2.shape[1],I2.shape[0]))
        im4 = I2*(1-blendmask) + newpattern
        im4 = cv2.convertScaleAbs(im4)
        cv2.imshow("insert",im4)
        cv2.imshow("result",I2)
        cv2.waitKey(30)
