-- Monthly Sales & Profitability Analysis

SELECT
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity,
    COUNT(DISTINCT order_id) AS total_orders
FROM sales
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY year, month;