"""
        CREATE TABLE part_drawings (
                part_id INTEGER PRIMARY KEY,
                file_extension VARCHAR(5) NOT NULL,
                drawing_data BYTEA NOT NULL,
                FOREIGN KEY (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """

from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PartDrawing(Base):
    __tablename__ = 'part_drawings'

    part_id = Column(Integer, ForeignKey("parts.part_id"), primary_key=True)
    file_extension = Column(String, nullable=False)
    drawing_data = Column(LargeBinary, nullable=False)

    # Define relationship
    part = relationship('Part', back_populates='part_drawings')