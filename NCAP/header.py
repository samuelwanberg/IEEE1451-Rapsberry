
class HeaderMessage:

    '''
        Contrução do Header do pacote com base no Artigo:
        IEEE 1451 Smart Sensor Digital Twin Federation for IoT/CPS Researchh
    
        Field           Length       Description
        Message Type    1 Byte       Type of message 
        MEssage ID      2 Bytes      Funcionalidade Exemplo READBlockDataFromSingle 
        Session No      1 Byte       Identifies the current sesssion 
        Sequence No.    2 Bytes      Identifies the sequence No.
        Status          1 Byte       Error flag.
        Length          2 Bytes      Number of following bytes.      
        Check Sum       2 Bytes      Placed at the end of every message. OUtiside   
    '''

    def __init__(self, typeMessage, messageID, sessionNo, sequecenNo, status, priority, length, checksum=x0):

        self.typeMessage = typeMessage
        self.messageID = messageID
        self.sessionNo = sessionNo
        self.sequeceNo = sequenceNo
        self.status    = status
        self.priority = priority
        self.length = length
        self.checksum = checksum       
    
    def formatMessage(self):
        pass

    
        
        

        
