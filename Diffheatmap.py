import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

image=plt.imread('Rewritten.jpg')

def function(image):
    grayimg=np.dot(image[...,:3],[1/2, 1/4 , 1/4])
    return grayimg

newimage= ndimage.rotate(image, angle)
new_image= function(newimage)
(a,b)=new_image.shape
Z=np.zeros((a,b-1))
for i in range(a):
    for j in range(b-1):
        Z[i,j] += abs(new_image[i,j+1]-new_image[i,j])

fig, ax= plt.subplots()
im=ax.imshow(Z, cmap='rainbow')

cbar = ax.figure.colorbar(im, ax = ax)
cbar.ax.set_ylabel("Color bar", rotation = -90, va = "bottom")

plt.show()



