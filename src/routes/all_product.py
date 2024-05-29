from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from config import get_engine
from sqlalchemy import text
from env import database_table_name
import pandas as pd


router = APIRouter()

# In-memory storage for demonstration
items = {}

# Pydantic model for item
class Item(BaseModel):
    ...

@router.get("/all_product_ids")
def create_item():
    try:
        engine=get_engine()
        with engine.begin() as conn:
            pass
    except:
        raise HTTPException(status_code=404, detail="couldn't connect to database")
    
    # validation for id and id
    try:
        with engine.begin() as conn:
            result=conn.execute(text(f"select * from {database_table_name};"))
            data=result.all()
            if not data:
                raise HTTPException(status_code=500, detail=f"no data found")
            data_=pd.DataFrame(data,columns=result.keys())
    except:
        # we have to create a table_first
        raise HTTPException(status_code=404, detail=f"no data found")
    
    print("rishabh")
    return {"status":"successful","data":str(data_.to_dict(orient="records"))}