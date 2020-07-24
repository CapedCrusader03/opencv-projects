#Importing the necessary libraries
import cv2
import numpy as np

img = cv2.imread('LM10.jpg')

layer = img.copy() #Creating s copy of the image
gaussianpyramid = [layer]

#Gaussian pyramids
for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussianpyramid.append(layer)
    cv2.imshow(str(i), layer)

cv2.waitKey(0)
cv2.destroyAllWindows() #Destroying all the windows