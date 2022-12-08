from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import connection
from auth import schemas as AuthSchemas, services as AuthServices

from . import services, schemas, models

router = APIRouter(
	prefix='/keramaian',
	tags=['Keramaian']
)

# Inisialisasi database
models.connection.Base.metadata.create_all(bind=connection.engine)

# Get keramaian lokasi
@router.get("/lokasi")
async def get_perkiraan_keramaian(lokasi: str, hari: str, waktu: str, db:Session=Depends(connection.get_db)):
	return await services.get_keramaian(lokasi=lokasi, hari=hari, waktu=waktu, db=db)

# Get keramaian fasilitas
@router.get("/nama")
async def get_perkiraan_keramaian_fasilitas(nama: str, hari: str, waktu: str, db:Session=Depends(connection.get_db)):
	return await services.get_keramaian_fasilitas(nama=nama, hari=hari, waktu=waktu, db=db)