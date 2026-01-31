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
## Docker MySQL
- cd docker/mysql
- docker compose down -v                        # cleaning the container (if it exists)
- docker compose up -d                          # creates docker container using 'docker-compose.yml' (in /docker/mysql)
- docker exec -it mysql-ecomm mysql -u ecomm_user1 -p       # connect to db as a terminal
- cd ../../scripts/data-generator
- python run_all_generators.py
