import json
from utils import *

class MetaTeds:

    """
      Classe que representa  a formação das metateds 
      Meta-TEDS tem como objetivo disponibilizar todas 
      as informações necessárias para obter acesso a 
      acesso a qualquer canal do transdutor e definir 
      uma identificação única para o modulo TIM.
    """
    _tableHex = []

    def __init__(self):

    def open(self):

        with open('metateds.json', 'r')  metadata:
           metateds = json.load(metadata)
        else:
            raise
       
    def length(self):
        
    def tedsiD(self):
        
        tedsid = self.metateds['TEDSID']
        hextable = tedsid.values()
        hextable[1] = convert_dec_to_hex(hextable[1], 2)

        return hextable
    
    def uuid(self):
        
        uuid = self.metateds['UUID']
        hextable = []

        #extract Type
        hextable.append(uuid['Type'])

        #extract Length
        hextable.append( convert_dec_to_hex( uuid['Length'], 2) )

        #extract Location
        location = uuid['Location']
        n_s = localtion[0]
        log = ((20 - len(bin(location[1])[2:])) * '0') + bin(location[1])[2:]
        e_w = location[2]
        lat = ((20 - len(bin(location[3])[2:])) * '0') + bin(location[3])[2:]
        
        manufactorValue = uuid['Manufacturer']

        year = uuid['Year']
        yearBin = ((12 - len(bin(year)[2:])) * '0') + bin(year)[2:]

        time = uuid['Time']
        timeBin = ((12 - len(bin(time)[2:])) * '0') + bin(time)[2:]
        ''' testar ''' 
        binary = n_s + log + e_w + lat + manufactorValue + yearBin + timeBin
        hextable.append( "0:0>10X".format( binary ) )

        return hextable
        
    def oHodOff(self):

        '''
          Input Example from json file 0A 4 0.5
          output 0A 40    
             
        '''
        import bitstring

        ohodOff = self.metateds['OHoldOff']
        hextable = []
        hextable.append(ohodOff['Type'])
        hextable.append( "{0:0>2X}".format( ohodOff['Length'] ) )

        b = bitstring.BitArray(float = ohodOff['Timeout'] , length=32)
        index = [(0,4), (4,8), (8,12), (12,16), (16,20), (20,24), (24,28), (28,32)]
        hexadecimal = [ "{0:0>1X}".format(b.bin[i,j])  for i,j in index]
        hextable.append( "".join(hexadecimal))

        return hextable
        
              
    def testTime(self):

        import bitstring
        testTime = self.metateds['TestTime']
        hextable = []

        hextable.append( tesTime['Type'])
        hextable.append( "{0:0>2X}".format( testTime['Length']))
        b = bitstring.BitArray(float = testTime['Timeout'] , length=32)
        index = [(0,4), (4,8), (8,12), (12,16), (16,20), (20,24), (24,28), (28,32)]
        hexadecimal = [ "{0:0>1X}".format(b.bin[i,j])  for i,j in index]
        hextable.append( "".join(hexadecimal))
        return hexadecimal     
        
    def maxChannel(self):

        maxChannel = self.metateds['MaxChannel']
        hextable = []
        hextable.append( maxChannel['Type'])
       
    def checksum(self):

    def do_write(self):
                with 
        
