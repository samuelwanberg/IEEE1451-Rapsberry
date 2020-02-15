
class Reply:
    
    def flag(self):
        raise Exception("Flag is Empty and not Implement")

    def length(self):
        raise Exception("length is Empty and not Implement")
        
    def reply_dependent(self):
        raise Exception("reply_dependent is Empty and not implement")

    def byteMesg(self):
        return bytes.fromhex(self.flag() + /
                             self.length() + / 
                             self.reply_dependent()
