import json
from utilitys import convert_hex_to_decimal as hex_to_dec



class PhyTedsReads:
    
    '''
    The Meta-TEDS is a reqired TEDS. The function of the Meta-TEDS shall be 
    to make avaliable at the interface all information needed to gain acess to a
    ny TransducerChannel, plus information common to all TransducerChannels
    
         Acess Query TEDS command
         Read TEDS segment command
    '''
    def __init__(self, filename="userTransducerNameTeds.json"):
        
        self.name = "userTransducerNameTeds"

        self.blockcode = {
            'Format' : '04',
            'TCName' : '05',
        }

