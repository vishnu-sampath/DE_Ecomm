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
    cursor.execute("TRUNCATE TABLE customers")

    customers = []

    for customer_id in range(1, 2001):
        customers.append((
            customer_id,
            faker.name(),
            faker.email(),
            faker.phone_number(),
            faker.city(),
            faker.state(),
            faker.country()
        ))

    cursor.executemany("""
    INSERT INTO customers
    (customer_id, customer_name, email, phone, city, state, country)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, customers)

    conn.commit()
    print("Inserted 2000 customers")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()