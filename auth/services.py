from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from typing import Union
from datetime import datetime, timedelta
from passlib.context import CryptContext

from database import connection
from user import models as UserModels
from jose import JWTError, jwt

from . import schemas, models

# Secret key yang didapatkan dari command openssl rand -hex 32
SECRET_KEY = '6e3337f8a63d454372e71a2cf9818f6ee6479667359c3935d1db58141093eb2d'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

PWD_CONTEXT = CryptContext(schemes=['bcrypt'], deprecated='auto')

'''
Create class Hash to manage hashing password
>>> pip install passlib bcrypt 
'''

# Untuk hashing password
class Hash:
	def encrypt(password: str):
		return PWD_CONTEXT.hash(password)

	def verify(plain_password, hashed_password):
		return PWD_CONTEXT.verify(plain_password, hashed_password)

# authscheme yang akan dipanggil
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Login
def login(db:Session, request:OAuth2PasswordRequestForm):
	user = db.query(UserModels.User).filter(UserModels.User.username==request.username).first()
	if not user:
		raise HTTPException(status_code=401, detail='Invalid credentials.')
	if not Hash.verify(request.password, user.password):
		raise HTTPException(status_code=401, detail='Incorrect password')
	
	# return user
	# Instead of returning the user data, this function will return the JWT token
	access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
	access_token = create_access_token(
		data={"sub": user.username}, expires_delta=access_token_expires
	)
	return {"access_token": access_token, "token_type": "bearer"}

# Create access token
def create_access_token(data:dict, expires_delta:Union[timedelta, None]=None):
	to_encode = data.copy()
	if expires_delta:
		expire = datetime.utcnow() + expires_delta
	else:
		expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
	to_encode.update({"exp": expire})
	encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
	return encoded_jwt

# Get user yang saat ini sedang login
async def get_current_user(token:str=Depends(oauth2_scheme), db:Session=Depends(connection.get_db)):
	credentials_exception = HTTPException(
		status_code=status.HTTP_401_UNAUTHORIZED,
		detail="Could not validate credentials",
		headers={"WWW-Authenticate": "Bearer"},
	)

	# Verifikasi token
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		email:str = payload.get("sub")
		if email == None:
			raise credentials_exception
		token_data = schemas.TokenData(username=email)
	except JWTError:
		raise credentials_exception

	# Return user
	user = db.query(UserModels.User).filter(UserModels.User.email==email).first()
	return user