
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment      Python Project 1
	Author:         Alec Pannunzio, afpannun@purdue.edu
	Team ID:        LC4-5 
	
Contributors:   Jonathan, jdufresn@purdue.edu
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
from Grayscale import grayscale


def runPicture(fileName,thresh=20,outputFile = "EdgeDetectedImage.png"):
    raw_image = Input_Output.inputImage(fileName);
    
    grayScale_image = grayscale(raw_image);
    
    picture = MyTrix(grayScale_image);
          
    #turn debug mode off so we don't see what is happening
    picture.setDebugMode(False);
    
    
    blurTransArray = [[1,1],[1,1]];
    
    xEdgeDetectArray = [[-1,0,1],[-2,0,2],[-1,0,1]];
    
    yEdgeDetectArray = [[-1,-2,-1],[0,0,0],[1,2,1]];
    
    print("Blurring");
    picture.transform(blurTransArray,0);
    picture.toInt();
    Input_Output.outputImage(picture.array);
    
    
    #pad the array before we do edge detection
    picture.pad(1);
    
    print("xEdge detect");
    xEdgeDetectTransMat = picture.calculateTransformation(xEdgeDetectArray);
    xEdgeDetectTransformed = MyTrix(xEdgeDetectTransMat);
    xEdgeDetectTransformed.toInt();
    
    print(xEdgeDetectTransformed);
    Input_Output.outputImage(xEdgeDetectTransformed.array);
    
    print("yEdge detect");
    yEdgeDetectTransMat = picture.calculateTransformation(yEdgeDetectArray);
    yEdgeDetectTransformed = MyTrix(yEdgeDetectTransMat);
    yEdgeDetectTransformed.toInt();
    
    Input_Output.outputImage(yEdgeDetectTransformed.array);
    
    picture.array = (xEdgeDetectTransformed + yEdgeDetectTransformed);
    picture.updateArraySize();
    
    print("Combined:");
    Input_Output.outputImage(picture.array);
    
    print("enhance")    
    picture.enhance();


    print("thresh");
    picture.threshold(thresh);
    Input_Output.outputImage(picture.array,outputFile);
    
    
    
    print("done");


#runPicture("coins",20,"edgyCoins.png");
#runPicture("Purdue_Arch",5,"edgyArch.png");
runPicture("cheerios.png",5,"edgycheerios.png");
#runPicture("CMOS.png",10,"edgyCMOS.png");
