import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()


def run_sql_query(query):

    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    cursor = conn.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()

    columns = [desc[0] for desc in cursor.description]

    results = []

    for row in rows:
        results.append(dict(zip(columns, row)))

    cursor.close()
    conn.close()

    return results