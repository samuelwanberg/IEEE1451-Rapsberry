from sqlalchemy import Column, String, Integer, Date, Table 
from database import Base

class InputWTIM(Base):

    '''
         Espera-se para este contexto, que sejam armazenadas 
         informação de para cada módulo do zigbee
         uma informação de endereço mac e possivel 
         um nome que possa indetificar um componente 
         físico  além do periodo de inxerção
    '''
    
    __tablename__ = 'wtim'
    
    timId = Column(Integer, primary_key=True)
    mac = Column(String)
    name = Column(String)
    version = Column(String)
    firmware = Column(String)
    protocol = Column(String)
    relasea_date = Column(Date)

    def __init__(self):
        pass

    def input_new(self,mac,name, version, firmware, protocol):
        self.mac = mac
        self.name = name
        self.version = version
        self.firmware = firmware
        self.protocol = protocol
        self.release_date = str( date.today())
        
    def query(self):

        
