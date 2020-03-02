from sqlalchemy as create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

try:           
    engine = create_engine('sqlite:///ieee1451.sqlite')
    session = sessionmaker(bind=engine) 
    Base = declarative_base

except Exception:
    print("Error connect Database")

