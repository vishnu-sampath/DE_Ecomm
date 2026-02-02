from pyspark.sql import SparkSession
from dotenv import load_dotenv
from pathlib import Path

import os
import shutil

print(">>> SCRIPT STARTED <<<\n", flush=True)

ROOT = Path(__file__).resolve().parents[3]
ENV_PATH = ROOT/"env"/".env"
TMP_SPARK_PATH = ROOT/"scripts"/"spark"/"tmp_spark"

TMP_SPARK_PATH.mkdir(parents=True, exist_ok=True)                  # make sure directory exists

load_dotenv(ENV_PATH)

MYSQL_HOST = os.getenv("MYSQL_HOST") 
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

jdbc_url = f"jdbc:mysql://{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

spark = (
    SparkSession.builder
    .appName("ExtractSales")                                                # name shown in Spark UI and Logs
    .config("spark.jars.packages", "mysql:mysql-connector-java:8.0.33")     # Tell Spark to download the MySQL JDBC Driver
    .config("spark.local.dir", str(TMP_SPARK_PATH))
    .getOrCreate()                                                          # create Spark Session or return exisiting one
)

spark.sparkContext.setLogLevel("ERROR")                                     # suppress warnings and log errors only

print(">>> SPARK SESSION CREATED <<<\n", flush=True)

sales_df = (
    spark.read                                      # read data from mysql into Spark DataFrame
    .format("jdbc")                                 # speacify that the source is a JDBC compatible database
    .option("url", jdbc_url)                        # url tells Spark how to reach MySQL
    .option("dbtable", "sales")                     # name of the table to read from MySQL
    .option("user", MYSQL_USER) 
    .option("password", MYSQL_PASSWORD)
    .option("driver", "com.mysql.cj.jdbc.Driver")   # fully qualified class name of the MySQL JDBC Driver
    .load()                                         # execute the read and return a Spark DataFrame
)

print(">>> DATAFRAME LOADED <<<\n", flush=True)


sales_df.printSchema()
sales_df.show(10)

spark.stop()

# Cleanup Spark temp files (Windows-safe)
try:
    print("Manual cleanup of Spark temp files")
    shutil.rmtree(TMP_SPARK_PATH, ignore_errors=True)
    TMP_SPARK_PATH.mkdir(exist_ok=True)
except Exception as e:
    print(f"Cleanup warning: {e}")
