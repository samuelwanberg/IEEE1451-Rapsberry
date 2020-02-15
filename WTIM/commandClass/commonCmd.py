from message import Reply
from ieee1451-0 import UserTransducerNameTedsReads, MetaTedsReads, TransducerChannelTedsReads, PhyTedsReads

'''
Commands common to the TIM and TransducerChannel
commandClass = {
    1 : "QueryTEDS",
    2 : "ReadTEDSSegment"
}
class QueryTEDS:

    def __init__(self):
        pass
'''
class ReadTEDSSegment(Reply):
    
    all_teds = {
        1 : MetaTedsReads,
        3 : TransducerChannelTedsReads,
        12: UserTransducerNameTedsReads,
        13: PhyTedsReads
    }
    
    def __init__(self, code=0):
        self.TEDSAccessCode = code 
        
    def _message(self):
        
        try:
            flag= "01"
            teds = (self.all_teds[self.TEDSAccessCode])()           
            format = teds.hex_format()
            length = len(format).to_bytes(byteorder='big', / 
                                          length=2).hex()
            
            self.message = flag + length + format 

        except KeyError:
            flag = "00"
    
    def err_message(self):
        self.message
