import cv2 as cv
import numpy as np

img = cv.imread('Aula05\pompeii.jpeg',cv.IMREAD_UNCHANGED)

#Mask
mask = np.matrix([[1 , 1, 1],[1,1,1],[1,1,1]],np.float32)/9

filtered=cv.filter2D(img,-1,mask)

cv.imwrite('Aula05\output1.jpeg',filtered)
