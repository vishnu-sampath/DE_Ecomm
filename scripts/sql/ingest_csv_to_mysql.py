import pandas as pd
import mysql.connector
import os

# MYSQL Connection
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Password@123",
    database = "de_ecomm"
)

cursor = conn.cursor()

DATA_DIR = "../../data/raw/"

TABLES = [
    "products",
    "customers",
    "suppliers",
    "warehouses",
    "stores",
    "inventory",
    "sales",
    "returns"
]

for table in TABLES:
    file_path = os.path.join(DATA_DIR, f"{table}.csv")
    if not os.path.exists(file_path):
        print(f"Skipping '{table}': CSV not found at {file_path}")
        continue
    
    print(f"\nLoading table: {table}")
    df = pd.read_csv(file_path)
    df = df.where(pd.notnull(df), None)

    columns = ",".join(df.columns)
    placeholders = ",".join(["%s"] * len(df.columns))

    insert_sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

    for row in df.itertuples(index = False):
        cursor.execute(insert_sql, tuple(row))
    
    conn.commit()
    
    print(f"Inserted {len(df)} rows into {table}")

    ## Validation

    select_sql = f"SELECT * FROM {table}"
    cursor.execute(select_sql)
    rows = cursor.fetchall()

    print(f"Top rows in {table} are: \n")

    for r in rows[ : 5]:
        print(r)
    
cursor.close()
conn.close()

print("\nInitial ingestion to de_ecomm DB completed.")