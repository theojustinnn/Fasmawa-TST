from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
# from auth import schemas as AuthSchemas

from . import models, schemas

# Create fasilitas
async def create_fasilitas(fasilitas: schemas.CreateFasilitas, db:Session) -> schemas.GetFasilitas:
	new_fasilitas = models.Fasilitas(**fasilitas.dict())
	db.add(new_fasilitas)
	db.commit()

	# Return the newly created fasilitas
	db.refresh(new_fasilitas)
	return schemas.GetFasilitas.from_orm(new_fasilitas)

# Get all fasilitas
async def get_all_fasilitas(db: Session) -> List[schemas.GetFasilitas]:
	fasilitas = db.query(models.Fasilitas).all()
	# if fasilitas is None:
	# 	raise HTTPException(status_code=404, detail='You don\'t have any fasilitas.')
	return list(map(schemas.GetFasilitas.from_orm, fasilitas))

# @fasilitas_router.get("/{id}", response_model=Fasilitas)
async def get_id_fasilitas(id: int, db: Session) -> List[schemas.GetFasilitas]:
	fasilitas = db.query(models.Fasilitas).filter(models.Fasilitas.id == id)
	return list(map(schemas.GetFasilitas.from_orm, fasilitas))

async def get_lokasi_fasilitas(loc: str, db: Session) -> List[schemas.GetFasilitas]:
	fasilitas = db.query(models.Fasilitas).filter(models.Fasilitas.lokasi == loc)
	return list(map(schemas.GetFasilitas.from_orm, fasilitas))