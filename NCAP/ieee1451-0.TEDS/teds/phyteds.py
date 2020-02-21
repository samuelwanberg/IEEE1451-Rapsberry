

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
