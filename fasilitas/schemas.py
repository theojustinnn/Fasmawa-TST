from pydantic import BaseModel

# Skema utama
class Fasilitas(BaseModel):
	nama : str
	lokasi : str
	hari : str
	waktu : str
	pengguna : str
	jumlah : int

# Skema untuk create
class CreateFasilitas(Fasilitas):
	pass

	class Config:
		orm_mode = True

# Skema untuk get
class GetFasilitas(Fasilitas):
	id : int

	class Config:
		orm_mode = True
