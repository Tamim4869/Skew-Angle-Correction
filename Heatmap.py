import matplotlib.pyplot as plt
import numpy as np

image=plt.imread('Rewritten.jpg')

def function(image):
    grayimg=np.dot(image[...,:3],[1/2, 1/4, 1/4])
    return grayimg
gray_image=function(image)

fig, ax= plt.subplots()
im=ax.imshow(gray_image, cmap='rainbow')

cbar = ax.figure.colorbar(im, ax = ax)
cbar.ax.set_ylabel("Color bar", rotation = -90, va = "bottom")

plt.show()









 


