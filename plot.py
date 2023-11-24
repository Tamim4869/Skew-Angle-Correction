import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np

import os
os.chdir('C:\\Users\Tamim\Stat Project Codes\Input Images')

image=plt.imread('rewritten8.jpg')
def function(image):
    grayimg=np.dot(image[...,:3],[1/2, 1/4 , 1/4])
    return grayimg

newimage=function(image)
(a,b)=newimage.shape
lsy=[]
for i in range(a):
    count=0
    for j in range(b-1):
        if 45 <= abs(newimage[i,j+1]-newimage[i,j]) <= 170 :
            count +=1
    lsy.append(count)
lsx=[n for n in range(a)]
plt.plot(lsx, lsy)
plt.show()
