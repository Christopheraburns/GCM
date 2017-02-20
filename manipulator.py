import numpy as np
import cv2

#Load the image first
image = cv2.imread('images/exit-ramp.jpg')
#Convert to grayscale
grImage = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

#Pre-create the window
cv2.namedWindow('master_image')

#parameters
gaussKernel = 3
canny_low = 1
canny_high = 10

def nothing(x):
    pass

def showImage(img):
    cv2.imshow('master_image', img)
    cv2.waitKey(0)


def gaussImage(x):
    # gaussian
    global gaussKernel
    gaussKernel = cv2.getTrackbarPos('Gauss', 'master_image')
    if gaussKernel%2 == 0: #this is an even number - throw it out!
        pass
    else:
        gaussian = cv2.GaussianBlur(grImage,(x,x),0)
        showImage(gaussian)

def cannyImage(x):
    global grImage, canny_low,canny_high
    canny_low = cv2.getTrackbarPos('Canny_Low', 'master_image')
    canny_low = cv2.getTrackbarPos('Canny_High', 'master_image')

    canny = cv2.Canny(grImage, canny_low, canny_high)
    showImage(canny)

#create the Trackbar
cv2.createTrackbar('Gauss', 'master_image', 3, 100, gaussImage)
cv2.createTrackbar('Canny_Low', 'master_image', 1, 150, cannyImage)
cv2.createTrackbar('Canny_High', 'master_image', 50, 300, cannyImage)

showImage(grImage)









