# Write your MySQL query statement below
delete p2 from Person p join Person p2 ON  strcmp(p.email,p2.email)=0 and p.id<p2.id