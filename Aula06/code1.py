import cv2 as cv
import numpy as np

img=cv.imread('Aula06\pepitas.png',cv.IMREAD_GRAYSCALE)
_,img_bin = cv.threshold(img,127,255,cv.THRESH_BINARY)
img_bin = 255 - img_bin

cv.imshow('Thresh',img_bin)
cv.waitKey(0)
cv.destroyAllWindows()