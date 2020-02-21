from read_teds import TEDS 
from utils import hex2dec, bin2dec, hex2float


class PhyTEDS(TEDS):

    def __init__(self,teds):

        self.teds = teds
        self.name = "PhyTeds"
        
        super().__init__(self.name, self.teds)

        self.stages = { '0A' : ('Radio', self.Radio), 
                        '0B' : ('MaxBPS', self.MaxBPS),  
                        '0C' : ('MaxCDev', self.MaxCDev), 
                        '0D' : ('MaxRDev', self.MaxRDev), 
                        '0E' : ('Ecrypt', self.Ecrypt), 
                        '0F' : ('Authent', self.Authent), 
                        '12' : ('MaxSDU', self.MaxSDU), 
                        '13' : ('MinALat', self.MinALat), 
                        '14' : ('MinTLat', self.MinTLat), 
                        '15' : ('MaxXact', self.MaxXact), 
                        '16' : ('Baterry', self.Baterry), 
                        '17' : ('Version', self.Version), 
                        '18' : ('MaxRetry', self.MaxRetry), 
                        '40' : ('Phy_Ch', self.Phy_Ch), 
                        '41' : ('Phy_ch_w', self.Phy_ch_w), 
                        '43' : ('phyFreq', self.phyFreq), 
                        '44' : ('RangeMax', self.RangeMax)
        }

    def Radio(self, code): 
        return{ 
            "Radio" : hex2dec(code)
        }

    def MaxBPS(self, code): 
        return{ 
            "MaxBPS" : hex2dec(code)
        }
 
    def MaxCDev(self, code): 
        return{ 
            "MaxCDev" : hex2dec(code)
        }
 
    def MaxRDev(self, code): 
        return { 
            "MaxRDev" : hex2dec(code)
        }
 
    def Ecrypt(self, code): 
        return { 
            "Ecrypt" : hex2dec(code)
        }
 
    def Authent(self, code):
        ''' Duvida'''
        return { 
            "Authent" : hex2dec(code)
        }
 
    def MaxSDU(self, code): 
        return { 
            "MaxSDU" : hex2dec(code)
        }

    def MinALat(self, code): 
        return { 
            "MinALat" : hex2dec(code)
        }
 
    def MinTLat(self, code): 
        return { 
            "MinALat" : hex2dec(code)
        }

    def MaxXact(self, code): 
        return { 
            "MaxXact" : hex2dec(code)
        }
 

    def Baterry(self, code): 
        return { 
            "Baterry" : hex2dec(code)
        }

    def Version(self, code):  
        return { 
            "Version" : hex2dec(code)
        }

    def MaxRetry(self, code): 
        return { 
            "MaxRetry" : hex2dec(code)
        }

    def Phy_Ch(self, code): 
        return { 
            "Phy_Ch" : hex2dec(code)
        }

    def Phy_ch_w(self, code): 
        return { 
            "Phy_ch_w" : hex2dec(code)
        }

    def phyFreq(self, code): 
        return { 
            "phyFreq" : hex2dec(code)
        }

    def RangeMax(self, code): 
        return { 
            "RangeMax" : hex2dec(code)
        }
