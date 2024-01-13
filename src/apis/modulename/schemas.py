from datetime import datetime
from typing import List, Optional, Dict
from pydantic import BaseModel




class UserBaseSchema(BaseModel):
    name: str
    age : int
    country: str
    city : str
    code : str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
    
    def __init__(self, name: str, age: int, country: str, city: str, code:str ) -> None:
        super().__init__(name=name, age=age, city=city, country=country,code=code)