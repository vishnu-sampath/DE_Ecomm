import os
import random
import mysql.connector
from datetime import date, timedelta
from dotenv import load_dotenv

def main():
    
    load_dotenv()

    conn = mysql.connector.connect(
        host = os.getenv("MYSQL_HOST"),
        port = int(os.getenv("MYSQL_PORT")),
        user = os.getenv("MYSQL_USER"),
        password = os.getenv("MYSQL_PASSWORD"),
        database = os.getenv("MYSQL_DATABASE")        
    )

    cursor = conn.cursor()
    cursor.execute("TRUNCATE TABLE returns")

    cursor.execute("SELECT sale_id, product_id, sale_date, unit_price, quantity FROM sales")

    sales_data = {
        row[0]: {
            "product_id": row[1],
            "sale_date": row[2],
            "unit_price": row[3],
            "quantity": row[4]
        }
        for row in cursor.fetchall()
    }


    returns = []

    for return_id in range(1, 5001):
        sale_id = random.choice(list(sales_data.keys()))
        sale = sales_data[sale_id]

        today = date.today()

        max_days = min(30, (today - sale["sale_date"]).days)

        return_date = sale["sale_date"] + timedelta(
            days=random.randint(1, max(1, max_days))
        )

        quantity_returned = random.randint(1, sale["quantity"])

        returns.append((
            return_id,
            sale_id,
            sale["product_id"],
            return_date,
            quantity_returned,
            sale["unit_price"]
        ))


    cursor.executemany("""
    INSERT INTO returns
    (return_id, sale_id, product_id, return_date, quantity_returned, unit_price)
    VALUES (%s, %s, %s, %s, %s, %s)
    """, returns)

    conn.commit()
    print("Inserted 5000 returns")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()