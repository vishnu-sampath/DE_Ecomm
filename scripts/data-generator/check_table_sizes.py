import os
import mysql.connector
from dotenv import load_dotenv

def main():
    # ----------------------------
    # CONFIGURATION
    # ----------------------------
    load_dotenv()
    
    DB_CONFIG = {
        "host" : os.getenv("MYSQL_HOST"),
        "port" : int(os.getenv("MYSQL_PORT")),
        "user" : os.getenv("MYSQL_USER"),
        "password" : os.getenv("MYSQL_PASSWORD"),
        "database" : os.getenv("MYSQL_DATABASE")
    }

    TABLES = [
        "sales",
        "inventory",
        "returns",
        "products",
        "customers",
        "stores",
        "warehouses",
        "suppliers"
    ]

    # ----------------------------
    # CONNECT TO DATABASE
    # ----------------------------
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # ----------------------------
    # QUERY TO GET TABLE SIZE
    # ----------------------------
    query = """
    SELECT 
        table_name AS TableName,
        ROUND((data_length + index_length) / 1024 / 1024, 2) AS Size_MB
    FROM information_schema.TABLES
    WHERE table_schema = %s
    AND table_name = %s
    """

    print("Table Sizes (MB):")
    print("------------------")

    # ----------------------------
    # LOOP THROUGH TABLES
    # ----------------------------
    for table in TABLES:
        cursor.execute(query, (DB_CONFIG["database"], table))
        result = cursor.fetchone()
        if result:
            print(f"{result[0]:<12}: {result[1]} MB")
        else:
            print(f"{table:<12}: Not found")

    # ----------------------------
    # CLEAN UP
    # ----------------------------
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()