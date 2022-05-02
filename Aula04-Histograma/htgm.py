import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

def histogram(data):
    shape=data.shape
    if(len(shape)==1):
        x=np.unique(data)
        print(x)
        y=np.zeros(x.shape[0])
        print(y)
        for j in range (0,shape[0]):
            y[np.where(x==data[j])]+=1
        print(y)
    # fig, ax = plt.subplots()
    plt.bar(x,y,width=0.2, color="#FFFF00")
    plt.show()
    return [x,y]

def clrHistogram(image):
    image_hsb=cv.cvtColor(image,cv.COLOR_BGR2HSV)
    shape=image.shape
    # print(shape)
    pixels = [0]*(shape[0]*shape[1])
    pixels_hsb = np.zeros(shape[0]*shape[1])
    # print(pixels_hsb.shape)
    for j in range (0, shape[1]):
        for i in range(0,shape[0]):
            pixels[i+j*shape[0]]=f'#{image[i,j,0]:x}{image[i,j,1]:x}{image[i,j,2]:x}'
            pixels_hsb[i+j*(shape[0]-1)]=image_hsb[i,j,1]
    x=np.unique(pixels_hsb)
    # print(x.shape)
    y=np.zeros(x.shape[0])
    # print(y.shape)
    for j in range (0,pixels_hsb.shape[0]):
        
        # print(np.where(x==pixels_hsb[j])[0][0])
        y[np.where(x==pixels_hsb[j])[0][0]]+=1
    y=100*y/(shape[0]*shape[1])
    fig=plt.figure('Histograma')

        # redraw the canvas
    fig.canvas.draw()

    # convert canvas to image
    img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8,
            sep='')
    img  = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    # img is rgb, convert to opencv's default bgr
    img = cv.cvtColor(img,cv.COLOR_RGB2BGR)
    plt.bar(x,y)
    # plt.show()
    # plt.pause(0.0001)
    cv.imshow('Histograma',img)
    # print(pixels)
    # print(pixels_hsb)
    # return [x,y]
