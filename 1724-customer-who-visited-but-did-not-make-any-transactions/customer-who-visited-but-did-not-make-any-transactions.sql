# Write your MySQL query statement below
-- select distinct customer_id,count(*) as count_no_trans from visits where Visit_id not in(select distinct visit_id from transactions) group by customer_id


SELECT 
    v.customer_id,
    count(*)as count_no_trans
FROM 
    Visits v
LEFT JOIN 
    Transactions t
using(visit_id)
where transaction_id is null
group by customer_id