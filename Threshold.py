#Importing the necessary libraries
import numpy as np
import cv2

img = cv2.imread('sudoku.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Conversion to Grayscale is must or these thresholds won't work
_,th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) #Binary threshold

#Adaptive thresholding techniques in which different thresholds values are calculated for different smaller regions.
#This thresholding technique is used when the image has a case of variable lighting conditions in which the simple
#thresholding techniques won't work.
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2) #Mean filter
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2) #Gaussian filter

cv2.imshow('image', img)
cv2.imshow('th1',th1)
cv2.imshow('th2',th2)
cv2.imshow('th3',th3)

cv2.waitKey(0) #The image is closed when a button is pressed.
cv2.destroyAllWindows() #Destroys all the windows