from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import connection
from auth import schemas as AuthSchemas, services as AuthServices

from . import models, schemas, services

router = APIRouter(
	prefix='/listfasilitas',
	tags=['ListFasilitas']
)

# Inisialisasi database user
models.connection.Base.metadata.create_all(bind=connection.engine)

# Create fasilitas baru
@router.post('/new', status_code=201)
async def create_list_fasilitas(listfasilitas:schemas.CreateListFasilitas, db:Session=Depends(connection.get_db), authenticated_user: AuthSchemas.AuthenticatedUser=Depends(AuthServices.get_current_user)):
	return await services.create_list_fasilitas(listfasilitas=listfasilitas, db=db)

# Delete fasilitas
@router.delete('/delete', status_code=200)
async def delete_list_fasilitas(nama: str, db:Session=Depends(connection.get_db), authenticated_user: AuthSchemas.AuthenticatedUser=Depends(AuthServices.get_current_user)):
	return await services.delete_list_fasilitas(nama=nama, db=db)

# Get semua fasilitas yang terdata
@router.get('', response_model=List[schemas.ListFasilitas])
async def get_list_fasilitas(db:Session=Depends(connection.get_db)):
	return await services.get_list_fasilitas(db=db)