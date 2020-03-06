from sqlalchemy import Column, String, Integer, Date, Table 
from database import Base

class WTimZigbee(Base):

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
    relasea_date = Column(Date)

    def __init__(self, name, mac,  release_date):
        self.name = name
        self.mac = mac
        self.release_date = release_date

    

wtim_zigbee_association = Table(
    'wtim_zigbee', Base.metadata,
    Column('wtim_id', Integer, ForeignKey('wtim.id'))
)
