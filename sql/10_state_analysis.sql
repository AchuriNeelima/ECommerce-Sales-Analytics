-- State Performance Analysis

SELECT
    state,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders,
    (SUM(profit) / SUM(sales)) * 100 AS profit_margin
FROM sales
GROUP BY state
ORDER BY total_profit DESC
LIMIT 10;