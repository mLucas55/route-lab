USE my_guitar_shop;

# SIMPLE SINGLE TABLE QUERIES
SELECT * FROM addresses;
SELECT * FROM administrators;
SELECT * FROM categories;
SELECT * FROM customers;
SELECT * FROM order_items;
SELECT * FROM orders;
SELECT * FROM products;

# INNER JOINS
SELECT o.order_id, oi.product_id
FROM orders o
INNER JOIN order_items oi ON o.order_id = oi.order_id;

SELECT oi.order_id, p.product_name
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.product_id;

SELECT c.email_address, c.customer_id
FROM customers c
INNER JOIN addresses a ON c.customer_id = a.customer_id

SELECT c.first_name, c.last_name, o.order_date
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id;

SELECT p.product_name, cat.category_name
FROM products p
INNER JOIN categories cat ON p.category_id = cat.category_id;

# Functions & Group By
SELECT 
    order_id,
    order_date,
    ship_date,
    DATEDIFF(ship_date, order_date) AS days_to_ship
FROM orders
WHERE ship_date IS NOT NULL;

SELECT 
    customer_id,
    COUNT(*) AS total_orders
FROM orders
GROUP BY customer_id;

SELECT 
    category_id,
    COUNT(*) AS product_count
FROM products
GROUP BY category_id;

SELECT 
    order_id,
    COUNT(*) AS item_count
FROM order_items
GROUP BY order_id;

SELECT 
    state,
    COUNT(*) AS customer_count
FROM addresses
GROUP BY state;

















