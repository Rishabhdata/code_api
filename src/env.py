import dotenv
import os

dotenv.load_dotenv(".env")

database_user=os.getenv("DATABASE_USER",None)
database_password=os.getenv("DATABASE_PASSWORD",None)
database_ip=os.getenv("DATABASE_IP",None)
database_port=os.getenv("DATABASE_PORT",None)
database_database=os.getenv("DATABASE_SCHEMA",None)
database_table_name=os.getenv("TABLE_NAME",None)

