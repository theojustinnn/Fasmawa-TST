from typing import List
from sqlalchemy.orm import Session
# from auth.services import Hash

from . import models, schemas

# Create fasilitas baru
async def create_list_fasilitas(listfasilitas: schemas.CreateListFasilitas, db:Session) -> schemas.CreateListFasilitas:
	new_listfasilitas = models.ListFasilitas(**listfasilitas.dict())
	db.add(new_listfasilitas)
	db.commit()

	db.refresh(new_listfasilitas)
	return schemas.CreateListFasilitas.from_orm(new_listfasilitas)

# Delete fasilitas
async def delete_list_fasilitas(nama: str, db:Session) -> schemas.GetListFasilitas:
	deleted_fasilitas = db.query(models.Fasilitas).\
		filter(models.ListFasilitas.nama == nama).\
			delete(synchronize_session=False)
	db.commit()
	return {"status" : "berhasil"}

# Get semua fasilitas
async def get_list_fasilitas(db: Session) -> List[schemas.GetListFasilitas]:
	fasilitas = db.query(models.ListFasilitas).\
		order_by(models.ListFasilitas.lokasi, models.ListFasilitas.nama).\
			all()
	if fasilitas is None:
		return {"Details" : "Tidak ada fasilitas yang terdaftar"}
	return list(map(schemas.GetListFasilitas.from_orm, fasilitas))