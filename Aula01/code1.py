import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('/home/wattes/Dev/visaocomp/visaocomp/Aula03/pompeii.jpeg',cv.IMREAD_UNCHANGED)
print(img)
# cv.imshow('Pompeii ',img[:,:,2])
# cv.waitKey(0)
# cv.destroyAllWindows()
plt.imshow(img,cmap='gray')
plt.colorbar(cmap='gray',fraction=0.03,pad=0.04)
plt.show()
