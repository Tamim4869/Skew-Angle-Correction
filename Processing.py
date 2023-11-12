import matplotlib.pyplot as plt
import numpy as np

def rgbtogray(image):
    grayimg=np.dot(image[...,:3],[0.299, 0.587, 0.114])
    return grayimg

def threshold(image, thres=122):
    img=rgbtogray(image)
    (a,b)=img.shape
    for i in range(a):
        for j in range(b):
            if img[i,j] >= thres:
                img[i,j] =255
            else:
                img[i,j]=0
    return img

def Saveto(image):
    img2=threshold(image)
    plt.imshow(img2, cmap='gray', interpolation='hanning)
    plt.axis('off')
    plt.savefig('rewritten.jpg')
    
    img3=plt.imread('rewritten.jpg')
    return img3




    
