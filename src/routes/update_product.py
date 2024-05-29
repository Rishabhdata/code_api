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
    name: str
    category: str
    price: float

@router.post("/update", response_model=Item)
def create_item(item: Item):
    item_id,item_name,item_category,item_price=item.id,item.name,item.category,item.price
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
    
    # inserting record 
    try:
        with engine.begin() as conn:
            query=f"update {database_table_name} set name='{item_name}',category='{item_category}',price={item_price} where id={item_id}"
            conn.execute(text(query))
    except:
        raise HTTPException(status_code=404, detail=f"couldn't update record in{database_table_name}")
    
    return {'id':item_id,'name':item_name,'category':item_category,"price":item_price,"status":"processed them"}