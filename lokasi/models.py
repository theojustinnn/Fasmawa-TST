from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import connection

# Import relations
from user.models import User

class Lokasi(connection.Base):
    __tablename__ = 'lokasi'

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, index=True)
    kapasitas = Column(Integer)

	# Foreign key
    # user_id = Column(Integer, ForeignKey('users.id'))

	# Relationships
    # writer = relationship('User', back_populates='notes')