# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:44:41 2020

@author: jameslong57
"""

# load and display an image with Matplotlib
from matplotlib import image
from matplotlib import pyplot
import numpy as np

im = 255 * image.imread('Coins.PNG')
im = np.around(im)
im = im.astype(int)



def grayscale(im):
    y = 0
    
    #change all channels of R,G,B mat to a brightness value
    for x in range(0,len(im)):
        for i in range(0,len(im[0])):
            y = 0.2126 * im[x,i,0] + 0.7152 * im[x,i,1] + 0.0722 * im[x,i,2]
            im[x,i,0] = y
            im[x,i,1] = y
            im[x,i,2] = y

    print(np.shape(im))
    
    gray = np.zeros((im.shape[0],im.shape[1]))
    print(gray)
    
    print(len(im))
    print(len(im[0]))
    
    
    #convert 3D array to 2D array
    for a in range(0,len(im)):
        for b in range(0,len(im[0])):
            gray[a,b] = im[a,b,0]


    return gray
'''    
x = Grayscale(im)

pyplot.imshow(x)
pyplot.show()
'''