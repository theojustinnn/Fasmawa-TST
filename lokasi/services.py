from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from . import models, schemas
from fasilitas import models as fasmod
from fasilitas import schemas as faschem

# Get semua lokasi
async def get_all_lokasi(db: Session) -> List[schemas.GetLokasi]:
	fasilitas = db.query(models.Lokasi).all()
	if fasilitas is None:
		return {"Details" : "Tidak ada lokasi yang terdata"}
	return list(map(schemas.GetLokasi.from_orm, fasilitas))
