import cv2 as cv
import numpy as np

img = cv.imread('Aula05\pompeii.jpeg',cv.IMREAD_UNCHANGED)

#Mask
mask = np.matrix([[0 , 1, 0],[1,-4,1],[0,1,0]],np.float32)

filtered=cv.filter2D(img.astype(np.float32),-1,mask)
c=-1
enhanced = filtered*c+img
cv.imwrite('Aula05\output2.jpeg',enhanced)
