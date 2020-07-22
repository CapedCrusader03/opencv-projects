#Importing the necessary libraries
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('sudoku.jpg')

_,th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY) #Binary Threshold
_,th2 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV) #Binary Inverse threshold
_,th3 = cv2.threshold(img, 50, 255, cv2.THRESH_TRUNC) #Truncated threshold
_,th4 = cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO)  #To Zero threshold
_,th5 = cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO_INV) #TO zero inverse threshold

titles = ['Original image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TO_ZERO', 'TO_ZERO_INV'] #Titles for each thresholds
images = [img,th1,th2,th3,th4,th5] #The image list which contains original and all the threshold images

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([]) #Removing labels from X and Y axes

plt.show()
