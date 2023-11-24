import matplotlib.pyplot as plt
import numpy as np

import os
os.chdir('C:\\Users\Tamim\Stat Project Codes\Input Images')


image=plt.imread('rewritten8.jpg')

def rgbtogray(image):
    grayimg=np.dot(image[...,:3],[1/2, 1/4, 1/4])
    return grayimg
gray_image=rgbtogray(image)

fig, ax= plt.subplots()
im=ax.imshow(gray_image, cmap='rainbow')

cbar = ax.figure.colorbar(im, ax = ax)
cbar.ax.set_ylabel("Color bar", rotation = -90, va = "bottom")

plt.show()









 


