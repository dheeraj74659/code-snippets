""" CREATE TABLE parts (
                part_id SERIAL PRIMARY KEY,
                part_name VARCHAR(255) NOT NULL
                )
        """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Part(Base):
    __tablename__ = 'parts'

    part_id = Column(Integer, primary_key=True)
    part_name = Column(String, nullable=False)