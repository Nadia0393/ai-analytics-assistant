import streamlit as st
import requests

st.title("AI Analytics Assistant")

question = st.text_input(
    "Ask a business question:",
    placeholder="Show customer churn trends"
)

if st.button("Run Analysis"):

    response = requests.post(
        "http://127.0.0.1:8000/query",
        json={"question": question}
    )

    result = response.json()

    st.subheader("Generated SQL")
    st.code(result.get("sql_query", ""))

    st.subheader("Analytics Data")
    st.write(result.get("data", []))

    st.subheader("Business Insight")
    st.success(result.get("insight", ""))