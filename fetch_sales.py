import mysql.connector
import pandas as pd

# Connect to MySQL
db_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SHAIKali7@",
    database="sales_db"
)
cursor = db_conn.cursor()

# Fetch sales data with customer details
query = """
SELECT s.sale_id, c.name AS customer_name, c.country, s.product, s.quantity, s.price, s.sale_date 
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id;
"""
cursor.execute(query)

# Convert the result to a DataFrame
data = cursor.fetchall()
columns = ["Sale ID", "Customer Name", "Country", "Product", "Quantity", "Price", "Sale Date"]
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv("sales_data.csv", index=False)

# Close the connection
cursor.close()
db_conn.close()

print("Sales data exported to sales_data.csv successfully!")



