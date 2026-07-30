-- with reference as (select
-- case 
--    when income<20000 then 'Low Salary'
--    when (income >=20000 and income<=50000) then 'Average Salary'
--    else "High Salary"
-- end  as category from Accounts)
-- select category,count(*) as accounts_count from reference group by category;
select 'Low Salary' as category,sum(income<20000) as accounts_count from Accounts
union all 
select 'Average Salary' as category ,sum(income>=20000 and income<=50000) as accounts_count from Accounts
union all 
select 'High Salary' as category,sum(income>50000) as accounts_count from Accounts;