
-- Yearly Sales & Profitability Analysis

SELECT
    YEAR(order_date) AS year,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity,
    COUNT(DISTINCT order_id) AS total_orders,
    (SUM(profit) / SUM(sales)) * 100 AS profit_margin
FROM sales
GROUP BY YEAR(order_date)
ORDER BY year;