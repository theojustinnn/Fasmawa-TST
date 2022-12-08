from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship

from database import connection
	
class ListFasilitas(connection.Base):
    __tablename__ = 'listfasilitas'

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, index=True)
    lokasi = Column(String, ForeignKey('lokasi.nama'))