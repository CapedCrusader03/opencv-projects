#importing the necessary libraries
import numpy as np
import cv2

#defining a function that does nothing
def nothing(x):
    pass

while(1):
    frame = cv2.imread('balls.jpg') #Reading the image

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Converting to coloured image to HSV image

    l_b = np.array([110, 50, 50]) #The lower bound for the blue color
    u_b = np.array([130, 255, 255]) #Upper bound for the blue color

    mask = cv2.inRange(hsv, l_b, u_b) #Mask that detects only the blue balls

    res = cv2.bitwise_and(frame, frame, mask = mask) #A result frame that does a bitwise and operation on the frame

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27: #The frame will exit if the Esc key is pressed
        break

cv2.destroyAllWindows() #Destroy all the windows