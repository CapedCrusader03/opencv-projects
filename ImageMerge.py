#Importing the necessary libraries
import cv2

#Reading the two images
img = cv2.imread('LM10.jpg')
img2 = cv2.imread('OpenCV_Logo.png')

#Resizing both the images to the same size so that geometrical transformations can be made on them
img = cv2.resize(img, (700,550))
img2 = cv2.resize(img2, (700,550))

#Adding both the images using weights
dst = cv2.addWeighted(img, 0.7, img2, 0.3, 0)

cv2.imshow('image',dst) #Showing the resultant image
cv2.waitKey(0) #Ensuring that the frame won't close until a key is pressed
cv2.destroyAllWindows() #Destroying all the windows