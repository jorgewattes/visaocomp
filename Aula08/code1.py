import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('Aula08\pompeii.jpeg',cv.IMREAD_UNCHANGED)

img_borders=cv.Canny(img,100,200)

fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax1.imshow(img,cmap='Greys')
ax2 = fig.add_subplot(1,2,2)
ax2.imshow(img_borders,cmap='Greys')
plt.show()