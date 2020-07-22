#Importing the necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('balls.jpg', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 40, 255, cv2.THRESH_BINARY) #Simple threshold operation

kernel = np.ones((2,2), np.uint8) #Defining a kernel

dilation = cv2.dilate(mask,kernel, iterations=2)  #Creates a dilation effect
erosion = cv2.erode(mask, kernel, iterations=1) #Creates an erosion effect
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) #Opening is erosion followed by dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel) #Closing is dilation followed by erosion
morph_grad = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel) #Difference between dilation and erosion
tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel) #Difference between input image and opening

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'morph_gradient', 'top hat'] #Titles for the images
images = [img, mask, dilation, erosion, opening, closing, morph_grad, tophat]

for i in range(8):
    plt.subplot(2,4,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()