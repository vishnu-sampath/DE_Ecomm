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