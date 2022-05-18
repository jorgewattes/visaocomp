import cv2 as cv
import numpy as np

img = cv.imread('Aula05/fruits.png',cv.IMREAD_UNCHANGED)
img_hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
#Mask
mask = np.matrix([[0 , 1, 0],[1,-4,1],[0,1,0]],np.float32)

filtered=cv.filter2D(img_hsv[:,:,2],-1,mask)
c=-1
img_hsv[:,:,2] = filtered*c+img_hsv[:,:,2]
img_bgr=cv.cvtColor(img_hsv,cv.COLOR_HSV2BGR)
cv.imwrite('Aula05\output3.jpeg',img_bgr)

filtered_red = cv.filter2D(img[:,:,0],-1,mask)
filtered_green = cv.filter2D(img[:,:,1],-1,mask)
filtered_blue = cv.filter2D(img[:,:,2],-1,mask)
img[:,:,0]=img[:,:,0]+c*filtered_red
img[:,:,1]=img[:,:,1]+c*filtered_green
img[:,:,2]=img[:,:,2]+c*filtered_blue
cv.imwrite('Aula05\output4.jpeg',img)
  
  