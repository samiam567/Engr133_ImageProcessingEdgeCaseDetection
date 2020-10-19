
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Python Project 1
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


import numpy as np
from math import floor

class MyTrix():
    def __init__(self,array, largestValueAllowed = 255): #initialize a new MyTrix object with a numpy array 
            
        if not (type(array) is np.ndarray): #make sure the user entered in an array we can work with
                raise TypeError("MyTricks must be initialized with a numpy array");
        else:
            # store the passed array as one of our class members
            # self.array is the main data that this class will work with
            self.array = array;
            
            # debug mode is whether or not we should output verbose updates
            self.debugMode = False; 
            
            #the largest value we want elements of this array to have on transformations
            self.largestValueAllowed = largestValueAllowed; 
    
    # just a different way of accessing an element in the array
    def at(self,i,j): 
       return self.array[i][j];
    
    def __str__(self):
        return str(self.array);
    
    def __getitem__(self,key):
        return self.array[key];
    
    def __add__(self,addPic): #adds to MyTrixes together
        
        # make sure addPic is another MyTrix
        try:
            addMat = addPic.array;
        except TypeError:
            print("Cannot add type", type(addPic), "and Picture");
            
            
        #figure out which matrix is smaller and limit the indices accordingly
        if (len(self.array) < len(addMat)):
            rowLimit = len(self.array);
        else:
            rowLimit = len(addMat);    
        
        if (len(self.array[0]) < len(addMat[0])):
            columnLimit = len(self.array[0]);
        else:
            columnLimit = len(addMat[0]);
            
            
            
        #create an output array with the smaller of the two mat's dimensions
        outMat = np.empty((rowLimit,columnLimit));
            
        for rowIndx in range(0,rowLimit):
            for columnIndx in range(0,columnLimit):
                outMat[rowIndx][columnIndx] = (self.array[rowIndx][columnIndx] + addMat[rowIndx][columnIndx])/2;
        return outMat;

    #sets whether to give verbose progress logs or not
    def setDebugMode(self, debugMode):
        self.debugMode = debugMode;
    
    #returns a copy of the array    
    def getArrayCopy(self):
        return np.arrCopy(self.array);
        
        
    #converts all of the elements of the matrix to integers
    def toInt(self):
        self.array = self.array.astype(int);
        return self.array;
        
    #will make all values smaller than the threshold lowVal and larger than threshold highVal
    def threshold(self,thresh = 155, highVal = 255,lowVal = 0):
        
        # iterate through all of the elements
        for rowIndx in range(0,len(self.array)):
            for columnIndx in range(0,len(self.array[0])):
                
                
                if (self.array[rowIndx][columnIndx] >= thresh): 
                    # if this element is larger than the threshold then set it to highval
                    self.array[rowIndx][columnIndx] = highVal;
                else: 
                    #otherwise set it to lowVal
                    self.array[rowIndx][columnIndx] = lowVal;
                    
                    
    #will make all values smaller than the threshold lowVal and larger than threshold highVal
    def enhance(self, threshold):
  
        # iterate through all of the elements
        for rowIndx in range(0,len(self.array)):
            for columnIndx in range(0,len(self.array[0])):

                if (self.array[rowIndx][columnIndx] < threshold): 
                    self.array[rowIndx][columnIndx] = int((self.array[rowIndx][columnIndx])/2);

    #initializes the process of parcing through the MyTrix by sub-matricies of the specified size
    def startSubMatrixAquisition(self,rowSize, columnSize, stride=1):
        
        # set the settings members for the subMatrix aquisition to what was passed into the function
        self.subRowSize = rowSize;
        self.subColumnSize = columnSize;
        
        self.stride = stride; # stride is how many elements we iterate each subMatrix
        
        
        
        # bring the iteration variables back to their starting position
        self.subRowIndx = 0; 
        self.subColumnIndx = -1; #we start at -1 because we increment the indeces at the start of the nextSubMatrix method
        
      
        
    # will return the next submatrix of the specified size. (startSubMatrixAquisition() must be called before this method for it to work properly)
    def nextSubMatrix(self):
        
        #advance to the next subMatrix indices
        if ((self.subColumnIndx*self.stride) + self.subColumnSize < len(self.array[0])): #have we gone to the end of this row?
                self.subColumnIndx += 1; #advance to the next column in this row
        
        elif ( (self.subRowIndx*self.stride) + self.subRowSize < len(self.array)): #have we done all of the rows?
            self.subColumnIndx = 0; #go to the first column
            self.subRowIndx += 1; #advance to the next row
        else:
            return None;
                
            
        #create the submatrix to fill with values    
        subMatrix = np.zeros((self.subRowSize,self.subColumnSize));
        
        
        try:
            #determine where to start grabbing values from the our matrix
            startRowIndx = self.subRowIndx * self.stride;
            startColumnIndx = self.subColumnIndx * self.stride; 
            
            #fill the submatrix with our matrix's values
            for relativeRowIndx in range(0,self.subRowSize):
                for relativeColumnIndx in range(0,self.subColumnSize):
                    subMatrix[relativeRowIndx][relativeColumnIndx] = self.at(startRowIndx + relativeRowIndx, startColumnIndx + relativeColumnIndx);

        except IndexError:
            print("index error (nextSubMatrix)");
            pass;
            
        return subMatrix;
    
    
    def replaceSubMatrix(self,newArray):
        
        try: 
            #calculate where the matrix to replace will start
            startRowIndx = self.subRowIndx * self.subRowSize;
            startColumnIndx = self.subColumnIndx * self.subColumnSize; 
            
            
            #figure out which matrix is smaller and limit the indices accordingly
            if (self.subRowSize < len(newArray)):
                rowLimit = self.subRowSize;
            else:
                rowLimit = len(newArray);
                
            if (self.subColumnSize < len(newArray[0])):
                columnLimit = self.subColumnSize;
            else:
                columnLimit = len(newArray[0]);
            
            for relativeRowIndx in range(0,rowLimit):
                for relativeColumnIndx in range(0,columnLimit):
                    self.array[startRowIndx + relativeRowIndx][startColumnIndx + relativeColumnIndx] = newArray[relativeRowIndx][relativeColumnIndx];
                  
                relativeColumnIndx = 0;

        except IndexError:
            print("index error (replaceSubMatrix)");
            
    # pads this array by adding [padding] layers of zeros around it 
    def pad(self,padding = 1):
        if (padding > 0):
            
            #create an output matrix full of zeros with the larger dimensions
            padding = int(padding);
            paddedMatrix = np.zeros((len(self.array)+2*padding,len(self.array[0])+2*padding));
            
            '''
            copy the contents of our array into the larger, padded array
            '''
            #iterate through all of the elements in our array
            for rowIndx in range(0,len(self.array)):
                for columnIndx in range(0,len(self.array[0])):
                    
                    #copy our value at the current index to the padded matrix at the current index
                    paddedMatrix[rowIndx+padding][columnIndx+padding] = self.array[rowIndx][columnIndx];
                    
            self.array = paddedMatrix; #replace our array with the padded array
            
            if (self.debugMode):
                print(f"Padded Matrix {padding} layers: ");
                print(self.array);
        else:
            print("cannot pad a negative or zero amount.");
            
        
        
    # calculates the transformation of this matrix by the passed transArray
    def calculateTransformation(self,transArray,stride=1):
        
      
        #get the lengths of our array and the transformation array
        nR = len(self.array);
        nC = len(self.array[0]);
        fR = len(transArray);
        fC = len(transArray[0]);
        
        #calculate output matrix size
        outLenR = int(floor( (1 + nR - fR) / stride ) ); 
        outLenC = int(floor( (1+ nC - fC) / stride ) ); 
        
        
        #create a numpy matrix
        outMatrix = np.zeros((outLenR,outLenC));
        
        if (self.debugMode):
           print(f"outSize = int(floor( (1 + {nR} - {fR}) / {stride} ) )")
           print("OutMatrix before");
           print(outMatrix);
        
        #start subMatrix stepping
        self.startSubMatrixAquisition(len(transArray),len(transArray[0]),stride);
    
    
        '''
        Repetively get submatrices from the submatrix iterator, calculate the 
        dot product of that submatrix with the transformation matrix and put that
        dot product into the appropriate place in the outputmatrix
        '''
        subMatrix = self.nextSubMatrix();
        while (type(subMatrix) != type(None)):
              
            dotProduct = 0;
            
            # iterate through each element in the submatrix
            for rowIndx in range(0,len(subMatrix)):
                for columnIndx in range(0,len(subMatrix[0])):
                    
                    #calculate the dot product
                    dotProduct += transArray[rowIndx][columnIndx] * subMatrix[rowIndx][columnIndx];
            
            #put the dot product of the transformation in the output matrix
            outMatrix[self.subRowIndx][self.subColumnIndx] = abs(dotProduct/(fR*fC)); 
            
            
            if (self.debugMode):
                print("SubMatrix:");
                print(subMatrix);
                print(f"Dot product: {dotProduct}");
            
            subMatrix = self.nextSubMatrix(); # get the next subMatrix()
            
        return outMatrix;
    
    
    
    #transforms the picture
    def transform(self,transArray,padding = 0, stride = 1):
        if (padding > 0):
            self.pad(padding);
        
        self.array = self.calculateTransformation(transArray,stride);
        


#this is a testing method not used in any project
def testMyTrix():   
    #create a 2D numpy array
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13,14,15,16]]);
    
    #initialize a MyTricks with the numpy array
    picture = MyTrix(a);
    
    
    
    #turn on debug mode so we can see what is happening
    picture.setDebugMode(True);
    
    #MyTrix manipulation should work the same as normal array manipulations at base levels
    print("rowSize:", picture.rowSize);
    print("columnSize:", picture.columnSize);
    print("\n Matrix:")
    print(picture);
    print(picture.at(1,1));
    print(picture[0][0]);
    print(picture[0]);
    picture[0][0] = -1;
    
    print("\n Matrix with single replacement:")
    print(picture)  
    
    print("\n")
    
    #test subMatrix stepping
    picture.startSubMatrixAquisition(2,2);
    print("Sub matrices:");
    
    subMatrix = picture.nextSubMatrix();
    while (type(subMatrix) != type(None)):
        print(subMatrix);
        subMatrix = picture.nextSubMatrix();
        
    #test subMatrix replacement
    print("\nMatrix with replacement:");
    picture.replaceSubMatrix([[1,-2,3],[4,5,6],[7,8,9]]);
    print(picture);
    
    
    #test transformation with padding 1
    print("\n Test transformation:");
    picture.transform([[-1,2],[3,4]],1);
    print(picture);
    
    
    #test transformation with padding 2 and larger transformation
    print("\n Test transformation:");
    picture.transform([[1,-2,3],[4,5,6],[7,8,9]],2);
    print(picture);
    
#testMyTrix();

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''