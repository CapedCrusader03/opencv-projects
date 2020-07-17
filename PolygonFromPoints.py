#importing the necessary packages
import numpy as np
import cv2

#defining the click event for the left mouse button
def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 3, (0,0,255),3,cv2.LINE_AA) #Considering points as small circles of radius 3
        points.append((x,y)) #Appending the clicked points in the list
        if len(points) >=2 :  #If there are more than or equal to 2 points, then a line is drawn between the last and the second last points.
            cv2.line(img, points[-1], points[-2], (255,255,0), 3)
        cv2.imshow('image',img)

points = [] #initialising the list where all the clicked points will be saved

#Creating a black image of size 512x512
img = np.zeros((512,512,3), np.uint8)
cv2.imshow('image',img)

#Calling the click event
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0) #Ensuring that the frame won't close until a key is pressed
cv2.destroyAllWindows() #Destroying all the windows.