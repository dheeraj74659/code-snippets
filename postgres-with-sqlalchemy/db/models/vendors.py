"""
        CREATE TABLE vendors (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
        """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String

Base = declarative_base()

class Vendor(Base):
    """
    Database model class for vendor table."""

    __tablename__ = 'vendors'

    vendor_id = Column(Integer, primary_key=True)
    vendor_name = Column(String, nullable=False)