def joinHex(hex):
        return ''.join(hex)


class MessageStructure:
    
    def __init__(self, vect):
        self.vect = vect
    
    def __str__(self):
        return f"$(self.vect)"

    def __repr__(self):
        return f"$(self.vect)"

    def __len__(self):
        return len(self.vect)
        
    def __getitem__(self, i):
        return self.vect[i]
        
    def __setitem__(self, i, value):
        self.vect[i] = value

    def destination(self):
        return joinHex(self.vect[:2]) 
    
    def commandClass(self):
        return joinHex(self.vect[2])
    
    def commandFunction(self):
        return joinHex(self.vect[3])
    
    def length(self):
        return joinHex(self.vect[4:6])

    def commandDependent(self):
        return joinHex(self.vect[6:])
    
    def byteMesg(self):
        return bytes.fromhex(self.destination() + 
                             self.commandClass() +  
                             self.commandFunction() + 
                             self.length() + 
                             self.commandDependent())
