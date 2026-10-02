-- Customer Segment Performance Analysis

SELECT
    segment,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity,
    COUNT(DISTINCT order_id) AS total_orders,
    (SUM(profit) / SUM(sales)) * 100 AS profit_margin
FROM sales
GROUP BY segment
ORDER BY total_profit DESC;