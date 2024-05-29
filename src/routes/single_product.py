from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from config import get_engine
from sqlalchemy import text
from env import database_table_name

router = APIRouter()

# In-memory storage for demonstration
items = {}

# Pydantic model for item
class Item(BaseModel):
    id: int
    
class ItemResponse(Item):
    data: str  # Additional field for the response

@router.post("/single_record", response_model=ItemResponse)
def create_item(item: Item):
    item_id=item.id
    try:
        engine=get_engine()
        with engine.begin() as conn:
            pass
    except:
        raise HTTPException(status_code=404, detail="couldn't connect to database")
    
    # validation for id and id
    try:
        with engine.begin() as conn:
            result=conn.execute(text(f"select * from {database_table_name} where id={item_id}"))
            data=result.all()
            if not data:
                raise HTTPException(status_code=500, detail=f"id {item_id} doesn't exist")
    except:
        # we have to create a table_first
        raise HTTPException(status_code=404, detail=f"id {item_id} doesn't exist")
    
    # retreiving record 
    dict_={'id':item_id}
    dictt={"id":data[0][0],"name":data[0][1],"category":data[0][2],"price":data[0][3]}
    response = {**dict_, "data": str(dictt)}
    return response