import cv2 as cv
import time

# SIFT & Blob Feature Matcher
sift = cv.SIFT_create()
bf = cv.BFMatcher(cv.NORM_L2, crossCheck=True)

cap = cv.VideoCapture(0)
cap1 = cv.VideoCapture('') # Put IP camera address or 1 for second camera

while cap.isOpened():
    status, img1 = cap.read()
    stat, new = cap1.read()
    img2 = new

    start = time.time()

    # Resizing
    img1 = cv.resize(img1, (680, 440))
    img2 = cv.resize(img2, (680, 440))
    # img2 = cv.resize(img2, (0, 0), fx=0.55, fy=0.55)

    # Color Conversion
    gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

    # keypoints & descriptors
    kp1, des1 = sift.detectAndCompute(gray1, None)
    kp2, des2 = sift.detectAndCompute(gray2, None)

    # Descriptor Matching
    matches = bf.match(des1, des2)
    matches = sorted(matches, key = lambda x:x.distance)


    end = time.time()
    totalTime = end - start

    fps = 1 / totalTime

    result_img = cv.drawMatches(img1, kp1, img2, kp2, matches[400:600], img1)
    
    cv.imshow("SIFT Image", result_img)
    if cv.waitKey(5) & 0xFF == 27:
        break
    
cap.release()
