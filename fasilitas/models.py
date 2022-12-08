from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import connection

# Import relations
from user.models import User

class Fasilitas(connection.Base):
    __tablename__ = 'fasilitas'

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, ForeignKey('listfasilitas.nama'), index=True)
    lokasi = Column(String, ForeignKey('lokasi.nama'), index=True)
    hari = Column(String)
    waktu = Column(String)
    pengguna = Column(String)
    jumlah = Column(Integer)
