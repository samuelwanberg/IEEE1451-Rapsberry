from teds import TEDS


class MetaTedsReads(TEDS):
    
    '''
    The Meta-TEDS is a reqired TEDS. The function of the Meta-TEDS shall be 
    to make avaliable at the interface all information needed to gain acess to a
    ny TransducerChannel, plus information common to all TransducerChannels
    
         Acess Query TEDS command
         Read TEDS segment command
    '''
    def __init__(self, filename="teds/metaTeds.json"):
        
        self.name = "MetaTeds"
        super().__init__(self.name, filename)

        self.blockcode = {
            'Header' : '03',
            'UUID' : '04',
            'OHoldOff' : '0A', 
            'TestTime' : '0C',
            'MaxChan' : '0D',
           }
    
    def pipeline(self):
        pass


class TransducerChannelTedsReads(TEDS):
    '''
            TransducerChannelTeds 
    Acess Query TEDS command
    Read TEDS segment command
    '''
    def __init__(self, filename="teds/transducerChannelTeds.json"):
        
        self.name = "TransducerChannelTeds"
        super().__init__(self.name, filename)

        self.blockcode = {
 	    "CalKey" : "0A", 
 	    "ChanType" : "0B", 
 	    "LowLimit" : "0D",
 	    "Hilimit" : "0E",
 	    "OError" : "0F",
 	    "SelfTest" : "10",
 	    "Sample" : "12",
 	    "UpdateT" : "14",
 	    "RSetupT" : "16",
 	    "SPeriod" : "17",
 	    "WarmUpT" : "18", 
 	    "RDelayT" : "19",
 	    "DataXmit" : "20",
 	    "Sampling" : "1F"
        } 


class PhyTedsReads(TEDS):
    
    def __init__(self, filename='teds/phyteds.json'):
        
        self.name = "PhyTeds"
        super().__init__(self.name, filename)

        self.blockcode = {
            "Radio": "0A",
            "MaxBPS": "0B", 
            "MaxCDev": "0C", 
            "MaxRDev": "0D", 
            "Ecrypt": "0E",
            "Authent": "0F", 
            "MaxSDU": "12",
            "MinALat": "13", 
            "MinTLat": "14", 
            "MaxXact": "15", 
            "Baterry": "16", 
            "Version": "17", 
            "MaxRetry": "18", 
            "Phy_Ch": "40",
            "Phy_ch_w": "41", 
            "phyFreq": "43", 
            "RangeMax": "44"
        }


class UserTransducerNameTedsReads(TEDS):
    
    def __init__(self, filename="teds/userTransducerNameTeds.json"):
        
        self.name = "userTransducerNameTeds"
        super().__init__(self.name, filename)

        self.blockcode = {
            'Format' : '04',
            'TCName' : '05',
        }

