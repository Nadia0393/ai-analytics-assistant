import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="analytics_db",
    user="admin",
    password="password123"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT,
    customer_name TEXT,
    churn_status TEXT,
    monthly_spend FLOAT
)
""")

cursor.execute("""
INSERT INTO customers VALUES
(1, 'Alice', 'Yes', 120),
(2, 'Bob', 'No', 80),
(3, 'Charlie', 'Yes', 150)
""")

conn.commit()

cursor.close()
conn.close()

print("PostgreSQL setup complete")