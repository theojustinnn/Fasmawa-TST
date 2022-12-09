from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import connection
from auth import schemas as AuthSchemas, services as AuthServices

from . import services, schemas, models

router = APIRouter(
	prefix='/fasilitas',
	tags=['Fasilitas']
)

# Inisialisasi database
models.connection.Base.metadata.create_all(bind=connection.engine)

# Create data penggunaan fasilitas baru
@router.post('/new', status_code=201)
async def create_penggunaan_fasilitas(fasilitas:schemas.CreateFasilitas, db:Session=Depends(connection.get_db), authenticated_user: AuthSchemas.AuthenticatedUser=Depends(AuthServices.get_current_user)):
	return await services.create_fasilitas(fasilitas=fasilitas, db=db)

# Update data penggunaan fasilitas
@router.put('/update', status_code=200)
async def update_penggunaan_fasilitas(nama: str, hari: str, waktu: str, pengguna: str, db:Session=Depends(connection.get_db), authenticated_user: AuthSchemas.AuthenticatedUser=Depends(AuthServices.get_current_user)):
	return await services.update_fasilitas(nama=nama, hari=hari, pengguna=pengguna, waktu=waktu, db=db)

# Delete data penggunaan fasilitas
@router.delete('/delete', status_code=200)
async def delete_penggunaan_fasilitas(nama: str, hari: str, waktu: str, pengguna: str, db:Session=Depends(connection.get_db), authenticated_user: AuthSchemas.AuthenticatedUser=Depends(AuthServices.get_current_user)):
	return await services.delete_fasilitas(nama=nama, hari=hari, pengguna=pengguna, waktu=waktu, db=db)

# Get semua penggunaan fasilitas
@router.get('', response_model=List[schemas.Fasilitas])
async def get_semua_penggunaan_fasilitas(db:Session=Depends(connection.get_db)):
	return await services.get_all_fasilitas(db=db)

# Get penggunaan fasilitas berdasarkan lokasi
@router.get("/{lokasi}", response_model=List[schemas.Fasilitas])
async def get_penggunaan_fasilitas_berdasarkan_lokasi(lokasi: str, db:Session=Depends(connection.get_db), authenticated_user: AuthSchemas.AuthenticatedUser=Depends(AuthServices.get_current_user)):
	return await services.get_lokasi_fasilitas(lokasi=lokasi, db=db)

# Get rekomendasi fasilitas berdasarkan jumlah pengguna
@router.get("/rekomendasi/{jumlah}")
async def get_rekomendasi_fasilitas(jumlah: int, hari: str, waktu: str, db:Session=Depends(connection.get_db), authenticated_user: AuthSchemas.AuthenticatedUser=Depends(AuthServices.get_current_user)):
	return await services.get_rekomendasi(jumlah=jumlah, hari=hari, waktu=waktu, db=db)
