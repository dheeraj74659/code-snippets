"""
        CREATE TABLE vendor_parts (
                vendor_id INTEGER NOT NULL,
                part_id INTEGER NOT NULL,
                PRIMARY KEY (vendor_id , part_id),
                FOREIGN KEY (vendor_id)
                    REFERENCES vendors (vendor_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (part_id)
                    REFERENCES parts (part_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class VendorPart(Base):
    __tablename__ = "vendor_parts"

    vendor_id = Column(Integer, ForeignKey('vendors.vendor_id') , primary_key=True)
    part_id = Column(Integer, ForeignKey('parts.part_id') , primary_key=True)

    # Define relationships
    vendor = relationship('Vendor', back_populates='vendor_id')
    part = relationship('Part', back_populates='part_id')