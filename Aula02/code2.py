import numpy as np
import math as mt
import cv2 as cv

cap = cv.VideoCapture(-1)
# cap = cv.VideoCapture('videos/example.mp4')
# fps = int(cap.get(cv.CAP_PROP_FPS))
# frames=int(cap.get(cv.CAP_PROP_FRAME_COUNT))

ret,frame = cap.read()
cv.imshow('Frame',frame)

# while(True):
#     ret,frame = cap.read()

#     cv.imshow('Frame',frame)
cap.release()
cv.destroyAllWindows()