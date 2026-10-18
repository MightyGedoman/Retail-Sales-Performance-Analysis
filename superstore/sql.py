import sqlite3
import pandas as pd

# Read CSV
df = pd.read_csv("data.csv")

# Connect to database
conn = sqlite3.connect("superstore.db")


query = """
SELECT *
FROM superstore
LIMIT 10;
"""

df = pd.read_sql_query(query, conn)

print(df)


conn.close()
