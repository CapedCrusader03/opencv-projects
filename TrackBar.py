#importing the necessary libraries
import numpy as np
import cv2

#Creating a black image of size 300 x 512 and contains 3 channels - R,G,B
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

#Function which prints the value of the slider when the trackbar is used
def SliderValue(x):
    print(x)
#Creating the trackbars for B,G and R
cv2.createTrackbar('B', 'image', 0, 255, SliderValue)
cv2.createTrackbar('G', 'image', 0, 255, SliderValue)
cv2.createTrackbar('R', 'image', 0, 255, SliderValue)

#Creating a switch to toggle changing the colour of the image
switch = '0 : OFF\n 1 : ON'
cv2.createTrackbar(switch,'image', 0, 1, SliderValue)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(0) & 0xFF
    if k ==27: #Don't close the image until the Esc key is pressed
        break


    b = cv2.getTrackbarPos('B', 'image') #Get the slider value for B
    g = cv2.getTrackbarPos('G', 'image') #Get the slider value for G
    r = cv2.getTrackbarPos('R', 'image') #Get the slider value for R
    s = cv2.getTrackbarPos(switch, 'image') #Get the slider value for switvh

    if s == 0: #If switch's value is zero, then no the image doesn't change
        img[:] = 0
    else: #If switch's value is one, then the image changes
        img[:] = [b, g, r] #Applying the values of b,g and r obtained from above

cv2.destroyAllWindows() #Destroying all the windows