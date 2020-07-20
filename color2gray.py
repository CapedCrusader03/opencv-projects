#importing the necessary libraries
import numpy as np
import cv2

cv2.namedWindow('image')

#A simple function which prints the current slider position
def sliderValue(x):
    print(x)

#Defining a switch to toggle between RGB/Grayscale image
switch = 'BGR/Gray'
cv2.createTrackbar(switch, 'image', 0, 1, sliderValue)

while(1):
    img = cv2.imread('LM10.jpg') #Loading the image
    img = cv2.resize(img, (700,550)) #Resizing the image

    k = cv2.waitKey(1) & 0xFF
    if k == 27: #If Esc key is pressed, then the frame will be closed
        break
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0: #RGB when slider is on 0
        pass
    else: #Grayscale when slider is on 1
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    img = cv2.imshow('image',img)
cv2.destroyAllWindows() #Destroying all the windows