
#def proces_query(question):
#    if "sales" in question.lower():
#        return {
#           "sql":"SELECT * FROM sales LIMIT 5",
#            "insight":"Sales data retrieved"
 #       }
  #  return{
   #     "sql":"SELECT * FROM customers LIMIT 5",
    #    "insight":"Customer data retrieved"
    #}

from app.query_mapper import generate_sql
from app.sql_engine import run_sql_query
from app.llm_service import generate_insight


def process_query(question):

    # Step 1 → generate SQL
    sql_query = generate_sql(question)

    if not sql_query:
        return {
            "error": "Could not generate SQL for this question"
        }

    # Step 2 → execute SQL
    data = run_sql_query(sql_query)

    # Step 3 → generate insights
    insight = generate_insight(question, data)

    return {
        "question": question,
        "sql_query": sql_query,
        "data": data,
        "insight": insight
    }