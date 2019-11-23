from utils import *

"""
   Representation Class for UserTransducerNameTeds 
   
"""

class UserTransducerNameTeds:

    def __init__(self):
        '''
        with open('userTedsId.json', 'r')  metadata:
           userteds = json.load(metadata)
        else:
            raise
        '''
        pass 
        
    def format(self):
        '''
             Define o formato de representação do Nome do usuario
        _type = "04"
        length = "01"
        value = "00" Formato do texto do TIM Definido pelo usuario
        '''
        return "04 01 00"


    def TCN_Name(self):
        '''
              wtim-1
        '''
        type = "05 "
        length = "07 "
        value = "77 74 69 6d 2d 31 0A"
        
        return type + length + value 

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
        return "03 04 00 " + convert_dec_to_hex(12) + " 01 01"

    def tlv(self):
        
        return "{0} {1} {2} ".format(
            self.header(),
            self.format(),
            self.TCN_Name(),
        )
    
    def length(self):
        '''
            TEDS length é o numero total de octetos no bloco de construcao
            dos teds + 2 octetos para o checksum 
            representação Uint32  4 octets 
        '''
        total_octet = self.tlv()
        length = len( total_octet.split() ) + 2  # + 2 do checksum
        return convert_dec_to_hex(length, oct=4 ) + " "

    def checksum(self):
        #teste
        hexcodes = self.tlv()
        
    def teds_format(self):
        return self.length() + self.tlv() 
        
