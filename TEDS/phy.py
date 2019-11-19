
"""
  Class implement PhyTEDS for Wifi 
   
"""
class PhyTEDSforWiFI:

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
          Class 12 for transducer name teds for default (in Table 17)
          Version 01
          Tuple Length 01
        '''
        return "03 04 05 0C 01 01"
    
    def Radio(self):
        return "0A 01 01"
    
    def MaxBPS(self):
        return "0B 04 00 00 00 FA"
    
    def MaxRDEV(self):
        pass

    def encrypty(self):
        pass

    def autenth(self):
        pass

    def maxSDU(self):
        pass

    def minALat(self):
        pass

    def minTLat(self):
        pass

    def maxXact(self):
        pass

    def baterry(self):
        pass

    def version(self):
        pass

    def maxRetry(self):
        pass

    def tlv(self):
        
        return "{0} {1} {2} ".format(
            self.header(),
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
        pass

    def teds_format(self):
           
