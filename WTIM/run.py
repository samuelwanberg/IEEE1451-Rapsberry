from zigbee.zigConnect import xBeeConnect

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
    
    data_recv = xbee_msg
    msg = parse_msg(data_recv)
    
    class_command = {
        1 : 
        2 :
        3 :

    }

    
    
        
if __name__ == '__main__':
    
    xbee = xBeeConnect()
    xbee.connect()
    xbee.get(callback)
    
