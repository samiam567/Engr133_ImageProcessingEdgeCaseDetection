'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment      Python Project 1
	Author:         Jonathan Dufresne, jdufresn@purdue.edu
	Team ID:        LC4-5 
	
Contributors:   Alec, afpannun@purdue.edu
                Sam, graha205@purdue.edu
                James, long365@purdue.edu
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

from MyTrix import MyTrix
import Input_Output
from inputToolbox import getIntegerFromUser
from Grayscale import grayscale
from matplotlib import pyplot


def runPicture(fileName,thresh=20,outputFile = "EdgeDetectedImage.png"):

    raw_image = Input_Output.inputImage(fileName);
    pyplot.figure(1)
    pyplot.imshow(raw_image)
    grayScale_image = grayscale(raw_image);
    
    
    
    '''
    NOTE: Not all methods in MyTrix are used. The ones that are used are outlined in the flowcharts
    '''   
    picture = MyTrix(grayScale_image); 
    
    
    '''
    these are the matrices for the transformations that we do
    '''
    blurTransArray = [[1,1],[1,1]];
    
    xEdgeDetectArray = [[-1,0,1],[-2,0,2],[-1,0,1]];
    
    yEdgeDetectArray = [[-1,-2,-1],[0,0,0],[1,2,1]];
    
    
    
    print("Blurring");
    picture.transform(blurTransArray,0);
    picture.toInt();
    pyplot.figure(2)
    Input_Output.outputImage(picture.array);
    
    
    print("Enchancing")
    picture.enhance(10);
    pyplot.figure(3)
    Input_Output.outputImage(picture.array);
    
    
    #pad the array before we do edge detection
    picture.pad();
    
    print("X Edge Detection");
    xEdgeDetectTransMat = picture.calculateTransformation(xEdgeDetectArray);
    xEdgeDetectTransformed = MyTrix(xEdgeDetectTransMat);
    xEdgeDetectTransformed.toInt();
    pyplot.figure(4)
    Input_Output.outputImage(xEdgeDetectTransformed.array);

    print("Y Edge Detection");
    yEdgeDetectTransMat = picture.calculateTransformation(yEdgeDetectArray);
    yEdgeDetectTransformed = MyTrix(yEdgeDetectTransMat);
    yEdgeDetectTransformed.toInt();
    pyplot.figure(5)
    Input_Output.outputImage(yEdgeDetectTransformed.array);
    
    picture.array = (xEdgeDetectTransformed + yEdgeDetectTransformed);
    
    print("Combining");
    pyplot.figure(6)
    Input_Output.outputImage(picture.array);
    
    
    print("Thresholding");
    picture.threshold(thresh);
    pyplot.figure(7)
    Input_Output.outputImage(picture.array,outputFile);
    
    print("Done");

runPicture(input("What is the fileName?"),getIntegerFromUser("What threshold do you want to use? (must be between 0 and 255 to do anything) ","threshold must be a valid integer between 0 and 255 to do anything "),input("What fileName do you want to output the file to?"));
#runPicture("coins",20,"edgyCoins.png");
#runPicture("Purdue_Arch",8,"edgyArch.png");
#runPicture("cheerios.png",5,"edgycheerios.png");
#runPicture("CMOS.png",15,"edgyCMOS.png");