#importin the necessary libraries
import numpy as np
import cv2

#Defining a function that does nothing
def nothing(x):
    pass

cv2.namedWindow('Tracker') #The window which contains all the sliders
cv2.createTrackbar('Lower Hue','Tracker',0,255,nothing)
cv2.createTrackbar('Lower Saturation','Tracker',0,255,nothing)
cv2.createTrackbar('Lower Value','Tracker',0,255,nothing)
cv2.createTrackbar('Upper Hue','Tracker',255,255,nothing)
cv2.createTrackbar('Upper Saturation','Tracker',255,255,nothing)
cv2.createTrackbar('Upper Value','Tracker',255,255,nothing)

while(1):
    frame = cv2.imread('balls.jpg')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_h = cv2.getTrackbarPos("Lower Hue", "Tracker")
    lower_s = cv2.getTrackbarPos("Lower Saturation", "Tracker")
    lower_v = cv2.getTrackbarPos("Lower Value", "Tracker")

    upper_h = cv2.getTrackbarPos("Upper Hue", "Tracker")
    upper_s = cv2.getTrackbarPos("Upper Saturation", "Tracker")
    upper_v = cv2.getTrackbarPos("Upper Value", "Tracker")

    lower_b = np.array([lower_h,lower_s,lower_v])
    upper_b = np.array([upper_h, upper_s, upper_v])

    mask = cv2.inRange(hsv, lower_b, upper_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:  # The frame will exit if the Esc key is pressed
        break

cv2.destroyAllWindows()  # Destroy all the windows