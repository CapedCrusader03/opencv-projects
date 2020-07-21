#Importing the necessary libraries
import cv2

img = cv2.imread('sudoku.jpg',0) #Using the grayscale image

_,th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY) #Binary Threshold
_,th2 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV) #Binary Inverse threshold
_,th3 = cv2.threshold(img, 50, 255, cv2.THRESH_TRUNC) #Truncated threshold
_,th4 = cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO)  #To Zero threshold
_,th5 = cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO_INV) #TO zero inverse threshold

cv2.imshow('th1',th1)
cv2.imshow('th2',th2)
cv2.imshow('th3',th3)
cv2.imshow('th4',th4)
cv2.imshow('th5',th5)

cv2.waitKey(0)
cv2.destroyAllWindows()