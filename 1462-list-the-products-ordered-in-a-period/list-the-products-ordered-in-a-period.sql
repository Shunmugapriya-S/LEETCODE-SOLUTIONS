# Write your MySQL query statement below
select p.product_name,sum(O.unit) AS unit from Products P join Orders O on P.product_id=O.product_id
where O.order_date>='2020-02-01' and O.order_date<'2020-03-01' 
group by P.product_id,P.product_name 
having sum(unit)>=100