from message import Reply
from TEDS.utility import convert_hex_to_decimal as hex_to_dec
from TEDS.ieee1451-0 import UserTransducerNameTedsReads, MetaTedsReads, TransducerChannelTedsReads, PhyTedsReads, 
'''
Commands common to the TIM and TransducerChannel

commandClass = {
    1 : "QueryTEDS",
    2 : "ReadTEDSSegment"
}
'''

class QueryTEDS:

    def __init__(self):
        pass


class ReadTEDSSegment(Reply):
    
    all_teds = {
        1 : MetaTedsReads,
        3 : TransducerChannelTedsReads,
        12: UserTransducerNameTedsReads,
        13: PhyTedsReads
    }
    
    def __init__(self, msg):
            self.msg = msg
            self.Success = "01"
            self.Fail = "00"
            self.sucess()
            self.body()

    def body(self):
        try:
            code = self.msg['code']
            tedsAcessCode = int.from_bytes(code, 'big')
            teds = self.all_teds[tedsAcessCode]()
            return teds.hex_format()
        except KeyError:
            '''
              TEDS code Error
            '''
            self.fail()
        
    def sucess(self):
        self._flag = self.Success 
        
    def fail(self):
        self._flag = self.Fail
        
    def flag(self):
        return self._flag
    
    def length(self):
        
        if self.flag() != "00":
            _length = len(self.body)
        
            return _length.to_bytes(byteorder='big',
                                    length=4).hex()
        else:
            return "0000"

    def reply_dependent(self):
        if self.flag() != "00":
            return self.body()
        else:
            return "0000"
