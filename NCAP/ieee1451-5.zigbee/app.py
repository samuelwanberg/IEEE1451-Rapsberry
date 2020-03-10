from zigbee import ConnectZigBee
from datanase import Wtim
from callbacks import Calls

class MachineState:

    def __init__(self):
        
        self.zigbee = ConnectZigBee()
        callb = Calls()
        
    def init(self):
        
        self.zigbee.connect()
        self.zigbee.dicovery_node(callb.discovery)
        self.finishing()

    def wait(self):
        pass

    def finishing(self):
        print('Finish !!!!')
        
        
    

if __name__ == '__main__':
    
    ncap = NCAPMachineState()
    ncap.init()
