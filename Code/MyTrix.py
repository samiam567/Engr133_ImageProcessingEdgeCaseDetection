
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


import numpy as np;

class MyTrix():
    def __init__(self,array): #initialize a new MyTrix object with a numpy array 
        if not (type(array) is np.ndarray):
                raise TypeError("MyTricks must be initialized with a numpy array");
        else:
            self.array = array;
            self.rowSize = array.shape[0];
            self.columnSize = array.shape[1];
    
    def at(self,i,j):
       return self.array[i][j];
    
    def __str__(self):
        return str(self.array);
    
    def __getitem__(self,key):
        return self.array[key];

    #initializes the process of parcing through the MyTrix by sub-matricies of the specified size
    def startSubMatrixAquisition(self,rowSize, columnSize):
        self.subRowSize = rowSize;
        self.subColumnSize = columnSize;
        
        
        self.subRowIndx = 0; 
        self.subColumnIndx = -1; #we start at -1 because we increment the indeces at the start of the nextSubMatrix method
        
        
    # will return the next submatrix of the specified size. (startSubMatrixAquisition() must be called before this method for it to work properly)
    def nextSubMatrix(self):
        
        #advance to the next subMatrix indices
        if ((self.subColumnIndx+1)*self.subColumnSize < self.columnSize):
                self.subColumnIndx += 1;
        
        elif ( (self.subRowIndx+1)*self.subRowSize < self.rowSize):
            self.subColumnIndx = 0;
            self.subRowIndx += 1;
        else:
            return None;
                
            
        #create the submatrix to fill with values    
        subMatrix = np.zeros((self.subRowSize,self.subColumnSize));
        
        
        try:
            #determine where to start grabbing values from the our matrix
            startRowIndx = self.subRowIndx * self.subRowSize;
            startColumnIndx = self.subColumnIndx * self.subColumnSize; 
            
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
            startRowIndx = self.subRowIndx * self.subRowSize;
            startColumnIndx = self.subColumnIndx * self.subColumnSize; 
            
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

    #transforms the matrix by multiplying each element by the cooresponding 
    def transForm(self,transArray):
        #start subMatrix stepping
        self.startSubMatrixAquisition(len(transArray),len(transArray[0]));
        
        subMatrix = self.nextSubMatrix();
        while (type(subMatrix) != type(None)):
            
            for rowIndx in range(0,len(subMatrix)):
                for columnIndx in range(0,len(subMatrix[0])):
                    subMatrix[rowIndx][columnIndx] = transArray[rowIndx][columnIndx] * subMatrix[rowIndx][columnIndx];
                    
            self.replaceSubMatrix(subMatrix);
            
            subMatrix = self.nextSubMatrix();
            

        
            

def testMyTrix():   
    #create a 2D numpy array
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13,14,15,16]]);
    
    #initialize a MyTricks with the numpy array
    picture = MyTrix(a);
    
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
    picture.replaceSubMatrix([[1,-2],[3,4]]);
    print(picture);
    
    print("\n Test transformation:");
    picture.transForm([[-1,2],[3,4]])
    print(picture);
    
testMyTrix();

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''