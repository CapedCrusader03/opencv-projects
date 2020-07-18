# opencv-projects

All the below mini-projects use OpenCV library for this purpose.

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
