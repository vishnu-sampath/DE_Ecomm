#!/bin/bash

# Get the absolute path to the project root (one level up from /pipelines)
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Navigating to Project Root: $PROJECT_ROOT"
cd "$PROJECT_ROOT"

echo "Cleaning old data and starting MySQL Container..."
# -v ensures the volume is wiped so 01_schema.sql runs fresh
docker-compose -f docker/mysql/docker-compose.yml down -v
docker-compose --env-file docker/.env -f docker/mysql/docker-compose.yml up -d

echo "Waiting for MySQL to be healthy..."
# Added spaces inside [ ] and a status check
until [ "$(docker inspect --format='{{.State.Health.Status}}' mysql-ecomm)" == "healthy" ]; do
    printf "."
    sleep 2
done

# --- THE FIX IS HERE ---
echo -e "\nContainer is healthy, but waiting 10s for networking to stabilize..."
sleep 10 
# -----------------------

echo -e "\nMySQL is ready"

echo "Running local data generators..."
# We stay in PROJECT_ROOT so the scripts can resolve internal paths
python scripts/data-generator/run_all_generators.py

echo "Data generation complete."
echo "Checking Schema of tables..."
python scripts/data-generator/check_table_sizes.py

echo "====================== END OF SHELL SCRIPT ============================"