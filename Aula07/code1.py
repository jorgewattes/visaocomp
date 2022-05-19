from cgitb import grey
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

a=cv.imread('Aula07/a.png',cv.IMREAD_GRAYSCALE)
thresh=60
_,a_bin = cv.threshold(a,thresh,255,cv.THRESH_BINARY)
# img_bin = 255 - img_bin
struct_element = np.array([[0,1,0],[1,1,1],[0,1,0]],np.uint8)
print(a_bin.shape)
b=cv.dilate(cv.erode(a_bin,struct_element,iterations=5),struct_element,iterations=5)


c=cv.imread('Aula07/c.png',cv.IMREAD_GRAYSCALE)
thresh=60
_,c_bin = cv.threshold(c,thresh,255,cv.THRESH_BINARY)

d=cv.erode(cv.dilate(c_bin,struct_element,iterations=5),struct_element,iterations=5)


e=d
f=cv.dilate(e,struct_element,iterations=1)-cv.erode(e,struct_element,iterations=1)

# g=d
# h = cv.connectedComponents(g)
# https://www.geeksforgeeks.org/python-opencv-connected-component-labeling-and-analysis/


fig = plt.figure()
ax1 = fig.add_subplot(3,2,1)
ax1.imshow(a_bin,cmap='Greys')
ax2 = fig.add_subplot(3,2,2)
ax2.imshow(b,cmap='Greys')
ax3 = fig.add_subplot(3,2,3)
ax3.imshow(c_bin,cmap='Greys')
ax4 = fig.add_subplot(3,2,4)
ax4.imshow(d,cmap='Greys')
ax5 = fig.add_subplot(3,2,5)
ax5.imshow(e,cmap='Greys')
ax6 = fig.add_subplot(3,2,6)
ax6.imshow(f,cmap='Greys')
plt.show()


# cv.imshow('a',a_bin)
# cv.imshow('b',b)
# cv.imshow('c',c_bin)
# cv.imshow('d',d)
# cv.waitKey(0)
# cv.destroyAllWindows()