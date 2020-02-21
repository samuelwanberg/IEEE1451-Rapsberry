from utils import hex2dec, bin2dec, hex2float

class TransducerChannelTeds(TEDS):
    
    def __init__(self):
        
        self.stages  = {
 	    "0A": ("CalKey", self.CalKey ), 
 	    "0B": ("ChanType", self.ChanType ), 
 	    "0D": ("LowLimit", self.LowLimit ),
 	    "0E": ("Hilimit", self.Hilimit ),
 	    "0F": ("OError", self.OError ),
 	    "10": ("SelfTest", self.SelfTest ),
 	    "12": ("Sample", self.Sample ),
 	    "14": ("UpdateT", self.UpdateT ),
 	    "16": ("RSetupT", self.RSetupT ),
 	    "17": ("SPeriod", self.SPeriod ),
 	    "18": ("WarmUpT", self.WarmUpT ), 
 	    "19": ("RDelayT", self.RDelayT ),
 	    "20": ("DataXmit", self.DataXmit ),
 	    "1F": ("Sampling", self.Sampling ) 
        } 


    def CalKey(self, code): 
        return {
            'Calkey': hex2dec(code)  
            }

    def ChanType(self, code): 
        return { 
            'ChanType' : hex2dec(code) 
        }
 	    
    def LowLimit(self, code): 
        return {
            "LowLimit" : hex2float(code)
        }
 	    
    def Hilimit(self, code): 
        return {
            "Hilimit" : hex2float(code)
        }
 	    
    def OError(self. code): 
        return {
            "OError" : hex2float(code)
        }
 	    
    def SelfTest(self, code): 
        return {
            "SelfTEst" : hex2dec(code)
        }
 	
    def Sample(self, code): 
        '''Duvidas  '''
        return {
            "Sample" : hex2float(code)
        }
 	    
    def UpdateT(self, code): 
        return {
            "UpdateT" : hex2float(code)
        }
 	    
    def RSetupT(self, code): 
        return {
            "RSetupT" : hex2float(code)
        }
    
    def SPeriod(self, code): 
        return {
            "SPeriod" : hex2float(code)
        }

    def WarmUpT(self, code): 
        return {
            "WarmUpT" : hex2float(code)
        }
 	    
    def RDelayT(self, code): 
        return {
            "RDelayT" : hex2float(code)
        }
 	    
    def DataXmit(self, code): 
        return {
            "DataXmit" : hex2float(code)
        }
 	    
    def Sampling(self, codey):
        '''
    Duvidas 
        '''
        return {
            "Sampling" : hex2float(code)
        }
