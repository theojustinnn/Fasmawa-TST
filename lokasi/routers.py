from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import connection

from . import services, schemas, models
from fasilitas import models as fasmod
from fasilitas import schemas as faschem

router = APIRouter(
	prefix='/lokasi',
	tags=['Lokasi']
)

# Inisialisasi database lokasi
models.connection.Base.metadata.create_all(bind=connection.engine)

# Get semua lokasi
@router.get('', response_model=List[schemas.Lokasi])
async def get_all_lokasi(db:Session=Depends(connection.get_db)):
	return await services.get_all_lokasi(db=db)
