
from pydantic import BaseModel
# from datetime import datetime


class Fasilitas(BaseModel):
	nama : str
	lokasi : str
	hari : str
	jam : str
	pengguna : str
	jumlah : int

# Get all attributes
class BaseFasilitas(Fasilitas):
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
class CreateFasilitas(Fasilitas):
	nama : str
	lokasi : str
	hari : str
	jam : str
	pengguna : str
	jumlah : int

	class Config:
		orm_mode = True

# Get Note schema
class GetFasilitas(Fasilitas):
	id : int
	nama : str
	lokasi : str
	hari : str
	jam : str
	pengguna : str
	jumlah : int

	class Config:
		orm_mode = True