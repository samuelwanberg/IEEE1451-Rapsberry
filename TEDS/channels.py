from utils import *

"""
   Representation Class for UserTransducerNameTeds 
   
"""

class ChannelTransducerTeds:

    def __init__(self):
        '''
        with open('userTedsId.json', 'r')  metadata:
           userteds = json.load(metadata)
        else:
            raise
        '''
        pass 
    
    def header(self):
        '''
          TEDS_ID 
          Header tvl for the UserTransducerName  Default
          Type 03
          Length 04 
          Family 00
          Class 03 for transducer name teds for default (in Table 17)
          Version 01
          Tuple Length 01
        '''
        return "03 04 00 " + convert_dec_to_hex(03) + " 01 01"

    def Calkey(self):
        return "0A 01 00"
    
    def ChanType(self):
        return "0B 01 00"
    
    def PhynUnits(self):
        return "OC 06 32 01 00 39 01 82"
   
    def LowLimit(self):
        return "43 88 93 33"
    
    def HiLimit(self):
        return "43 88 93 33"
    
    def Oerror(self):
        return "0F 01 3F 00 00 00"
    
    def selfTest(self):
        return "10 01 01"
    
    def Sample(self):
        return "12 09 28 01 00 29 01 01 30 01 08"
    
    def UpdateT(self):
        return "14 04 3D CC CC CD"

    def RSetupT(self):
        return "16 04 37 D1 B7 17"
    
    def Speriod(self):
        return "17 04 3D CC CC CD"

    def WarmUpT(self):
        return "18 04 41 F0 00 00"

    def Rdelay(self):
        return "19 04 37 D1 B7 17"

    def TestTime(self):
        return "20 04 41 F0 00 00"
    
    def Sampling(self):
        return "1F 03 21 01 02"

    def tlv(self):
        
        return "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} ".format(
            self.header(),
            self.Calkey(),
            self.ChanType(),
            self.PhynUnits(),
            self.LowLimit(),
            self.HiLimit(),
            self.Oerror(),
            self.selfTest(),
            self.Sample(),
            self.UpdateT(),
            self.RSetupT(),
            self.Speriod(),
            self.WarmUpT(),
            self.Rdelay(),
            self.TestTime(),
            self.Sampling()
        )
    
    def length(self):
        '''
            TEDS length é o numero total de octetos no bloco de construcao
            dos teds + 2 octetos para o checksum 
            representação Uint32  4 octets 
        '''
        total_octet = self.tlv()
        length = len( total_octet.split() ) + 2  # + 2 do checksum
        return convert_dec_to_hex(length, octect=2 )

    def checksum(self):
        return "11 BA"

    def teds_format(self):

        
