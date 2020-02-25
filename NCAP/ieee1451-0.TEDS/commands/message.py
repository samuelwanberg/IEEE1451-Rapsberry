

class MessageStructure:
    
    def __init__(self, vect):
        self.vect = vect
        
    def __len__(self):
        return len(self.vect)
        
    def __getitem__(self, i):
        return self.vect[i]
        
    def __setitem__(self, i, value):
        self.vect[i] = value

    def destination(self):
        return self.vect[:2] 
        
    def commandClass(self):
        return self.vect[2]

    def commandFunction(self):
        return self.vect[3]

    def length(self):
        return self.vect[4:6]

    def commandDependent(self):
        return self.vect[6:]
    
    def byteMesg(self):
        return bytes.fromhex(self.destination() + \
                             self.commandClass() + \ 
                             self.commandFunction() + \
                             self.length() + \
                             self.commandDependent()
        )

