from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("SalesETL") \
    .getOrCreate()

# Read CSV
df = spark.read.csv(
    "data/sales.csv",
    header=True,
    inferSchema=True
)

print("Raw Data")
df.show()

# Cleaning
df = df.dropDuplicates()
df = df.dropna()

# Transformation
df = df.withColumn(
    "revenue",
    col("quantity") * col("price")
)

print("Transformed Data")
df.show()

import pandas as pd

pdf = df.toPandas()

pdf.to_csv(
    "output/final_sales.csv",
    index=False
)

print("CSV created successfully")



spark.stop()