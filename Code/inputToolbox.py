
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

def getIntegerFromUser(inputString = "Enter a number", errorString = "Invalid number, must be a valid integer."):
    validInput = False;
    
    while(not validInput):
        try:
            Input = float(input(inputString));
            
            if (int(Input) != Input): #make sure whole number
                print(errorString);
                continue;
                
            Input = int(Input);
            
            validInput = True;
        except ValueError:
            print(errorString);
    return Input;


def getFloatFromUser(inputString = "Enter a number", errorString = "Invalid number, must be a valid floating point number."):
    validInput = False;
    
    while(not validInput):
        try:
            Input = float(input(inputString));
            
            validInput = True;
        except ValueError:
            print(errorString);
    return Input;


def getListInputFromFile(file,numChars = -1, delimeter = ' ', eol = '\n', fileNotFoundStr = "Error; file not found"): #input from file function that can take either a file object or a string address of a file object
    
    try:
        tokenIndx = 0;
        lineIndx = 0;
        token = "";
        inputList = [[]];
        charReadCount = 0;
        while (charReadCount != numChars): #keep reading until we have read the target amount. (Any negative number will read until the end of the file)
            char = file.read(1);
             
            
            if(char == ""): #we have reached the end of the file
               inputList[lineIndx].append(token);
               return inputList
           
            if(eol in char): #create a new line
                inputList[lineIndx].append(token);
                token = "";
                inputList.append([]);
                lineIndx+=1;
                continue;
            elif (char == delimeter): #token is complete
                tokenIndx+=1;
                charReadCount+=1;
                inputList[lineIndx].append(token);
                token = "";
                continue;
            
                
            token += char;
                        
            charReadCount+=1;
 
    except AttributeError: #file is a string and not a file
        inputFile = open(file,"r");
        Return = getListInputFromFile(inputFile,numChars, delimeter, eol,fileNotFoundStr); #open a file with "file" as the address
        inputFile.close();
        return Return;
    except FileNotFoundError:
        print(fileNotFoundStr);


def getListInputFromString(string,numChars = -1, delimeter = ' ', eol = '\n'): #input from string function that can take either a file object or a string address of a file object
        tokenIndx = 0;
        lineIndx = 0;
        token = "";
        inputList = [[]];
        charReadCount = 0;
        
        while (charReadCount != numChars): #keep reading until we have read the target amount. (Any negative number will read until the end of the file)
            char = string[charReadCount];
            charReadCount+=1;
            
            if((charReadCount >= len(string)-1) or (char == "")): #we have reached the end of the file
               inputList[lineIndx].append(token);
               return inputList
           
            if(eol in char): #create a new line
                inputList[lineIndx].append(token);
                token = "";
                inputList.append([]);
                lineIndx+=1;
                continue;
            elif (char == delimeter): #token is complete
                tokenIndx+=1;
                
                inputList[lineIndx].append(token);
                token = "";
                continue;
            
                
            token += char;


def indexOf(x, big):
    i = 0;
    for cThin in big:
        if (cThin == x):
            return i;
        i+=1;
    return -1;
    
        
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''