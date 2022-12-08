from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import connection
from auth import schemas as AuthSchemas, services as AuthServices

from . import models, schemas, services

router = APIRouter(
	prefix='/user',
	tags=['Users']
)

# Inisialisasi database user
models.connection.Base.metadata.create_all(bind=connection.engine)

# Create user baru
@router.post('', status_code=201)
async def create_user(user:schemas.CreateUser, db:Session=Depends(connection.get_db)):
	return await services.create_user(user=user, db=db)

# Get semua user
@router.get('', response_model=List[schemas.GetUser])
async def get_all_users(db:Session=Depends(connection.get_db), authenticated_user: AuthSchemas.AuthenticatedUser=Depends(AuthServices.get_current_user)):
	return await services.get_all_users(db=db)
