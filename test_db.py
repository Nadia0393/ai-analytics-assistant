from app.sql_engine import run_sql_query

query = """
SELECT * FROM customers
"""

result = run_sql_query(query)

print(result)