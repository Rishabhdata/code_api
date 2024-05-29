from sqlalchemy import create_engine,text
from env import *

def get_engine():
    engine = create_engine(f'mysql+pymysql://{database_user}:{database_password}@{database_ip}:{database_port}/{database_database}', echo=False)
    return engine