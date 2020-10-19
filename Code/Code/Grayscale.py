# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:44:41 2020

@author: jameslong57
"""

# Import Numpy to gain access to numpy arrays
import numpy as np

#user defined function to grayscale the image
def grayscale(im):
    #define y, which is used as a generic value for the brightness of pixels
    i = 0
    #create a blank 2D array that is the same xy shape as the image
    gray = np.zeros((im.shape[0],im.shape[1]))
    
    #go through every row in the array and go through every column in the array
    #define the grayscale value of each pixel and set the corresponding value in teh blank array equal to the grayscale brightness
    for x in range(0,len(im)):
        for y in range(0,len(im[0])):
            i = 0.2126 * im[x,y,0] + 0.7152 * im[x,y,1] + 0.0722 * im[x,y,2]
            gray[x,y] = i
            
    #Show the user the shape of the image
    print(f'File Shape is {np.shape(im)}')
    

    return gray
  
