# init a base image (Alpine is small Linux distro)
FROM python:3.9-slim

# define the present working directory
RUN mkdir -p /app

# copy the contents into the working dir
COPY /src /app/src

RUN pwd
#WORKDIR /app

# run pip to install the dependencies of the app downloading mysqlclient
RUN apt update && apt install -y build-essential default-libmysqlclient-dev
RUN pip install -r /app/src/requirements.txt

ENV DATABASE_USER='dtsdev' \
    DATABASE_PASSWORD='varaisys123' \
    DATABASE_IP='192.168.29.7' \
    DATABASE_PORT='3306' \
    DATABASE_SCHEMA='umang_db' \
    TABLE_NAME='product_inventory'


WORKDIR /app

EXPOSE 8000

# define the command to start the container
CMD ["python3","src/main.py"]

