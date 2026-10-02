-- Product Performance Analysis

-- 1. Top 10 Products by Sales
SELECT
    product_name,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;


-- 2. Top 10 Products by Profit
SELECT
    product_name,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY product_name
ORDER BY total_profit DESC
LIMIT 10;


-- 3. Bottom 10 Products by Profit
SELECT
    product_name,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY product_name
ORDER BY total_profit ASC
LIMIT 10;