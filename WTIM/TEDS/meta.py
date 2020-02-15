from teds import TEDS

class MetaTedsReads(TEDS):
    
    '''
    The Meta-TEDS is a reqired TEDS. The function of the Meta-TEDS shall be 
    to make avaliable at the interface all information needed to gain acess to a
    ny TransducerChannel, plus information common to all TransducerChannels
    
         Acess Query TEDS command
         Read TEDS segment command
    '''
    def __init__(self, filename="metaTeds.json"):
        
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
