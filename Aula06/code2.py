import cv2 as cv
import numpy as np

img=cv.imread('Aula06/fruits.png',cv.IMREAD_UNCHANGED)
img_hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)

# img_h=img_hsv[:,:,0]
# img_s=img_hsv[:,:,1]
# img_v=img_hsv[:,:,2]

# img_hsv_thr=img_hsv
# img_hsv_thr=[:,:,0]
shape=img_hsv.shape
img_bin=np.zeros(shape[0:2])
for j in range(0,shape[1]):
    for i in range(0,shape[0]):
        if(img_hsv[i,j,0]>20 
        and img_hsv[i,j,0]<78
        and img_hsv[i,j,1]>50
        and img_hsv[i,j,2]>50):
            img_bin[i,j]=1
        else:
            img_bin[i,j]=0

img_new=img
for j in range(0,shape[1]):
    for i in range(0,shape[0]):
        if(img_bin[i,j]==1):
            img_new[i,j,:]=img[i,j,:]
        else:
             img_new[i,j,:]=0

# _,img_bin = cv.threshold(img,127,255,cv.THRESH_BINARY)
# img_bin = 255 - img_bin

cv.imshow('Thresh',img_new)
cv.waitKey(0)
cv.destroyAllWindows()