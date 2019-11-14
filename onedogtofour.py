import numpy as np
from functools import reduce
import matplotlib.pyplot as plt

im = plt.imread('dog.jpg')
plt.imshow(im)

print(im.shape)

im2 = im[30:175,20:250]
plt.imshow(im2)
plt.savefig('dog2.jpg')

mim1 = []
mim2 = []
height = im2.shape[1] // 44
for i in range(0,44):
    if not i%2:
        mim1.append(im2[:,height*i:height*(i+1)])
    else:
        mim2.append(im2[:,height*i:height*(i+1)])
        

def pinjie(x,y):
    hnp = np.hstack((x,y))
    return hnp
plt.figure()
plt.subplot(1,2,1)
im6 = reduce(pinjie,mim1)
plt.imshow(im6)
plt.subplot(1,2,2)
im7 = reduce(pinjie,mim2)
plt.imshow(im7)

im8 = np.hstack((im6,im7))
plt.imshow(im8)
plt.savefig('dog8.jpg')


lim1 = []
lim2 = []
weight = im8.shape[0] // 24
for i in range(0,24):
    if not i%2:
        lim1.append(im8[weight*i:weight*(i+1),:])
    else:
        lim2.append(im8[weight*i:weight*(i+1),:])
        
def pinjie(x,y):
    hnp = np.vstack((x,y))
    return hnp
plt.figure()
plt.subplot(2,1,1)
im9 = reduce(pinjie,lim1)
plt.imshow(im9)
plt.subplot(2,1,2)
im10 = reduce(pinjie,lim2)
plt.imshow(im10)


im11 = np.hstack((im9,im10))
plt.imshow(im11)
plt.savefig('dog11.jpg')