from pydantic import BaseModel
from datetime import datetime

# Skema utama
class ListFasilitas(BaseModel):
	nama : str
	lokasi : str

# Skema untuk get
class GetListFasilitas(ListFasilitas):
	pass 

	class Config:
		orm_mode = True

# Skema untuk create
class CreateListFasilitas(ListFasilitas):
	pass 

	class Config:
		orm_mode = True