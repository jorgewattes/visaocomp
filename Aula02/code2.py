import numpy as np
import math as mt
import cv2 as cv

cap = cv.VideoCapture(-1)
# cap = cv.VideoCapture('videos/example.mp4')
# fps = int(cap.get(cv.CAP_PROP_FPS))
# frames=int(cap.get(cv.CAP_PROP_FRAME_COUNT))

while(True):
    ret,frame = cap.read()

    cv.imshow('Frame',frame)
    if(cv.waitKey(1) & 0xFF ==ord('q')):
        break
cap.release()
cv.destroyAllWindows()