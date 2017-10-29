#capture the person who turns on your computer

import cv2
import numpy as np

#capture from camera at location 0
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while (cap.isOpened()):
    ret, frame = cap.read() #capture it frame by frame
    if ret == True:
        
        frame = cv2.flip(frame, 1)
        output.write(frame) 
    
    #display it
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    else:
        break

cap.release()
output.release()
cv2.destroyAllWindows()
