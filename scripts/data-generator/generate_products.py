import random
import mysql.connector
from faker import Faker

def main():
    fake = Faker()
    random.seed(42)

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Password@123",
        database = "de_ecomm"
    )

    cursor = conn.cursor()
    cursor.execute("TRUNCATE TABLE products")

    CATEGORIES = ["Electronics", "Furniture", "Accessories", "Clothing", "Home", "Sports", "Books"]
    products = []

    for product_id in range(1, 301):
        category = random.choice(CATEGORIES)

        products.append((
            product_id,
            f"{fake.word().capitalize()} {category}",
            category,
            random.randint(1, 20),
            round(random.uniform(5, 500), 2)
        ))

    cursor.executemany("""
    INSERT INTO products
    (product_id, product_name, category, supplier_id, cost_price)
    VALUES (%s, %s, %s, %s, %s)
    """, products)

    conn.commit()
    print("Inserted 300 products")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()