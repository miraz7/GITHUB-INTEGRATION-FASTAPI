from core.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import requests
from fastapi.responses import RedirectResponse

GITHUB_CLIENT_ID = ""
GITHUB_CLIENT_SECRET = ""


def login_github(): 
    
    print("I came here")
    return RedirectResponse(
        url="https://github.com/login/oauth/authorize?client_id=c9878e72ce637c337a8c", status_code=302
    )



def github_code(query_params): 
    
    url = 'https://github.com/login/oauth/access_token'
    data = {'client_id': GITHUB_CLIENT_ID ,
            'client_secret' : GITHUB_CLIENT_SECRET,
            "code" : query_params.get('code')
            
            
            }
    x = requests.post(url, json = data)
    
    print(query_params.get('code'))
    
    print(x.text)
    


def get_github_user(query_params):
    
    url = 'https://api.github.com/user'
    
    headers = {'Authorization': "Bearer " ,    
            }
    x = requests.get(url, headers = headers)
    
    print(x.text)
    