import cv2 as cv
from matplotlib import pyplot as plt
import os

img_bgr = cv.imread('Aula02/vegies.png',cv.IMREAD_UNCHANGED)
img_hsb = cv.cvtColor(img_bgr, cv.COLOR_BGR2HSV)
img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)
img_gray = cv.cvtColor(img_bgr, cv.COLOR_BGR2GRAY)
_,img_bin = cv.threshold(img_gray,127,255,cv.THRESH_BINARY)

# print(img)
# print(type(img))
# print(img.shape)
# print(img.dtype)

fig = plt.figure()
ax1 = fig.add_subplot(3,2,1)
ax1.imshow(img_rgb)
ax2 = fig.add_subplot(3,2,2)
ax2.imshow(img_bgr)
ax3 = fig.add_subplot(3,2,3)
ax3.imshow(img_hsb)
ax4 = fig.add_subplot(3,2,4)
ax4.imshow(img_gray,cmap='gray')
ax4 = fig.add_subplot(3,2,5)
ax4.imshow(img_bin,cmap='gray')


# cv.imshow('Vegies ',img[:,:,0])
# cv.waitKey(0)
# cv.imshow('Vegies ',img[:,:,1])
# cv.waitKey(0)
# cv.imshow('Vegies ',img[:,:,2])
# cv.waitKey(0)
# cv.destroyAllWindows()

fig.savefig('Aula02/colors_space.png',dpi=300,bbox_inches='tight')
plt.show()
