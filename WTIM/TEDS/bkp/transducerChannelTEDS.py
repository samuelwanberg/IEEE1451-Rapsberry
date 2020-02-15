from teds import TEDS


class TransducerChannelReads(TEDS):
    '''
            TransducerChannelTeds 
    Acess Query TEDS command
    Read TEDS segment command
    '''
    def __init__(self, filename="transducerChannelTeds.json"):
        
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
