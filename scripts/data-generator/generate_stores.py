import os
import mysql.connector
from faker import Faker
from dotenv import load_dotenv
from pathlib import Path

def main():
    fake = Faker()

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
    cursor.execute("TRUNCATE TABLE stores")

    stores = []

    for store_id in range(1, 31):
        stores.append((
            store_id,
            fake.company(),
            fake.city(),
            fake.state(),
            fake.country()
        ))

    cursor.executemany("""
    INSERT INTO stores
    (store_id, store_name, city, state, country)
    VALUES (%s, %s, %s, %s, %s)
    """, stores)

    conn.commit()
    print("Inserted 30 stores")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()