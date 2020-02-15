import json
from utilitys import convert_hex_to_decimal as hex_to_dec

class TEDS:

    '''
    Generic TEDS Structure General for TEDS formats
    '''
    #TAble 17 in the IEEE 1451 Document
    class_teds = {
        "METATEDS" : "01",
        "TRANSDUCERCHANNELTEDS" : "03",
        "USERTRANSDUCERTEDS" : "0C",
        "PHYTEDS" : "0D"
    }

    def __init__(self,name, filename):
        self.name = name
        self._readJson(filename)
        
        try:
            code = self.class_teds[self.name.upper()]
            # Make default header id valid for aspecific teds
            self.header_format = f"030400{code}0101"
        except KeyError:
            print(f"{self.name} is not include in _classteds for TEDS table ")
            
            
    def clear_hexcode(self, hexcode):
        
        assert type(hexcode) == str, "Type hexcode Error"
        data = hexcode.strip() \
                      .replace(" ","")       
        return data 

    def _readJson(self, filename):
        with open(filename,'r') as f:
            self.metadata = json.load(f)
    
    def _length(self):
        data = self.metadata['Length']
        
        hexcode = self.clear_hexcode(data)
        
        if not len(hexcode) / 2 == 4:
            raise Exception("Campo Length não possue 4 Octetos")
        
        length = hex_to_dec(hexcode)
        
        return length
    
    def header(self):
        '''
            header for metateds
        '''
        field = self.metadata['Header']
        _header = self.clear_hexcode("".join(field.values())) 
        
        if not field['Type'] == '03':
            raise Exception("TypeCode {0} Header not valid for {1}".format(field['Type'], self.name))
        
        print(self.header_format)
        if not _header == self.header_format: # UserTransducerChannelTedsIF
            raise Exception("UUID Header {0} not valid for {1}".format("".join(field.values()), self.name))
        
        return "".join(field.values())
    
    def verify_block(self):
        
        for key in self.metadata:
            
            if key in ['Length','Checksum', 'Header']:
                pass
            else:
                _type = self.clear_hexcode(self.metadata[key]['Type'])
                code  = self.blockcode[key]
                
                if not _type == code:
                    raise Exception("CodeType Error {0}".format(key))
                
                hexcode = self.clear_hexcode( self.metadata[key]['Length'] )
                length = hex_to_dec( hexcode )
                value = self.clear_hexcode(self.metadata[key]['Value'])
                
                if not length  == len(value) / 2:
                    raise Exception("Value Length Error {0} - {1}".format(key, self.name))
                
        '''
        extract TLV blockCode
        '''
        return { key : self.clear_hexcode(self.metadata[key]['Value']) 
                 for key in self.blockcode }

    def checksum(self):

        checksum = self.clear_hexcode(self.metadata['Checksum']) 
        if not len(checksum) / 2 == 2   : # two octecs
                    raise Exception("Length Chesum Error {0} - {1}".format(checksum, self.name))
                
        return  checksum
    
    def hex_format(self):
        return /
        self._length() + / 
        self.header()  + /
        "".join(self.verify_block().values()) + /
        self.checksum()
    
