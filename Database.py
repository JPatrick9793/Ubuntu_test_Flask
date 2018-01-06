import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import random
import string
Base = declarative_base()

# create Place table
class Place(Base):
    __tablename__ = 'place'
    id = Column(Integer, primary_key=True)
    address = Column(String(50), index=True)
    city = Column(String)
    country = Column(String)

    # serialize property to return information in JSON format
    @property
    def serialize(self):
        return {
               'id': self.id,
               'address': self.address,
               'city': self.city,
               'country': self.country,
               }

engine = create_engine('sqlite:///places.db')
Base.metadata.create_all(engine)
