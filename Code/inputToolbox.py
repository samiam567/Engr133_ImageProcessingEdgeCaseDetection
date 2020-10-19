

def getIntegerFromUser(inputString = "Enter a number", errorString = "Invalid number, must be a valid integer."):
    validInput = False;
    
    #repeat while we don't have valid input
    while(not validInput):
        try:
            #ask the user for a integer
            Input = float(input(inputString));
            
            if (int(Input) != Input): #make sure whole number
                print(errorString);
                continue;
                
            Input = int(Input); # convert input to an int
            
            validInput = True;
        except ValueError: # if there is an error print the error string
            print(errorString);
    return Input;
