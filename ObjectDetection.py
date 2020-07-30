#Import the necessary libraries
import cv2

cap = cv2.VideoCapture('funny_dog.mp4') #Reading the video

ret,frame1 = cap.read() #read the frames of the video
ret,frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1,frame2) #Find the difference between the two frames
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) #Convert the frames to Grayscale
    blur = cv2.GaussianBlur(gray, (5,5), 0) #Applying Gaussian blur
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) #Adding threshold
    dilated = cv2.dilate(thresh, None, iterations=3) #Dilating
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #Finding the contours

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour) #Get the x,y, width, height of the contour

        if cv2.contourArea(contour) < 10000:
            continue #if the area enclosed by th contour is less than 10000, then don't do anything
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0, 255, 0), 2) #Else draw a rectangle around the contour
        cv2.putText(frame1, "Status{}".format('Moving'), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3) #if the object is moving, then show the status as moving

    #cv2.drawContours(frame1, contours, -1, (0,255,0), 2)

    cv2.imshow("feed", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(20) == 27: #If the Esc key is pressed, then close the window
        break

cv2.destroyAllWindows()
cap.release()