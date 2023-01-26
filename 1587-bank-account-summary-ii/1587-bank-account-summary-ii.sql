# Write your MySQL query statement below
select u.name name, sum(t.amount) balance from Users u inner join Transactions t on u.account=t.account group by t.account having sum(t.amount)>10000;