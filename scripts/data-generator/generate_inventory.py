import random
import mysql.connector
from datetime import date

def main():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password@123",
        database="de_ecomm"
    )
    cursor = conn.cursor()

    cursor.execute("TRUNCATE TABLE inventory")

    inventory = []
    inventory_id = 1

    snapshot_dates = [date(2024, m, 1) for m in range(1, 13)] + [
                        date(2025, m, 1) for m in range(1, 13)]

    for product_id in range(1, 301):
        for warehouse_id in range(1, 6):
            base_qty = random.randint(50, 500)

            for snapshot_date in snapshot_dates:
                inventory.append((
                    inventory_id,
                    product_id,
                    warehouse_id,
                    max(0, base_qty + random.randint(-50, 50)),
                    snapshot_date
                ))
                
                inventory_id += 1

    cursor.executemany("""
    INSERT INTO inventory
    (inventory_id, product_id, warehouse_id, quantity_available, snapshot_date)
    VALUES (%s, %s, %s, %s, %s)
    """, inventory)

    conn.commit()
    print(f"Inserted {len(inventory)} inventory records")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()