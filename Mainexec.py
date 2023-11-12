from Processing import *

import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np
from statistics import variance as varn
import time


start=time.time()

image=plt.imread('barcode3.jpg')

binary_image= Saveto(image)

def tobw(image):
    return np.dot(image[...,:3], [1/2, 1/4, 1/4])

img4=tobw(binary_image)
(a,b)=img4.shape

def countvar(image, angle, thres1, thres2):
    rotimage= ndimage.rotate(image, angle)
    (h,w)= rotimage.shape
    ls=[]
    for i in range(h):
        count=0
        for j in range(w-1):
            if thres2 >= abs(rotimage[i, j+1]-rotimage[i,j]) >= thres1:
                count +=1
        ls.append(count)
    var= varn(ls)
    return var

thres1,thres2= 60,130
fnlist=[countvar(img4, 0.5*angle, thres1,thres2) for angle in range(0,360)]
B=min(fnlist)
m= 0.5*fnlist.index(B)

def adjust(angle):
    if angle >90:
        return angle-90
    else:
        return angle +270

fig, ax = plt.subplots(ncols=2, figsize=(20, 20))
ax[0].imshow(image, cmap='gray')
ax[1].imshow(ndimage.rotate(image, adjust(m)), cmap='gray')
plt.show()

end=time.time()
    
print('Skew about the positive X-axis is about :', 90-m, 'degrees')

print(end-start)
