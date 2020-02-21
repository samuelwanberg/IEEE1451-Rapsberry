from utils import hex2dec


class TEDS:

    def __init__(self,name,teds):
        self.name = name
        self.teds = self.verify(teds)
    
    def verify(self, teds):
        teds = teds.strip()
        teds = teds.replace(' ','')
        
        return teds
         
    def length(self):
        
        try:
            _length =  self.teds[:8]
            return int( _length, 16) 
        
        except IndexError as error:
            print(error)
            
    def header(self): 
        
        try:
            header =  self.teds[8:18] 
        except IndexError as error:
            print(error)
    
    def blockcode(self):
        
        try:
            #Conteudo entre o Header e o Checksum
            return self.teds[18:-4] 
        except IndexError as error:
            print(f"Error blockcode {self.name} TEDS Size: {error}")

    def checksum(self):
        try:
            header =  self.teds[-4] 
        except IndexError as error:
            print(f"Checksum {self.name} TEDS size Error {error}")

    def pipeline(self):
        
        #Reorganizando o arquivo para formar pares de octetos
        # Por exemplo [00aabbcc] -> [00, aa, bb, cc]
        blockcode = [self.blockcode()[i:i+2] 
                     for i in range(0, len(self.blockcode()), 2)]
        
        result = {}

        while len(blockcode) > 0:
            
            try:
                type = blockcode.pop()
                key, function = self.stages[type]
            except KeyError as error:
                print(f"Error BlockCode TEDS invalid ID: {error}")

            length = hex2dec( blockcode.pop() )
            
            try:
                value = blockcode[:length]
                result.update( function(value) )

                #increments
                blockcode = blockcode[length:]
            except (KeyError, IndexError) as error:
                print(f"Error to Construct {self.name} type {key} BlockCode: {error}")

        return result 
