def generate_insight(question, data):

    if not data:
        return "No data available for analysis."

    if "churn" in question.lower():

        yes_count = 0
        no_count = 0

        for row in data:

            if row["churn_status"] == "Yes":
                yes_count = row["total_customers"]

            elif row["churn_status"] == "No":
                no_count = row["total_customers"]

        if yes_count > no_count:
            return (
                "Customer churn appears high. "
                "Retention strategies may be needed for at-risk customers."
            )

        return "Customer retention appears stable."

    return "Data retrieved successfully."