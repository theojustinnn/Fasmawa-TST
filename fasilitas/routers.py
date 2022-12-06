
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import connection
# from auth import schemas as AuthSchemas, services as AuthServices

from . import services, schemas, models

router = APIRouter(
	prefix='/fasilitas',
	tags=['Fasilitas']
)

# Initialize tables
models.connection.Base.metadata.create_all(bind=connection.engine)

# Create fasilitas
@router.post('/new', status_code=201)
async def create_fasilitas(fasilitas:schemas.CreateFasilitas, db:Session=Depends(connection.get_db)):
	return await services.create_fasilitas(fasilitas=fasilitas, db=db)

# Get all fasilitas
@router.get('', response_model=List[schemas.Fasilitas])
async def get_all_fasilitas(db:Session=Depends(connection.get_db)):
	return await services.get_all_fasilitas(db=db)

@router.get("/id/{id}", response_model=List[schemas.Fasilitas])
async def get_fasilitas(id: int, db:Session=Depends(connection.get_db)):
	return await services.get_id_fasilitas(id=id, db=db)

@router.get("/lokasi/{loc}", response_model=List[schemas.Fasilitas])
async def get_fasilitas(loc: str, db:Session=Depends(connection.get_db)):
	return await services.get_lokasi_fasilitas(loc=loc, db=db)