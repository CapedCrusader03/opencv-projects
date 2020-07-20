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

9) Color2Gray : A trackbar is used to toggle between RGB image and Grayscale image
