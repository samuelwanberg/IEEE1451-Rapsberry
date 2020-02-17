from zigbee.zigConnect import xBeeConnect
from commonCmd import QueryTEDS, ReadTEDSSegment

def make_error():
   return bytes.fromhex("00" * 8)
    
def parse_msg(msg):
    
    id_channel = int.from_bytes(msg[:2], "big") # Dois primeiros bytes para id channel 
    commandClass = int.from_bytes(msg[2:3], "big") # 1 byte  para commandClass
    commandFunction =  int.from_bytes(msg[3:4], "big") # 1 byte para Function
    length = int.from_bytes(msg[4:6], "big") # Dois bytes para tamanaho da menssagem
    hex_code = msg[6:]
    
    return {
        'channel' : id_channel,
        'commandClass' : commandClass,
        'commandFunction', commandFunction,
        'length': length,
        'code' : hex_code
    }

def commonCMD_functions():
    
    return = {
        1: QueryTEDS,
        2: ReadTEDSSegment,
    }

def XdcrOperate_functions():

    return {
    }


def parse_msg(msg):
    
    id_channel = int.from_bytes(msg[:2], "big") # Dois primeiros bytes para id channel 
    commandClass = int.from_bytes(msg[2:3], "big") # 1 byte  para commandClass
    commandFunction =  int.from_bytes(msg[3:4], "big") # 1 byte para Function
    length = int.from_bytes(msg[4:6], "big") # Dois bytes para tamanaho da menssagem
    hex_code = msg[6:]
    
    return {
        'channel' : id_channel,
        'commandClass' : commandClass,
        'commandFunction', commandFunction,
        'length': length,
        'code' : hex_code
    }

def callback(xbee_msg):
    
    msg = parse_msg(xbee_msg)
        
    class_command = {
        1 : commonCMD_functions(),
        3 : XdcrOperate_functions()
    }

    try:
        command = class_command[cmd]
        response = command[function](msg).byteMesg()
        
    except KeyError:
        '''
           response error format
        '''
        respose = make_error()
        
    return response 

if __name__ == '__main__':
    
    xbee = xBeeConnect()
    xbee.connect()
    xbee.get(callback)
