from typing import Any, Dict
from fastapi import APIRouter ,Request
from fastapi import APIRouter, Depends, status

from . import views
from . import schemas
from core.database import get_db
from sqlalchemy.orm import Session


router = APIRouter( 
    prefix="/api/v1/github",
    tags=["auth"],
    responses={404: {"description": "Module Not Fount"}},
)



@router.get('/login', tags=["all"], status_code=status.HTTP_200_OK)
def login_with_github():
    return views.login_github()
 

@router.get('/code', tags=["all"], status_code=status.HTTP_200_OK)
def github_code(request: Request):
    query_params =  request.query_params
    return views.github_code(query_params)


@router.get('/get-user', tags=["all"], status_code=status.HTTP_200_OK)
def github_code(request: Request):
    query_params =  request.query_params
    return views.get_github_user(query_params)

github_router = router