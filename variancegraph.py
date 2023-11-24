import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np
from statistics import variance as varn

import os
os.chdir('C:\\Users\Tamim\Stat Project Codes\Input Images')

image=plt.imread('rewritten8.jpg')

def function(image):
    grayimg=np.dot(image[...,:3],[1/2, 1/4 , 1/4])
    return grayimg

def countvar(image, angle, thres1, thres2):
    rotated_image= ndimage.rotate(image, angle)
    grayimg=function(rotated_image)
    (h,w)= grayimg.shape
    ls=[]
    for i in range(h):
        count=0
        for j in range(w-1):
            if thres2 >= abs(grayimg[i, j+1]-grayimg[i,j]) >= thres1:
                count +=1
        ls.append(count)
    var= varn(ls)
    return var
thres1, thres2= 45,170
fnlist=[countvar(image, 0.5*angle, thres1,thres2) for angle in range(0,720)]
lsx=[0.5*n for n in range(0, 720)]

plt.plot(lsx, fnlist)
plt.show()

