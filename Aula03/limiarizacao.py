from cv2 import threshold
import numpy as np

def limiarizar(image):
    threshold=200
    shape = np.shape(image)
    print(shape)
    image_limiarizada = np.zeros(shape)
    for j in range (0, shape[1]):
        for i in range(0,shape[0]):
            if(image[i,j]<threshold):
                image_limiarizada[i,j]=0
            else:
                image_limiarizada[i,j]=255
    # image_limiarizada = (image>=threshold)*255
    return image_limiarizada
