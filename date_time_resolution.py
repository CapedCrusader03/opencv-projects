import cv2
import datetime
cap = cv2.VideoCapture(0)

cap.set(3, 700)
cap.set(4, 700)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        txt = 'Width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4)) + ' Time :' + str(datetime.datetime.now())
        hw = cv2.putText(gray, txt, (10,50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1, cv2.LINE_AA)
        cv2.imshow('live_stream',hw)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()