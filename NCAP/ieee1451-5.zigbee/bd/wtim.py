from sqlalchemy import Column, String, Integer, Data, Table, Foreignkey 
from database import Base

class Wtim(Base):
    
    __tablename__ = 'wtim'
    
    id = Column(Interger, primary_key=True)
    name = Column(String)
    relasea_date = Column(Date)

    def __init__(self, name, release_date):
        self.name = name
        self.release_date = release_date


class Zigbee(Base):

    __tablename__ = 'mac'

    id = Column(Interger, primary_key=True)
    mac = Column(String)
    relasea_date = Column(Date)

    def __init__(self, mac, release_date):
        self.mac = mac
        self.release_date = release_date

    
wtim_zigbee_association = Table(
    'wtim_zigbee', Base.metadata,
    Column('wtim_id', Integer, Foreignkey('wtim.id')),
    Column('zigbee_id', Integer, Foreignkey('mac.id'))
)
