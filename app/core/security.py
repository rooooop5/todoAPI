from passlib.context import CryptContext
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer

crypt_context=CryptContext(schemes=['bcrypt'],deprecated='auto')

def encrypt_password(password:str):
    return (crypt_context.hash(password))

def verify_password(password:str,db_password:str):
    return (crypt_context.verify(password,db_password))

