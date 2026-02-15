from pyspark.sql import SparkSession
from pyspark.sql import functions as F
# from dotenv import load_dotenv
# from pathlib import Path

import os

print(">>> SCRIPT STARTED <<<\n", flush=True)

ROOT = "/opt/project"

MYSQL_HOST = os.getenv("MYSQL_HOST") 
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

jdbc_url = f"jdbc:mysql://{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

spark = (
    SparkSession.builder
    .appName("ExtractSalesToParquet")                   # name shown in Spark UI and Logs
    .getOrCreate()                                      # create Spark Session or return exisiting one
)

spark.sparkContext.setLogLevel("ERROR")                 # suppress warnings and log errors only

print(">>> SPARK SESSION CREATED <<<\n", flush=True)

sales_df = (
    spark.read                                          # read data from mysql into Spark DataFrame
    .format("jdbc")                                     # speacify that the source is a JDBC compatible database
    .option("url", jdbc_url)                            # url tells Spark how to reach MySQL
    .option("dbtable", "sales")                         # name of the table to read from MySQL
    .option("user", MYSQL_USER) 
    .option("password", MYSQL_PASSWORD)
    .option("driver", "com.mysql.cj.jdbc.Driver")       # fully qualified class name of the MySQL JDBC Driver
    .load()                                             # execute the read and return a Spark DataFrame
)

print(">>> DATAFRAME LOADED FROM Sales Table <<<\n", flush=True)


sales_df.printSchema()

latest_sale_date = (
   sales_df
    .agg(F.max("sale_date").alias("latest_sale_date"))
    .collect()[0]["latest_sale_date"]
)

one_month_ago = F.date_sub(F.lit(latest_sale_date), 30)

filtered_sales_df = (
    sales_df
    .filter(F.col("sale_date") >= one_month_ago)
)

print(">>> Writing Parquet Files <<<\n", flush = True)

OUTPUT_PATH = f"{ROOT}/data/bronze/sales"
print(OUTPUT_PATH)

(
    filtered_sales_df
    .write
    .mode("overwrite")
    .partitionBy("sale_date")
    .parquet(str(OUTPUT_PATH))
)

spark.stop()

print(">>> Parquet files for 30 days of sales_data created successfully <<<", flush=True)