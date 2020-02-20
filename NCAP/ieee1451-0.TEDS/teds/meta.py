from read_teds import TEDS 
from utils import hex2dec, bin2dec, hex2float


class MetaTEDS(TEDS):
    
    def __init__(self,teds):
        self.teds = teds
        
    def UUID(self, code):

        try:

            binary = bin(  hex_to_dec(code) )[2:]

            N_S =  'N' if binary[0] == 0 else 'S'
            Latitude = bin_to_dec(binary[1:20]) 
            E_W = 'E'if binary[20] == 0 else 'W'
            Longitude = bin_to_dec(binary[21:41]) 
            Manufacturer = bin_to_dec(binary[41:45])
            Year = bin_to_dec(binary[45:57])
            Date = bin_to_dec(binary[57:])
            
            return {
                'N_S' : N_S,
                'Latitude' : Latitude,
                'E_W' : E_W,
                'Longitude' : Longitude,
                'Manufacturer' : Manufacturer,
                'Year' : Year,
                'Date' :  Date,
            }
            
        except IndexError:
            raise ("UUID Error in MetaTEDS")
        

    def OHoldOff(self, code):
        return {
            'OHoldOff': hex2float(code)
        }

    def TestTime(self, code):
        '''Float32 4 '''
    
    def MaxChan(self, code):
        '''Uint16 1 '''
        return {'MaxChan' : hex2dec(code) }
