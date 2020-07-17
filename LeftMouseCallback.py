#importing the necessary packages
import cv2
import numpy as np

#defining a click event for the left mouse button
def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:  #Left mouse button event
        print(x, ', ',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x,y), font, 0.5, (255,255,0), 1, cv2.LINE_AA)
        cv2.imshow('image',img)

#Creating a custom image using numpy.
img = np.zeros((512,512,3), np.uint8)  #This creates a black image of 512x512 dimensions
cv2.imshow('image', img)

#Calling the click event
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0) #This makes the frame appear for indefinite time.
cv2.destroyAllWindows() #This destroys all the windows.