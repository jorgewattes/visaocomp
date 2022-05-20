import cv2  as cv
import numpy as np

import sys

video = cv.VideoCapture(0)

tracker = cv.TrackerKCF_create()
ret,frame = video.read()
bbox = cv.selectROI(frame,False)
p1 = (int(bbox[0]), int(bbox[1]))
p2 = (int(bbox[0]+bbox[2]), int(bbox[1] + bbox[3]))
roi = frame[p1[0]:p2[0],p1[1]:p2[1]]
hsv_roi = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

h_min = 0.
h_max = 25.
s_min=80.
v_min=80.

mask =  cv.inRange(hsv_roi,np.array((h_min,s_min,v_min)),np.array((h_max,255.,255.)))


# tracker.init(frame,bbox)
roi_hist = cv.calcHist([hsv_roi],[0],mask,[190],[0,180])
cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)

term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT,10,1)


fourcc=cv.VideoWriter_fourcc(*'XVID')
vid_shape = (frame.shape[1],frame.shape[0])
video_out = cv.VideoWriter('Aula10/video2.avi',fourcc,30,vid_shape)

while(True):
    ret,frame = video.read()
    
    # ret_tckr, bbox = tracker.update(frame)

    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    dst = cv.calcBackProject([hsv],[0],roi_hist,[0,180],1)
    print(dst.shape)
    ret,bbox = cv.CamShift(dst,bbox,term_crit)

    pts = cv.boxPoints(ret)
    pts = np.int0(pts)
    fram = cv.polylines(frame,[pts],True,255,2)

    cv.imshow('Tracking',frame)
    cv.imshow('dst',dst)
    video_out.write(frame)

    k=cv.waitKey(1)&0xff
    if k==27:
        break

video.release()
cv.destroyAllWindows()