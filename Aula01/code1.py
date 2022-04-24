import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('Aula01/pompeii.jpeg',cv.IMREAD_UNCHANGED)
print(img)
print(type(img))
print(img.shape)
print(img.dtype)
# cv.imshow('Pompeii ',img[:,:,2])
# cv.waitKey(0)
# cv.destroyAllWindows()
plt.imshow(img[:,:,0],cmap='gray')
plt.colorbar(cmap='gray',fraction=0.03,pad=0.04)
plt.show()

