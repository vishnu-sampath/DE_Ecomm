# Omni Channel Retailer - Data Engineering
End-to-end data engineering project using Azure and local Docker for an omni-channel retailer.

## Project Goal
Build an end-to-end data engineering pipeline using Azure Blob Storage and open-source tools for a retailer selling products via two channels - online and brick-and-mortar stores.

## Architecture
All compute components run locally using Docker. Azure Blob Storage is used only for object storage (raw, staged, curated).

## Tech Stack
- Python
- Apache Spark
- Apache Hive
- Apache Kafka
- Apache Druid
- Apache Airflow
- MySQL
- Docker
- Azure Blob Storage
- Power BI Desktop

# Steps
## Python Virtual Environment
- pip install venv                          # if needed
- python -m venv de_py_env                  # creates virtual environment 'de_py_env'
- source ./de_py_env/Scripts/activate       # for linux / gitbash (Activate.ps1 if powershell)
- which python                              # verify
- pip install pyspark mysql-connector-python python-dotenv faker
- pip freeze > requirements.txt

## Docker MySQL
- cd /DE_ECOMM/docker/mysql
- docker compose down -v                        # cleaning the container (if it exists)
- docker compose up -d                          # creates docker container using 'docker-compose.yml' (in /docker/mysql)
- docker exec -it mysql-ecomm mysql -u ecomm_user1 -p       # connect to db as a terminal to check tables
- cd /DE_ECOMM/scripts/data-generator
- python run_all_generators.py                  # generates data using Faker library
