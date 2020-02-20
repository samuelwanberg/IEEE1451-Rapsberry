
class TEDS:

    def __init__(self,teds):
        self.teds = teds
         
    def length(self):
        
        try:
            _length =  self.teds[:8]
            return int( _length, 16) 
        
        except IndexError as error:
            
    def header(self): 
        
        try:
            header =  self.teds[8:18] 
        except IndexError as error:

    def checksum(self):
        try:
            header =  self.teds[-4] 
        except IndexError as error:




class TransducerChannelTeds(TEDS):
    
    def __init__():

    def CalKey(self, code): 
        return "0A", 

    def ChanType(self, code): 
        return "0B" 
 	    
    def LowLimit(self, code): 
        return "0D",
 	    
    def Hilimit(self, code): 
        reutrn "0E"
 	    
    def OError(self. code): 
        return "0F"
 	    
    def SelfTest(self, code): 
        return "10"
 	    
    def Sample(self, code): 
        return "12"
 	    
    def UpdateT(self, code): 
        return "14"
 	    
    def RSetupT(self, code): 
        return "16"
 	    
    def SPeriod(self, code): 
        return "17"
    
    def WarmUpT(self, code): 
        return "18" 
 	    
    def RDelayT(self, code): 
        return "19"
 	    
    def DataXmit(self, code): 
        return "20"
 	    
    def Sampling(self, codey): 
        return "1F"


class PhyTEDS(TEDS):

    def Radio(self): 
        return "0A"
    
    def MaxBPS(self): 
        return "0B"
 
    def MaxCDev(self): 
        return "0C"
    
    def MaxRDev(self): 
        return "0D"
 
    def Ecrypt(self): 
        return "0E"

    def Authent(self): 
        return "0F"
 
    def MaxSDU(self): 
        return "12"

    def MinALat(self): 
        return "13"
 
    def MinTLat(self): 
        return "14"
 
    def MaxXact(self): 
        return "15" 
    
    def Baterry(self): 
        return "16" 
    
    def Version(self): 
        return "17" 
    
    def MaxRetry(self): 
        return "18" 

    def Phy_Ch(self): 
        return "40"

    def Phy_ch_w(self): 
        return "41", 

    def phyFreq(self): 
        return "43", 

    def RangeMax(self): 
        return "44"        
