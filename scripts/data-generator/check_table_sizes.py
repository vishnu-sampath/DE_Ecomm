import mysql.connector

def main():
    # ----------------------------
    # CONFIGURATION
    # ----------------------------
    DB_CONFIG = {
        "host": "localhost",
        "user": "root",
        "password": "Password@123",
        "database": "de_ecomm"
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