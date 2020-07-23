#Imported the necessary libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('sudoku.jpg', cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize = 3) #Remove noise by applying a Gaussian blur
lap = np.uint8(np.absolute(lap))
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0) #Sobel X filter
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1) #Sobel Y filter
Canny = cv2.Canny(img, 100, 200) #Canny edge detector

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY) #Combined sobel x and sobel y filters to detect horizontal and vertical edges

titles = ['image', 'Laplacian', 'SobelX', 'SobelY', 'SobelCombined', 'Canny']

images = [img,lap,sobelX,sobelY,sobelCombined, Canny]
for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()