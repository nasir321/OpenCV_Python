import cv2

img = cv2.imread('opencv.png',)
img = cv2.resize(img, (0, 0), fx= 1, fy=1)
#img = cv2.rotate(img, cv2.cv2.ROTATE_180)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyWindow()