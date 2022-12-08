from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey

from database import connection
from user.models import User

class Lokasi(connection.Base):
    __tablename__ = 'lokasi'

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, index=True)
    kapasitas = Column(Integer)
