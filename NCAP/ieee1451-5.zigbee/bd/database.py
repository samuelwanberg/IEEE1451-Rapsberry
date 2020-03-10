from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Date, Table 
from datetime import date


try:           
    engine = create_engine('sqlite:///ieee1451.sqlite')
    sessionMaker = sessionmaker(bind=engine)
    session = sessionMaker()
    Base = declarative_base()

except Exception:
    print("Error connect Database")

class WTIM(Base):
    __tablename__ = 'wtim'
    Id = Column(Integer, primary_key=True)
    mac = Column(String)
    relasea_date = Column(Date)

def new_mac(_mac):
    
    tim = WTIM( mac = _mac, 
          relasea_date = str(date.today())
    )

    return tim 

def query_MAC(self):
        pass
       
