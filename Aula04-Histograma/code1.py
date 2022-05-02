import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import htgm


# data=np.array([1,2,3,5,4,4,4,2,2,3,4,5])
# htgm.histogram(data)

cap = cv.VideoCapture(-1)
ret,frame = cap.read()
while(True):
    ret,frame = cap.read()
    plt.close()
    # htgm.clrHistogram(frame)
    cv.imshow('Frame',frame)
    # plt.figure('Cam')
    # plt.imshow(frame)
    # plt.show()
    # plt.pause(0.0001)
    if(cv.waitKey(1) & 0xFF ==ord('q')):
        #Printar ao quitar
        htgm.clrHistogram(frame)
        cv.imwrite('Aula04/print.png',frame)
        break
htgm.clrHistogram(frame)
cap.release()
cv.destroyAllWindows()