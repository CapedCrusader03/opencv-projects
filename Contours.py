#Import the necessary libraries
import cv2

img = cv2.imread('OpenCV_Logo.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,127,255,0) #Set threshold
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #Find the contours
print("No. of contours = " + str(len(contours)))
print(contours[0])

cv2.drawContours(img, contours, -1, (100,200,255), 3) #Draw the contours

cv2.imshow('Image', img)
#cv2.imshow('Image GRAY', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()