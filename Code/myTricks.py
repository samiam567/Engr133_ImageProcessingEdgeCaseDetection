
import numpy as np;

class MyTricks():
    def __init__(self,array): #initialize a new MyTrix object with a numpy array 
        if not (type(array) is np.ndarray):
                raise TypeError("MyTricks must be initialized with a numpy array of type int or float");
        else:
            self.array = array;
    
    

def testCode():
    picture = MyTricks(np.empty(10,dtype=np.float32));
    print(picture.array);
    pass;
    
    
    
testCode();