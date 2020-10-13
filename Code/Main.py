

import MyTrix
import Input_Output
import inputToolbox
from Grayscale import Grayscale



raw_image = Input_Output.inputImage("coins.png");

grayScale_image = Graysale(raw_image);

picture = MyTrix(grayScale_image);
      
#turn debug mode off so we don't see what is happening
picture.setDebugMode(True);


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