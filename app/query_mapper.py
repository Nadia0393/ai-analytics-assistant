def generate_sql(question):

    question = question.lower()

    # churn analysis
    if "churn" in question:

        return """
        SELECT
            churn_status,
            COUNT(*) AS total_customers
        FROM customers
        GROUP BY churn_status
        """

    # high spending customers
    elif "high spending" in question:

        return """
        SELECT
            customer_name,
            monthly_spend
        FROM customers
        WHERE monthly_spend > 100
        """

    # all customers
    elif "all customers" in question:

        return """
        SELECT *
        FROM customers
        """

    # average spend
    elif "average spend" in question:

        return """
        SELECT
            AVG(monthly_spend) AS average_monthly_spend
        FROM customers
        """

    return None