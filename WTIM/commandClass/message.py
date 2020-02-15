class Reply:
    
    def __init__(self, ):
        self.message = []
    
    def flag(self):
        pass

    def length(self):
        pass
        
    def replymessage(self):
        pass

    def error(self):
        pass

    def byteMesg(self):
        return bytes.fromhex(self.flag() + /
                             self.length() + / 
                             self.replymessage())
