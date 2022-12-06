from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import connection

# Import relations
from user.models import User

class Fasilitas(connection.Base):
    __tablename__ = 'fasilitas'

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, index=True)
    lokasi = Column(String, ForeignKey('lokasi.nama'), index=True)
    hari = Column(String)
    jam = Column(String)
    pengguna = Column(String)
    jumlah = Column(Integer)

	# Foreign key
    # user_id = Column(Integer, ForeignKey('users.id'))

	# Relationships
    # writer = relationship('User', back_populates='notes')