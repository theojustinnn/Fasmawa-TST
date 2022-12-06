
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import connection
# from auth import schemas as AuthSchemas, services as AuthServices

from . import services, schemas, models
from fasilitas import models as fasmod
from fasilitas import schemas as faschem

router = APIRouter(
	prefix='/lokasi',
	tags=['Lokasi']
)

# Initialize tables
models.connection.Base.metadata.create_all(bind=connection.engine)

# Create fasilitas
# @router.post('/new', status_code=201)
# async def create_fasilitas(fasilitas:schemas.CreateFasilitas, db:Session=Depends(connection.get_db)):
# 	return await services.create_fasilitas(fasilitas=fasilitas, db=db)

# Get all fasilitas
@router.get('', response_model=List[schemas.Lokasi])
async def get_all_lokasi(db:Session=Depends(connection.get_db)):
	return await services.get_all_lokasi(db=db)

# @router.get("/id/{id}", response_model=List[schemas.Fasilitas])
# async def get_fasilitas(id: int, db:Session=Depends(connection.get_db)):
# 	return await services.get_id_fasilitas(id=id, db=db)

# @router.get("/kepadatan", response_model=List[schemas.GetKepadatan])
# async def get_fasilitas(db:Session=Depends(connection.get_db)):
	# return await services.get_fasilitas_lokasi(db=db)