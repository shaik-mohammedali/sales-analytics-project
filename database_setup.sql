CREATE DATABASE sales_db;
USE sales_db;

-- Table for storing customer details
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    country VARCHAR(50)
);

-- Table for storing sales transactions
CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product VARCHAR(100),
    quantity INT,
    price DECIMAL(10,2),
    sale_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Insert sample customer data
INSERT INTO customers (name, email, country) VALUES 
('John Doe', 'john@example.com', 'USA'),
('Jane Smith', 'jane@example.com', 'UK'),
('Alice Johnson', 'alice@example.com', 'Canada');

-- Insert sample sales data
INSERT INTO sales (customer_id, product, quantity, price, sale_date) VALUES 
(1, 'Laptop', 2, 1000.00, '2024-02-10'),
(2, 'Phone', 1, 800.00, '2024-02-11'),
(3, 'Tablet', 3, 500.00, '2024-02-12');
