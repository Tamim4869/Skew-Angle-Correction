import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from statistics import variance as varn
import time

start=time.time()

def triplet(a,b,c, thres):
    if a >= thres and b >= thres and c >= thres:
        return 1
    else:
        return 0

image=plt.imread('barcode34.png')

p,q,r=image.shape
Z=np.zeros((p,q), dtype=np.int32)
for i in range(p):
    for j in range(q):
        Z[i,j] +=triplet(image[i,j][0], image[i,j][1], image[i,j][2], 0.560784)

plt.imshow(Z, cmap='gray', interpolation='hanning')
plt.axis('off')
plt.savefig('Rewritten.png', bbox_inches='tight', pad_inches=0)

img=plt.imread('Rewritten.png')

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

thres1,thres2= 0.1647, 0.68627
fnlist=[countvar(img, 0.5*angle, thres1,thres2) for angle in range(0,360)]
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


