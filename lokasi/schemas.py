
from pydantic import BaseModel
# from datetime import datetime


class Lokasi(BaseModel):
	nama : str
	kapasitas : int

# Get all attributes
class BaseFasilitas(Lokasi):
	id : int
	nama : str
	lokasi : str
	hari : str
	jam : str
	pengguna : str
	jumlah : int

	class Config:
		orm_mode = True

# Create note schema
class CreateFasilitas(Lokasi):
	nama : str
	lokasi : str
	hari : str
	jam : str
	pengguna : str
	jumlah : int

	class Config:
		orm_mode = True

# Get Note schema
class GetLokasi(Lokasi):
	pass

	class Config:
		orm_mode = True

class GetKepadatan(BaseModel):
	nama : str
	jumlah : int

	class Config:
		orm_mode = True