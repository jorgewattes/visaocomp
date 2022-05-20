import cv2  as cv
import sys
#Acessa a camera
video = cv.VideoCapture(0) 
#Cria o Tracker KCF
tracker = cv.TrackerKCF_create()
#Faz uma leitura inicial
ret,frame = video.read()   
#Cria uma Region of Interest
bbox = cv.selectROI(frame,False) 
tracker.init(frame,bbox)
fourcc=cv.VideoWriter_fourcc(*'XVID')
vid_shape = (frame.shape[1],frame.shape[0])
video_out = cv.VideoWriter('Aula10/video.avi',fourcc,30,vid_shape)

while(True):
    ret,frame = video.read()
    
    ret_tckr, bbox = tracker.update(frame)

    p1 = (int(bbox[0]), int(bbox[1]))
    p2 = (int(bbox[0]+bbox[2]), int(bbox[1] + bbox[3]))

    cv.rectangle(frame, p1, p2, (255,0,0),2,1)

    cv.imshow('Tracking',frame)

    video_out.write(frame)

    k=cv.waitKey(1)&0xff
    if k==27:
        break

video.release()
cv.destroyAllWindows()