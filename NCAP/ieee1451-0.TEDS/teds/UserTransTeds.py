from read_teds import TEDS 
from utils import hex2dec, bin2dec, hex2float


class UserTransducerNameTEDS(TEDS):
    
    def __init__(self,teds):
        self.teds = teds
        self.name = "UserTransducerName"
        
        super().__init__(self.name, self.teds)
        
        self.stages = {
            '04': ('Format', self.Format) 
            '05': ('TCName', self.TCName)
        }

    def Format(self, code):
        return {
            'Format' : code
        }

    def TCName(self, code):
        return {
            'TCName' : code
        }

