import mysql.connector
from faker import Faker

def main():
    fake = Faker()

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Password@123",
        database = "de_ecomm",
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