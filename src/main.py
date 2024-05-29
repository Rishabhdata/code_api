from fastapi import FastAPI
from routes import all_product, delete_product,single_product,update_product
import uvicorn
from config import get_engine,text
from env import database_table_name,database_database
import sys

## validating the database
engine=None
try:
    engine=get_engine()
    with engine.begin() as conn:
        pass
    print(f"database {database_database} exist we can proceed further")
except:
    if engine:engine.dispose()
    error=f"database {database_database} doesn't exist"
    print("create a database first to run this api")
    sys.exit(1)
    
## creating table if not exist
try:
    with engine.begin() as conn:
        query=f"select* from {database_table_name}"
        conn.execute(text(query))
        print("table found")
except:
    print(f"since table {database_table_name} doesn't exist we will create it first")
    with engine.begin() as conn:
        query=f"""CREATE TABLE IF NOT EXISTS {database_table_name} (
                    id int PRIMARY KEY,
                    name text NOT NULL,
                    category text NOT NULL,
                    price float);"""
        conn.execute(text(query))
        print("table created")

app = FastAPI()

# Include the routers
app.include_router(all_product, prefix="/all_product", tags=["all_product"])
app.include_router(delete_product, prefix="/delete_product", tags=["delete_product"])
app.include_router(single_product, prefix="/single_product", tags=["single_product"])
app.include_router(update_product, prefix="/update_product", tags=["update_product"])

@app.get("/rishabh")
def read_root():
    return {"Hello": "World"}

# Run the application
if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000) # host="0.0.0.0"