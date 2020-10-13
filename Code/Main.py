
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



raw_image = Input_Output.inputImage("coins.png");

grayScale_image = grayscale(raw_image);

picture = MyTrix(grayScale_image);
      
#turn debug mode off so we don't see what is happening
picture.setDebugMode(False);


blurTransArray = [[0.25,0.25],[0.25,0.25]];

xEdgeDetectArray = [[-1,0,1],[-2,0,2],[-1,0,1]];

yEdgeDetectArray = [[-1,2,-1],[0,0,0],[1,2,1]];

print("Blurring");
picture.transform(blurTransArray,0);

print("xEdge detect");
xEdgeDetectTransformed = picture.calculateTransformation(xEdgeDetectArray,1);
Input_Output.outputImage(xEdgeDetectTransformed);

print("yEdge detect");
yEdgeDetectTransformed = picture.calculateTransformation(yEdgeDetectArray,1);
Input_Output.outputImage(yEdgeDetectTransformed);

picture.array = (xEdgeDetectTransformed + yEdgeDetectTransformed)/2;
picture.updateArraySize();

print("Combined:");
Input_Output.outputImage(picture.array);


print("thresh");
picture.threshold(155);