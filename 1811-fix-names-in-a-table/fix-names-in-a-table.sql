select user_id,concat(upper(left(name,1)) ,lower(substring(name,2))) as name  from Users order by user_id;
# Write your MySQL query statement below
-- SELECT user_id ,concat(upper(left(name,1)),lower(SUBSTRING(name,2))) as name from Users group by user_id
