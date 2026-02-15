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
    cursor.execute("TRUNCATE TABLE suppliers")

    suppliers = []

    for supplier_id in range(1, 21):
        suppliers.append((
            supplier_id,
            fake.company(),
            fake.company_email(),
            fake.phone_number(),
            fake.city(),
            fake.state(),
            fake.country()
        ))

    cursor.executemany("""
    INSERT INTO suppliers
    (supplier_id, supplier_name, email, phone, city, state, country)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, suppliers)

    conn.commit()
    print("Inserted 20 suppliers")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()