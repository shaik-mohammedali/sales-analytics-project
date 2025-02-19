import mysql.connector

# Connect to MySQL
db_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SHAIKali7@",
    database="sales_db"
)
cursor = db_conn.cursor()

# Insert sample customer data
customers = [
    ("Michael Brown", "michael@example.com", "Germany"),
    ("Sara Wilson", "sara@example.com", "France"),
    ("David Lee", "david@example.com", "Australia")
]
cursor.executemany("INSERT INTO customers (name, email, country) VALUES (%s, %s, %s)", customers)

# Insert sample sales data
sales = [
    (1, "Monitor", 1, 200.00, "2024-02-13"),
    (2, "Keyboard", 2, 50.00, "2024-02-14"),
    (3, "Mouse", 3, 30.00, "2024-02-15")
]
cursor.executemany("INSERT INTO sales (customer_id, product, quantity, price, sale_date) VALUES (%s, %s, %s, %s, %s)", sales)

# Commit changes and close connection
db_conn.commit()
cursor.close()
db_conn.close()

print("Data inserted successfully!")
