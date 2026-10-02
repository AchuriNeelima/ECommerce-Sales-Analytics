-- E-Commerce Sales & Profitability Analytics
-- KPI Analysis

-- 1. Total Sales
SELECT SUM(sales) AS total_sales
FROM sales;

-- 2. Total Profit
SELECT SUM(profit) AS total_profit
FROM sales;

-- 3. Total Quantity Sold
SELECT SUM(quantity) AS total_quantity
FROM sales;

-- 4. Total Orders
SELECT COUNT(DISTINCT order_id) AS total_orders
FROM sales;

-- 5. Total Customers
SELECT COUNT(DISTINCT customer_id) AS total_customers
FROM sales;

-- 6. Overall Profit Margin
SELECT
    (SUM(profit) / SUM(sales)) * 100 AS profit_margin
FROM sales;