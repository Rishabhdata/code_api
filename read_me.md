we have four routes 

route_first - all_product http://{system_ip}:8000/all_product/all_product_ids - GET request
route_second - single_product http://{system_ip}:8000/single_product/single_record - POST request - {"id":2}
route_third - delete_product http://{system_ip}:8000/delete_product/delete - POST request {"id":2}
route_fourth - update_product http://{system_ip}:8000/update_product/update - POST request {"id":2,"name":"Rishabh","category":"Software","price":"0"}

this code first validates if the database exist if not then throws error then for table if table not exist then it creates one
you also need to provide the mysql db connection details which i have mentioned in .env file

-- docker run command

docker run -itd -p 8000:8000 -e "DATABASE_USER=dtsdev" -e "DATABASE_PASSWORD=varaisys123" -e "DATABASE_IP=192.168.29.7" -e "DATABASE_PORT=3306" -e "DATABASE_SCHEMA=umang_db" -e "TABLE_NAME=product_inventory_1"  test_case

