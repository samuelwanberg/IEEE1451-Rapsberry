from message import Reply
from TEDS.ieee1451-0 import UserTransducerNameTedsReads, MetaTedsReads, TransducerChannelTedsReads, PhyTedsReads
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
    
    def __init__(self, code=0):
        
        self.TEDSAccessCode = code
        self.Success = "0001"
        self.Fail = "0000"
        
        try:
            self.sucess()
            teds = self.all_teds[self.TEDSAccessCode]()
            self.body = teds.hex_format()
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
        
        if self.flag() != "0000":
            _length = len(self.body)
        
            return _length.to_bytes(byteorder='big',
                                    length=4).hex()
        else:
            return "00000000"

    def reply_dependent(self):
        
        if self.flag() != "0000":
            return self.body
        else:
            return "00000000"
