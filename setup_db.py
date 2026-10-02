import sqlite3

conn = sqlite3.connect("db/customer_data.db")

cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER,
    customer_name TEXT,
    churn_status TEXT,
    monthly_spend REAL
)
""")

# insert sample data
sample_data = [
    (1, "Alice", "Yes", 120.5),
    (2, "Bob", "No", 89.0),
    (3, "Charlie", "Yes", 150.0),
    (4, "David", "No", 75.5),
    (5, "Eva", "Yes", 200.0)
]

cursor.executemany("""
INSERT INTO customers VALUES (?, ?, ?, ?)
""", sample_data)

conn.commit()

print("Database created successfully!")

conn.close()