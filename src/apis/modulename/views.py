from core.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import requests


def my_get_req_data(url_params): 
    if url_params :
     return {"data": url_params}
    else:
        raise HTTPException(status_code=400, detail='Channel Not Found')
    
    
