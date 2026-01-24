import mysql.connector
from faker import Faker

def main():
    faker = Faker()

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Password@123",
        database = "de_ecomm"
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