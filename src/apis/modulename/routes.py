from typing import Any, Dict
from fastapi import APIRouter
from fastapi import APIRouter, Depends, status
from . import views
from . import schemas
from core.database import get_db
from sqlalchemy.orm import Session


router = APIRouter( 
    prefix="/api/v1/module-name",
    tags=["auth"],
    responses={404: {"description": "Module Not Fount"}},
)



@router.get('/get-data/{url_params}/', tags=["all"], status_code=status.HTTP_200_OK)
def first_get_req_data(url_params):
    return views.my_get_req_dat(url_params = url_params)
 


# @router.post('/add-data/', tags=["all"], status_code=status.HTTP_201_CREATED)
# def create_data(payload: schemas.UserBaseSchema, db:Session = Depends(get_db)):
#     return views.create_data_demo(payload, db)


router_name = router