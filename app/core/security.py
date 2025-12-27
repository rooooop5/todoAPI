from passlib.context import CryptContext
import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime,timedelta,timezone
from pydantic import BaseModel


#-----declaring secret key and algorithm and creating a default expiration time-----
#-----used the following cmd to generate secret key------
#openssl rand -hex 32
SECRET_KEY="ae429b2ec5e5eb0c7b1d4f9e6aed8aa9e302892145ebf6bc41f16e82d70aa38a"
ALGORITHM="HS256"
DEFAULT_ACCESS_TOKEN_EXPIRATION_MINS=25


#-----Token and its model------
class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    username:str|None=None


#------helper function for creating token------
def create_access_token(data:dict):
    to_encode=data.copy()
    expires=datetime.now(timezone.utc)+timedelta(minutes=DEFAULT_ACCESS_TOKEN_EXPIRATION_MINS)
    to_encode.update({"exp":expires})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,ALGORITHM)
    return encoded_jwt


#------Password hashing and verification using context manager------
crypt_context=CryptContext(schemes=['bcrypt'],deprecated='auto')

def encrypt_password(password:str):
    return (crypt_context.hash(password))

def verify_password(password:str,db_password:str):
    return (crypt_context.verify(password,db_password))

