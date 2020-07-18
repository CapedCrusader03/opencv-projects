#importing the necessary packages
import numpy as np
import cv2

#defining the click event for the left mouse button for picking color
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        cv2.circle(img, (x,y), 3, (0,0,255),-1, cv2.LINE_AA)
        mycolorImage = np.zeros((300,300,3), np.uint8)

        mycolorImage[:] = [blue,green,red]

        cv2.imshow('PickedColor',mycolorImage)

#Reading the image
img = cv2.imread('LM10.jpg')
cv2.imshow('image',img)

#Calling the click event
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0) #Ensuring that the frame won't close until a key is pressed
cv2.destroyAllWindows() #Destroying all the windows.
