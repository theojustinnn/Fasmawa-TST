from pydantic import BaseModel
from datetime import datetime

# Skema utama
class User(BaseModel):
	username:str
	password:str
	email:str

class BaseUser(User):
	id:int
	date_created:datetime

	class Config:
		orm_mode = True

# Skema untuk create
class CreateUser(User):
	pass

	class Config:
		orm_mode = True

# Skema untuk get
class GetUser(BaseModel):
	username:str
	email:str

	class Config:
		orm_mode = True
