#importing the necessary libraries
import numpy as np
import cv2

#defining a function that does nothing
def nothing(x):
    pass

while(1):
    frame = cv2.imread('balls.jpg')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Converting to coloured image to HSV image

    l_b = np.array([110, 50, 50])
    u_b = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, l_b, u_b) 

    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()