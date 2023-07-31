import cv2 as cv

# SIFT & Blob Feature Matcher
sift = cv.SIFT_create()
bf = cv.BFMatcher(cv.NORM_L2, crossCheck=False)

# Loading Images
img1 = cv.imread("../img/Books/book_showcase.jpg")
img2 = cv.imread("../img/Books/book_cover.jpg")

# Resizing
img1 = cv.resize(img1, (0, 0), fx=0.25, fy=0.25)
img2 = cv.resize(img2, (0, 0), fx=0.25, fy=0.25)
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

result_img = cv.drawMatches(img1, kp1, img2, kp2, matches[100:300], img1)
img1 = cv.drawKeypoints(gray1, kp1, img1, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
img2 = cv.drawKeypoints(gray2, kp2, img2, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# cv.imwrite("Output/Descriptor1.jpg", img1)  # save photo
# cv.imwrite("Output/Descriptor2.jpg", img2)  # save photo
# cv.imwrite("Output/SIFT.jpg", result_img)  # save photo

# show image
cv.imshow("Descriptor Image1", img1)
cv.imshow("Descriptor Image2", img2)
cv.imshow("SIFT Image", result_img)
cv.waitKey(0)
