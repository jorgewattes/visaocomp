import limiarizacao as lm
import cv2 as cv

image = cv.imread('Aula03/vegies.png',cv.IMREAD_GRAYSCALE)
print(image.shape)
image_bin = lm.limiarizar(image)
cv.imshow('binar',image_bin)
cv.waitKey(0)
cv.destroyAllWindows()