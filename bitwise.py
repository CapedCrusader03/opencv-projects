#importing the necessary libraries
import numpy as np
import cv2

#reading the images
img1 = cv2.imread('LM10.jpg')
img2 = cv2.imread('OpenCV_Logo.png')

#Resizing the images to the same size
img1 = cv2.resize(img1, (700,550))
img2 = cv2.resize(img2,(700,550))

#Bitwise OR operation
bitOr = cv2.bitwise_or(img1,img2)
cv2.imshow('bitOr', bitOr)
cv2.waitKey(2000)
cv2.destroyAllWindows()

#Bitwise AND operation
bitAnd = cv2.bitwise_and(img1, img2)
cv2.imshow('bitAnd', bitAnd)
cv2.waitKey(2000)
cv2.destroyAllWindows()

#Bitwise XOR operation
bitXor = cv2.bitwise_xor(img1, img2)
cv2.imshow('bitXor', bitXor)
cv2.waitKey(2000)
cv2.destroyAllWindows()

#Bitwise NOT operations on both the images
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)
cv2.imshow('bitNot1', bitNot1)
cv2.waitKey(2000)
cv2.destroyAllWindows()
cv2.imshow('bitNot2', bitNot2)
cv2.waitKey(2000)
cv2.destroyAllWindows()
