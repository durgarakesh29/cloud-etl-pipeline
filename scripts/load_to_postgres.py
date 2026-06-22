# load_to_postgres.py

import pandas as pd
from sqlalchemy import create_engine

# Read transformed file
df = pd.read_csv(
    r"C:\Users\durga\OneDrive\Desktop\Cloud-ETL-Project\output\final_sales.csv"
)

# PostgreSQL connection
engine = create_engine(
    "postgresql+psycopg2://postgres:postgres123@localhost:5432/etl_db"
)

# Load table
df.to_sql(
    "sales_data",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully!")