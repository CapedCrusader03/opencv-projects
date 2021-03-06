# opencv-projects

All the below mini-projects use OpenCV library.

1) Date_time_resolution : This mini-project emphasises on printing the resolution of the camera and the current date and time. 
The original video is in RGB format, but it is converted to grayscale.

2) LeftMouseCallback : This mini-project emphasises on printing the co-ordinates of the points on the image where the left mouse
button is clicked.

3) MouseCallback : The co-ordinates of the points on the image where the left mouse button is clicked is printed in cyan. And if the
right mouse button is clicked, then the BGR co-ordinates of that point is printed in yellow.

4) PolygonFromPoints : If the user clicks anywhere in the image, then that point's co-ordinates are stored. If the user clicks somewhere
else, then the a line is generated between the previous clicked point and the last point. So basically, if there are more than 2 points, then a 
line is generated between the last and the second last points. The lines are drawn in Cyan and the points in red.

5) ColorPicker : This mini-project will pick the color of the image when left mouse button is clicked on the image, and the picked color is shown in 
an another 300 x 300 sized window.

6) ImageMerge : In this mini-project, two images are merged with weights (or transparency) into one single image.

7) bitwise : In this mini-project, bitwise operations are done between two images. The images go through OR, AND, XOR, and NOT operations.
The resultant images appear for a duration of 2 seconds before moving on to the next image.

8) TrackBar : Trackbars are created and the user can use slide them to create an RGB shade of their own choice. Also, a switch has been made to toggle 
whether the user want the change in the image.

9) Color2Gray : A trackbar is used to toggle between RGB image and Grayscale image.

10) ColoredBalls : Out of the many colored balls, only those balls are selected that are of blue color. Basically, a mask is created to do the object dection of blue clored balls. Also, a bitwise AND operation is done on the image to show the blue balls.

11) ColoredMask : This is generalisation of the ColoredBalls project. Here, I have used a mask that can be used to detect objects of the same category(like blue balls or red balls,  etc.). I've used trackbar to do the object detection of user's choice. And then, a res named frame is created which does bitwise AND operation and displays the final output, i.e., colored version of the mask.

12) VideoMask : This is the implementation of ColoredMask project in the video form, i.e. the faces or any other object can be used for object detection using primary camera. 

13) SimpleThresholds : This is used to do some simple threshold operations on images like binary threshold, binary inverse threshold, truncated threshold, to zero threshold, to zero inverse threshold.

14) Threshold : Adaptive threshold is used in this project which helps to do effective thresholding in the images in which there are variable lighting conditions. Mean and gaussian filters are used.

15) PltThreshold : All the threshold operations done in SimpleThreshold are displayed in a single frame using matplotlib.

16) MorphologicalOperations : Some morphological operations like erosion, dilation, opening, closing, top hat are done. These morphological transformations are helpful in removing noise from the input images. All the operations are shown in a single frame usin matplotlib library.

17) SmoothingAndBlurring : Used 2D covolutions, Average blurring and Gaussian blurring to blur and smoothen the image.

18) EdgeDetection : Used sobel filters, canny edge detector adn gaussian blur to detect the edges of the images and displayed all of them in a single frame using matplotlib library

19) ImagePyramid : Used Gaussian pyramids that downscale the image 5 times, where each downscale reduces the size of the image to one-fourth of the previous image

20) ImageBlend : Used Gaussian and Laplacian pyramids to blend two images smoothly. 

21) Contours : Used findcontours method of OpenCV to find the contours. Total no. of contours in are printed and the contours are drawn on the original image.

22) ObjectDetection : Used findContours method to detect all the objects that are moving in the video. Green coloured rectangles are drawn on the objects that are moving. The video has been added on which the object detection is performed. Obviously, the results can be improved by using state-of-the art models like SSD.
