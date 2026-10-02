-- Discount vs Profitability Analysis

SELECT
    discount,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders,
    (SUM(profit) / SUM(sales)) * 100 AS profit_margin
FROM sales
GROUP BY discount
ORDER BY discount;
