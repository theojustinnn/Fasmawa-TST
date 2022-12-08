from pydantic import BaseModel

# Skema utama
class Lokasi(BaseModel):
	nama : str
	kapasitas : int

# Skema untuk get
class GetLokasi(Lokasi):
	pass

	class Config:
		orm_mode = True
