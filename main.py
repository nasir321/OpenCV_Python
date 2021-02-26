#pip install opencv_python
#must install openCV library before run.
import cv2

img = cv2.imread('opencv.png',) #load or read image
img = cv2.resize(img, (0, 0), fx= 1, fy=1) #resize image 
img = cv2.rotate(img, cv2.cv2.ROTATE_180) #Rotate image as per need
cv2.imshow('Image', img) #Show image on screen
cv2.waitKey(0)
cv2.destroyWindow()
