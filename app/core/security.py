from passlib.context import CryptContext
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer

crypt_context=CryptContext(schemes=['bcrypt'],deprecated='auto')

