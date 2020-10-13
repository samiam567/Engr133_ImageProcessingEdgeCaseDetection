
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Python Project 1
	Author:         Sam Graham, graha205@purdue.edu
	Team ID:        LC4-05
	
Contributors: jdufres@purdue.edu, long365@purdue.edu, afpannun@purdue.edu
	My contributor(s) helped me:	
	[ ] understand the assignment expectations without
		telling me how they will approach it.
	[ ] understand different ways to think about a solution
		without helping me plan my solution.
	[ ] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================
'''
import numpy as np #Importing numpy for matrix use
from matplotlib import image #Importing the functinos of matplotlib that can transform an image into a matrix and back again along with other various functions
from matplotlib import pyplot #Importing the functions from matplotlib that allow us to plot the image in Spyder
import sys #Imports sys so that we can exit the code upon an error occuring
def inputImage(s= input("Enter png name here:")):
    try: #Tries the following line of code and if an exception or error is returned then it moves on to the code under except
        imMat = image.imread(s) #The imread function transforms an inputed image into a 3d matrix where each [x][y] is home to a list of 3 values from 0-1 representing RGB values
    except FileNotFoundError: #This is where the errors are handled, tests to see if user forgot ".png", and if the file cannot be found, then it returns an error message
        try:
            s = (s+".png")
            imMat = image.imread(s)
        except FileNotFoundError:
            print("[Error]:file not found, look in directory or re-check spelling")
            sys.exit()
    imMat = imMat * 255 #Multiplies the 3rd dimension of the matrix (the one containing the 0-1 float RGB values) by 255 for later integer conversion
    imMat = np.around(imMat) #Rounds the RBG values to the nearest whole number, still returns values as floats
    imMat = imMat.astype(int) #Transforms the rounded float RGB values to integers
    return imMat #Returns the matrix containing the image information

def outputImage(s):
    s = s/255.0 #the functions imsave and imshow are finiky around int RGB values, so it's overall easier to simply transform the inputed matrix back into 0-1 float values
    image.imsave("EdgeDectedImage.png",s) #Uses the given matrix of dimensions [x][y][z] to write an image file that is x pixels wide by y pixels tall with color at each pixel determines by the RGB values in z
    pyplot.imshow(s) #Similar to imsave however instead of writing it to a file, imshow displays the inputed matrix as an image in the "Plots" tab
    
s = inputImage()
outputImage(s)
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''

