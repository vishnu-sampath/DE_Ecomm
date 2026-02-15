import os
import random
import mysql.connector
from datetime import datetime, timedelta
from dotenv import load_dotenv
from pathlib import Path

def main():
    
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
    cursor.execute("TRUNCATE TABLE sales")

    start_date = datetime.now() - timedelta(days = 5 * 365)
    sales = []

    for sale_id in range(1, 30000):
        sale_date = start_date + timedelta(days=random.randint(0, 5 * 365))
        customer_id = random.randint(1, 2000)
        store_id = random.randint(1, 30)

        num_items = random.randint(1, 5)
        product_ids = random.sample(range(1, 301), num_items)

        for product_id in product_ids:
            sales.append((
                sale_id,
                product_id,
                customer_id,
                store_id,
                sale_date.date(),
                random.randint(1, 5),
                round(random.uniform(10, 1000), 2)
            ))

    cursor.executemany("""
    INSERT INTO sales
    (sale_id, product_id, customer_id, store_id, sale_date, quantity, unit_price)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, sales)

    conn.commit()
    print(f"Inserted {len(sales)} sales")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()