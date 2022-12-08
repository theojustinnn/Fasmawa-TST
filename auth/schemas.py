from typing import Union
from datetime import datetime
from pydantic import BaseModel

# Skema utama
class Login(BaseModel):
	username:str
	password:str

# Skema user terautentikasi
class AuthenticatedUser(BaseModel):
	id:int
	username:str
	password:str
	email:str
	date_created:datetime

# Skema token
class Token(BaseModel):
    access_token: str
    token_type: str

# class TokenData(BaseModel):
#     username: Union[str, None] = None