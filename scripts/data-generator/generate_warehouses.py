import os
import mysql.connector
from faker import Faker
from dotenv import load_dotenv
from pathlib import Path

def main():
    faker = Faker()

    # Get the path to the .env file in the CURRENT script directory
    env_path = Path(__file__).parent / ".env"
    load_dotenv(dotenv_path=env_path)

    conn = mysql.connector.connect(
        host = os.getenv("MYSQL_HOST"),
        port = int(os.getenv("MYSQL_PORT")),
        user = os.getenv("MYSQL_USER"),
        password = os.getenv("MYSQL_PASSWORD"),
        database = os.getenv("MYSQL_DATABASE")        
    )

    cursor = conn.cursor()
    cursor.execute("TRUNCATE TABLE warehouses")

    warehouses = []

    for warehouse_id in range(1, 6):
        city = faker.city()

        warehouses.append((
            warehouse_id,
            f"{city.capitalize()} Warehouse",
            city,
            faker.state(),
            faker.country()
        ))

    cursor.executemany("""
    INSERT INTO warehouses
    (warehouse_id, warehouse_name, city, state, country)
    VALUES (%s, %s, %s, %s, %s)
    """, warehouses)

    conn.commit()
    print("Inserted 5 warehouses")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()