# Write your MySQL query statement below
-- avg(selling), round 2
SELECT p.product_id, 
  ROUND(coalesce(SUM(price * units) / SUM(units),0), 2) AS average_price
FROM Prices p
left JOIN UnitsSold s
ON p.product_id = s.product_id
AND purchase_date BETWEEN start_date AND end_date
GROUP BY p.product_id