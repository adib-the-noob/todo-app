from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from fastapi.responses import JSONResponse

from schemas.user_auth_schema import UserAuthSchema, UserInDB
from db import db_dependency
from typing import Annotated

router = APIRouter(
    prefix='/auth',
    # tags='auth'    
)


